---
title: "Modern platforms and patching"
chapter: 5
hero: "5.22 Patch.png"
hero_alt: "Slide describing App Service's patched PHP images, Copilot modernization, Azure Migrate and managed databases, with a warning that pinned images and custom containers still need rebuilding."
thumb: "thumbs/5-22-patch.webp"
summary: "Understand which patching responsibilities move to a managed platform and which stay with you."
---

??? note "Text version of this slide"

    The slide uses the PHP2Shell response to illustrate platform-managed patching, while noting that pinned tags and custom containers still need attention. It also points to application modernisation and managed databases.

## Shared responsibility still needs an owner

Managed platforms can reduce the time a team spends maintaining infrastructure and runtimes. The PHP2Shell example describes Azure App Service rolling out patched built-in PHP images when fixes became available. Applications pinned to a full image tag and custom containers still require their owners to rebuild or update them on a patched base image.

Modernisation can also make future fixes easier. GitHub Copilot modernization assists with assessing and upgrading supported .NET and Java applications, but teams must review the changes and test the resulting application. Map which components the platform patches and which remain your responsibility before relying on an automatic update.

## Further reading

- [PHP critical security release and App Service Linux](https://azure.github.io/AppService/2026/10/21/php-critical-security-release-app-service-linux.html) (Azure App Service). Patching details and responsibilities.
- [Patch now: PHP2Shell and guidance for customers](https://www.microsoft.com/en-us/msrc/blog/2026/10/patch-now-php2shell-brotli-emudhra-guidance-for-customers) (Microsoft Security Response Center). Vulnerability response guidance.
- [GitHub Copilot modernization overview](https://learn.microsoft.com/en-us/azure/developer/github-copilot-app-modernization/overview) (Microsoft Learn). Supported application modernisation workflows.
