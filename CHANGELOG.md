# Changelog

All notable changes to this library will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] — 2026-04-24

### Added

Initial public release.

- **52 institutional-grade prompts** across 18 categories covering the full
  SFDR Article 8 & 9 analyst workflow.
- **Canonical seven-block XML architecture** applied uniformly across all
  prompts: `<role>`, `<context>`, `<inputs>`, `<task>`, `<reasoning>`,
  `<output_format>`, `<constraints>`, `<self_evaluation>`.
- **Shared issuer + fund header** (Prompt 00) imported by all downstream
  prompts — standardises issuer identifiers, fund context, and house
  conventions.
- **Four-tier confidence taxonomy**: `HIGH_CONFIDENCE`, `MEDIUM_CONFIDENCE`,
  `LOW_CONFIDENCE`, `UNVERIFIED`.
- **Compliance guardrails** built into every analytical prompt: anti-
  greenwashing check (FCA AGR + FG24/3 four Cs), MNPI flag, no-advice
  disclaimer, red-team step, and self-evaluation rubric.
- **Versioning convention** `esg.<category>.<function>.v<n>` for prompt IDs.
- **GitHub-rendered Mermaid workflow diagram** in README.
- **Supporting documentation**: `docs/GITHUB_DESKTOP_SETUP.md`,
  `docs/CATEGORIES.md`, `CONTRIBUTING.md`, `LICENSE` (CC BY 4.0),
  `.gitignore`, `.gitattributes`.

### Categories at launch

- 0 — Shared components (1 prompt)
- 1 — Pre-investment ESG integration (4 prompts)
- 2 — SFDR binding elements & SI testing (3 prompts)
- 3 — EU Taxonomy & DNSH (2 prompts)
- 4 — PAI assessment & reporting (2 prompts)
- 5 — Climate analytics (TCFD, ITR, WACI, PCAF) (4 prompts)
- 6 — Nature, biodiversity & TNFD (3 prompts)
- 7 — Social & human rights (3 prompts)
- 8 — Governance deep dive (2 prompts)
- 9 — Stewardship & engagement (4 prompts)
- 10 — Proxy voting (3 prompts)
- 11 — Controversy & incident response (2 prompts)
- 12 — Thematic & impact analysis (4 prompts)
- 13 — Client reporting & communications (3 prompts)
- 14 — RFP / DDQ responses (2 prompts)
- 15 — Portfolio-level ESG analytics (3 prompts)
- 16 — EM / Frontier market adaptations (2 prompts)
- 17 — Regulatory reporting (3 prompts)
- 18 — Sector-specific deep-dives (3 prompts)

### Regulatory grounding at launch

Library cites and operationalises: SFDR (Reg 2019/2088) + Level 2 RTS
(CDR 2022/1288); SFDR 2.0 Commission proposal (20 Nov 2025); EU Taxonomy
(Reg 2020/852) + Climate DA + Complementary Climate DA + Environmental DA;
CSRD + ESRS as simplified by Omnibus I Dir (EU) 2026/470; CSDDD; EUDR
(Reg 2023/1115 + 2025/2650 + Implementing Reg 2025/1093); EU Methane
Regulation; EU AI Act phasing; PAB/CTB Climate Benchmark Regulation
2020/1818; ESMA Guidelines on funds' names using ESG/sustainability terms
(applied 21 May 2025); UK SDR PS23/16 + FG24/3; FCA anti-greenwashing rule
(ESG 4.3.1R); UK Stewardship Code 2020; UK SRS 2026; IFRS S1/S2; TNFD v1.0;
TPT Disclosure Framework; PCAF Part A 3rd ed. (Dec 2025); IIGCC NZIF 2.0;
SBTi Corporate Net-Zero Standard v1.3.1; NZAM; NGFS Phase V (Nov 2024);
CA100+ NZCB 2.0; TPI MQ + CP; OGMP 2.0; Iceberg CBF 3.0; SBTN; ENCORE;
WBCSD Guidance on Avoided Emissions v2.0 (2025); UNGPs; OECD DDG; CHRB;
KnowTheChain; ATMI; AMR Benchmark; WBA Just Transition; IMP Five
Dimensions; IRIS+; OPIM; Article 29 LEC.

---

## Upcoming (unreleased)

Tracked on the regulatory watch list (see README). Candidates for v1.1+:

- SFDR 2.0 final text prompt refresh (SI definition, category labels)
- CSRD Omnibus I simplification impact prompt
- EUDR operational DD template (post 30 Dec 2026 application)
- SBTi V2.0 prompt alignment upgrade
- EU AI Act high-risk phase sector prompt upgrade
- UK SDR overseas-funds prompt extension
- Additional sector deep-dives beyond energy / healthcare / tech
- Gold-standard eval pairs per prompt

---

[1.0.0]: https://github.com/<handle>/sustainable-investment-sfdr-prompts/releases/tag/v1.0.0
