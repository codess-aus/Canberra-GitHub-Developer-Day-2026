"""Build the web images used by the site.

1. Generates hero artwork for chapters that do not have a supplied hero image.
2. Generates small WebP thumbnails (used by the home page and chapter cards)
   for every PNG in docs/assets and every generated hero.

Run from the repository root after adding or changing images:

    pip install pillow
    python scripts/build_images.py

The output is committed, so this is only needed when the source images change.
"""

import math
import random
import re
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

ASSETS = Path("docs/assets")
GENERATED = ASSETS / "generated"
THUMBS = ASSETS / "thumbs"

HERO_SIZE = (1480, 835)  # Same 16:9 shape as the supplied hero images
THUMB_WIDTH = 640
SPLIT = 0.46  # Share of the width taken by the text panel

# Palettes follow the supplied hero images: a dark text panel on the left and
# glowing, flowing lines on the right. Accents are the glow colours.
CHAPTERS = {
    2: {
        "eyebrow": "CHAPTER 02",
        "title": "Secure by Design, Modern by Default",
        "subtitle": "Modernising your app to align with PSPF",
        "panel": "#101411",
        "bg": "#0a0e0b",
        "accents": ["#5fed83", "#4aa3ff", "#ae85ff", "#2ea043"],
        "label": "#5fed83",
    },
    3: {
        "eyebrow": "CHAPTER 03",
        "title": "Storytime",
        "subtitle": "",
        "panel": "#1b1f3b",
        "bg": "#140f2c",
        "accents": ["#ff7ab6", "#b392f0", "#ffb86b", "#7c4ddb"],
        "label": "#ff9ccf",
    },
    5: {
        "eyebrow": "CHAPTER 05",
        "title": "Building trustworthy software at scale",
        "subtitle": "Security, governance, compliance and policy",
        "panel": "#10243a",
        "bg": "#07192a",
        "accents": ["#3fd0c9", "#4aa3ff", "#5fed83", "#b392f0"],
        "label": "#6fe3dc",
    },
    6: {
        "eyebrow": "CHAPTER 06",
        "title": "Resources and Workshops",
        "subtitle": "",
        "panel": "#241a35",
        "bg": "#160e25",
        "accents": ["#ff9f43", "#ff6bcb", "#d4f23c", "#b392f0"],
        "label": "#ffb26b",
    },
}

FONT_DIRS = ["/usr/share/fonts/truetype/liberation", "/usr/share/fonts/truetype/dejavu"]


def font(bold: bool, size: int) -> ImageFont.FreeTypeFont:
    """Load a bold or regular sans font, using the first one found."""
    names = (["LiberationSans-Bold.ttf", "DejaVuSans-Bold.ttf"] if bold
             else ["LiberationSans-Regular.ttf", "DejaVuSans.ttf"])
    for folder in FONT_DIRS:
        for name in names:
            if (Path(folder) / name).exists():
                return ImageFont.truetype(str(Path(folder) / name), size)
    return ImageFont.load_default(size)


def glow_art(width: int, height: int, palette: dict, seed: int) -> Image.Image:
    """Flowing glowing lines with bright nodes, drawn on a dark background."""
    rng = random.Random(seed)  # Seeded so the artwork is identical on every run
    lines = Image.new("RGB", (width, height), "black")
    nodes = Image.new("RGB", (width, height), "black")
    draw_lines, draw_nodes = ImageDraw.Draw(lines), ImageDraw.Draw(nodes)

    for _ in range(18):
        centre = rng.uniform(0.2, 0.8) * width
        amplitude = rng.uniform(0.06, 0.32) * width
        frequency = rng.uniform(0.7, 2.0)
        phase = rng.uniform(0, math.tau)
        colour = rng.choice(palette["accents"])
        points = []
        for y in range(0, height + 1, 4):
            t = y / height
            # Lines fan out at the top and pull together toward the bottom
            x = centre + amplitude * math.sin(frequency * t * math.tau + phase) * (1.1 - t)
            points.append((x, y))
        draw_lines.line(points, fill=colour, width=rng.choice([2, 2, 3, 4]), joint="curve")
        for x, y in rng.sample(points, 4):
            r = rng.choice([3, 4, 6])
            draw_nodes.ellipse((x - r, y - r, x + r, y + r), fill="white")
            draw_nodes.ellipse((x - 2 * r, y - 2 * r, x + 2 * r, y + 2 * r), outline=colour, width=2)

    # Screen-blend blurred copies over the background to create the glow
    art = Image.new("RGB", (width, height), palette["bg"])
    for layer, radii in ((lines, (28, 10)), (nodes, (14,))):
        for radius in radii:
            art = ImageChops.screen(art, layer.filter(ImageFilter.GaussianBlur(radius)))
        art = ImageChops.screen(art, layer)
    return art


def spaced_text(draw, xy, text, fill, fnt, spacing):
    """Draw letter-spaced text; Pillow has no tracking option."""
    x, y = xy
    for char in text:
        draw.text((x, y), char, fill=fill, font=fnt)
        x += draw.textlength(char, font=fnt) + spacing


def wrap(draw, text, fnt, max_width):
    lines, current = [], ""
    for word in text.split():
        trial = f"{current} {word}".strip()
        if draw.textlength(trial, font=fnt) <= max_width:
            current = trial
        else:
            lines.append(current)
            current = word
    return lines + [current]


def make_hero(number: int, spec: dict) -> Path:
    width, height = HERO_SIZE
    split = int(width * SPLIT)
    image = Image.new("RGB", HERO_SIZE, spec["panel"])

    # The art fades in from the text panel so there is no hard seam
    art = glow_art(width - split, height, spec, seed=number)
    mask = Image.new("L", art.size, 255)
    mask.paste(Image.linear_gradient("L").rotate(90).resize((180, height)), (0, 0))
    image.paste(art, (split, 0), mask)

    draw = ImageDraw.Draw(image)
    left, max_width = 80, split - 130
    title_font, sub_font = font(True, 60), font(False, 30)
    title_lines = wrap(draw, spec["title"], title_font, max_width)
    sub_lines = wrap(draw, spec["subtitle"], sub_font, max_width) if spec["subtitle"] else []

    # Centre the text block vertically
    block = 80 + len(title_lines) * 72 + (30 + len(sub_lines) * 42 if sub_lines else 0)
    y = (height - block) // 2
    spaced_text(draw, (left, y), spec["eyebrow"], spec["label"], font(True, 26), 5)
    y += 80
    for line in title_lines:
        draw.text((left, y), line, fill="white", font=title_font)
        y += 72
    y += 30
    for line in sub_lines:
        draw.text((left, y), line, fill="#c9cbe0", font=sub_font)
        y += 42

    GENERATED.mkdir(parents=True, exist_ok=True)
    out = GENERATED / f"chapter-{number}-hero.webp"
    image.save(out, "WEBP", quality=88, method=6)
    return out


def slug(path: Path) -> str:
    return re.sub(r"[^a-z0-9]+", "-", path.stem.lower()).strip("-")


def make_thumb(source: Path) -> Path:
    image = Image.open(source).convert("RGB")
    height = round(image.height * THUMB_WIDTH / image.width)
    THUMBS.mkdir(parents=True, exist_ok=True)
    out = THUMBS / f"{slug(source)}.webp"
    image.resize((THUMB_WIDTH, height), Image.LANCZOS).save(out, "WEBP", quality=82, method=6)
    return out


if __name__ == "__main__":
    sources = sorted(ASSETS.glob("*.png"))
    sources += [make_hero(number, spec) for number, spec in CHAPTERS.items()]
    for source in sources:
        print(f"{source.name} -> {make_thumb(source).relative_to(ASSETS)}")
