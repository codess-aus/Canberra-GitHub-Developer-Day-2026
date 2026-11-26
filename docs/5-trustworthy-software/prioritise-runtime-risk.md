---
title: "Prioritise by runtime risk"
chapter: 5
hero: "5.18 Prioritise.png"
hero_alt: "Diagram connecting GitHub Code Security alerts to Microsoft Defender for Cloud workloads, with runtime factors including internet exposure, sensitive data, critical resources and lateral movement."
thumb: "thumbs/5-18-prioritise.webp"
summary: "Use deployed workload context to focus remediation on real exposure."
---

??? note "Text version of this slide"

    Repository alerts are connected to deployed workloads. Runtime factors include internet exposure, sensitive data, critical resources and lateral movement.

## Connect code to what runs

Two alerts with the same severity can have different consequences. A vulnerable dependency in an internet-facing service handling sensitive data may need attention sooner than the same dependency in an isolated test system. Defender for Cloud's GitHub Advanced Security integration maps repositories to workloads and adds runtime risk context to GitHub alerts.

Use that context alongside severity, reachability and business knowledge, not as the only decision rule. Mapping depends on supported integrations and coverage; an alert without runtime context is not automatically harmless. Plan connectors and licensing together, including any separate connector needed for MDASH.

## Further reading

- [GitHub Advanced Security integration with Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/github-advanced-security-overview) (Microsoft Learn). Code-to-runtime mapping and risk factors.
- [Deploy the integration](https://learn.microsoft.com/en-us/azure/defender-for-cloud/github-advanced-security-deploy) (Microsoft Learn). Prerequisites and configuration.
- [Create a GitHub connector](https://learn.microsoft.com/en-us/security-exposure-management/create-github-connector) (Microsoft Learn). Connector planning for Security Exposure Management.
