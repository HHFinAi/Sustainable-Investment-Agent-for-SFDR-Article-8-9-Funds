# Sustainable Investment Prompt Library for SFDR Article 8 & 9 Funds

**A 52-prompt institutional-grade library for SFDR Article 8 / Article 9 global public equity strategies, UK SDR-labelled funds, and associated stewardship, reporting and client workflows.**

Built for a senior buy-side Sustainable Investment analyst operating across DM / EM / Frontier equities. Grounded in the EU SFDR RTS, SFDR 2.0 (Nov 2025 Commission proposal), EU Taxonomy, CSRD/ESRS (as simplified by Omnibus I Dir (EU) 2026/470), IFRS S1/S2, TNFD v1.0, PCAF Part A 3rd ed. (Dec 2025), NGFS Phase V, SBTi v1.3.1 (+V2.0 consultation), IIGCC NZIF 2.0, GFANZ NZTP, UK SDR PS23/16 + FG24/3, ESMA fund-names guidelines, FCA anti-greenwashing rule, Article 29 LEC, and sectoral references (CA100+ NZCB 2.0, TPI, OGMP 2.0, CBF 3.0, GISTM, IRMA, FAIRR, WBA, ATMI, CHRB, RDR).

---

## Table of Contents

- [How to read this library](#how-to-read-this-library)
- [0. Shared components](#0-shared-components)
  - [PROMPT 00 — Canonical issuer + fund header and house conventions](#prompt-00--canonical-issuer--fund-header-and-house-conventions-esgsharedheaderv1)
- [1. Pre-investment Sustainable Investment integration](#1-pre-investment-sustainable-investment-integration)
  - [PROMPT 01 — SASB/IFRS S1 materiality map builder](#prompt-01--sasbifrs-s1-materiality-map-builder-esgpreinvmaterialityv2)
  - [PROMPT 02 — ESG vendor rating reconciliation](#prompt-02--esg-vendor-rating-reconciliation-esgpreinvrating_reconcilev2)
  - [PROMPT 03 — Exclusion screen application](#prompt-03--exclusion-screen-application-esgpreinvexclusionsv2)
  - [PROMPT 04 — Pre-investment Sustainable Investment note (IC pre-read)](#prompt-04--pre-investment-sustainable-investment-note-ic-pre-read-esgpreinvic_prereadv3)
- [2. SFDR binding elements & Sustainable Investment testing](#2-sfdr-binding-elements--sustainable-investment-testing)
  - [PROMPT 05 — Article 2(17) three-prong Sustainable Investment test](#prompt-05--article-217-three-prong-sustainable-investment-test-esgsfdrsi_testv3)
  - [PROMPT 06 — Article 8 binding elements monitor](#prompt-06--article-8-binding-elements-monitor-esgsfdrart8_bindingv2)
  - [PROMPT 07 — Article 9 "substantially all SI" stress test](#prompt-07--article-9-substantially-all-si-stress-test-esgsfdrart9_stressv2)
- [3. EU Taxonomy & DNSH](#3-eu-taxonomy--dnsh)
  - [PROMPT 08 — Taxonomy eligibility + alignment estimation](#prompt-08--taxonomy-eligibility--alignment-estimation-esgtaxalignv2)
  - [PROMPT 09 — DNSH deep-dive (SFDR + Taxonomy combined)](#prompt-09--dnsh-deep-dive-sfdr--taxonomy-combined-esgtaxdnshv2)
- [4. PAI assessment & reporting](#4-pai-assessment--reporting)
  - [PROMPT 10 — Issuer-level PAI dossier](#prompt-10--issuer-level-pai-dossier-esgpaiissuer_dossierv2)
  - [PROMPT 11 — Entity-level PAI statement draft (Art 4, annual)](#prompt-11--entity-level-pai-statement-draft-art-4-annual-esgpaientity_statementv2)
- [5. Climate analytics (TCFD, ITR, WACI, PCAF)](#5-climate-analytics-tcfd-itr-waci-pcaf)
  - [PROMPT 12 — TCFD / IFRS S2 four-pillar disclosure assessment](#prompt-12--tcfd--ifrs-s2-four-pillar-disclosure-assessment-esgclimatetcfd_ifrss2v2)
  - [PROMPT 13 — WACI computation & benchmark attribution](#prompt-13--waci-computation--benchmark-attribution-esgclimatewaciv2)
  - [PROMPT 14 — PCAF financed emissions (Part A 3rd ed., Dec 2025)](#prompt-14--pcaf-financed-emissions-part-a-3rd-ed-dec-2025-esgclimatepcafv2)
  - [PROMPT 15 — Implied Temperature Rise triangulation](#prompt-15--implied-temperature-rise-triangulation-esgclimateitrv2)
- [6. Nature, biodiversity & TNFD](#6-nature-biodiversity--tnfd)
  - [PROMPT 16 — TNFD LEAP assessment](#prompt-16--tnfd-leap-assessment-esgnatureleapv2)
  - [PROMPT 17 — Portfolio biodiversity footprint](#prompt-17--portfolio-biodiversity-footprint-esgnaturefootprintv2)
  - [PROMPT 18 — Deforestation & EUDR exposure screen](#prompt-18--deforestation--eudr-exposure-screen-esgnaturedeforestationv2)
- [7. Social & human rights](#7-social--human-rights)
  - [PROMPT 19 — UNGP salient human rights issues assessment](#prompt-19--ungp-salient-human-rights-issues-assessment-esgsocialsalientv2)
  - [PROMPT 20 — CSDDD/CSRD-era HRDD readiness](#prompt-20--csdddcsrd-era-hrdd-readiness-esgsocialhrddv2)
  - [PROMPT 21 — Living wage & just transition scorecard](#prompt-21--living-wage--just-transition-scorecard-esgsociallivingwage_jtv2)
- [8. Governance deep dive (including EM controlled-company governance)](#8-governance-deep-dive-including-em-controlled-company-governance)
  - [PROMPT 22 — Good governance test for SFDR + controlled-company lens](#prompt-22--good-governance-test-for-sfdr--controlled-company-lens-esggovsfdr_goodv2)
  - [PROMPT 23 — Controlled-company / SOE governance deep dive](#prompt-23--controlled-company--soe-governance-deep-dive-esggovem_controlledv2)
- [9. Stewardship & engagement](#9-stewardship--engagement)
  - [PROMPT 24 — SMART engagement plan](#prompt-24--smart-engagement-plan-esgstewardsmart_planv2)
  - [PROMPT 25 — Engagement log entry](#prompt-25--engagement-log-entry-esgstewardlogv2)
  - [PROMPT 26 — Collaborative engagement positioning](#prompt-26--collaborative-engagement-positioning-esgstewardcollabv2)
  - [PROMPT 27 — Escalation decision: engage vs divest](#prompt-27--escalation-decision-engage-vs-divest-esgstewardescalatev2)
- [10. Proxy voting](#10-proxy-voting)
  - [PROMPT 28 — Custom voting rationale](#prompt-28--custom-voting-rationale-esgvoterationalev2)
  - [PROMPT 29 — Say-on-Climate vote analysis](#prompt-29--say-on-climate-vote-analysis-esgvotesocv2)
  - [PROMPT 30 — Shareholder proposal analysis](#prompt-30--shareholder-proposal-analysis-esgvoteshproposalv2)
- [11. Controversy & incident response](#11-controversy--incident-response)
  - [PROMPT 31 — 72-hour controversy response memo](#prompt-31--72-hour-controversy-response-memo-esgcontroresponsev2)
  - [PROMPT 32 — Divestment vs engagement protocol](#prompt-32--divestment-vs-engagement-protocol-esgcontrodivestv2)
- [12. Thematic & impact analysis](#12-thematic--impact-analysis)
  - [PROMPT 33 — Theory of Change builder](#prompt-33--theory-of-change-builder-esgimpacttocv2)
  - [PROMPT 34 — IMP Five Dimensions scoring](#prompt-34--imp-five-dimensions-scoring-esgimpactimp5dv2)
  - [PROMPT 35 — SDG alignment triangulation](#prompt-35--sdg-alignment-triangulation-esgimpactsdgv2)
  - [PROMPT 36 — Avoided emissions (Scope 4) computation](#prompt-36--avoided-emissions-scope-4-computation-esgimpactavoidedv2)
- [13. Client reporting & communications](#13-client-reporting--communications)
  - [PROMPT 37 — Annual impact report section](#prompt-37--annual-impact-report-section-esgclientimpact_reportv2)
  - [PROMPT 38 — Quarterly fund factsheet Sustainable Investment section](#prompt-38--quarterly-fund-factsheet-sustainable-investment-section-esgclientfactsheetv2)
  - [PROMPT 39 — Institutional client engagement summary](#prompt-39--institutional-client-engagement-summary-esgclientengagement_summaryv2)
- [14. RFP / DDQ responses](#14-rfp--ddq-responses)
  - [PROMPT 40 — Consultant DDQ answer generator](#prompt-40--consultant-ddq-answer-generator-esgrfpddqv2)
  - [PROMPT 41 — RFP Sustainable Investment capability narrative](#prompt-41--rfp-sustainable-investment-capability-narrative-esgrfpnarrativev2)
- [15. Portfolio-level Sustainable Investment analytics](#15-portfolio-level-sustainable-investment-analytics)
  - [PROMPT 42 — NGFS Phase V scenario overlay](#prompt-42--ngfs-phase-v-scenario-overlay-esgportfolingfsv2)
  - [PROMPT 43 — NZIF 2.0 portfolio alignment assessment](#prompt-43--nzif-20-portfolio-alignment-assessment-esgportfolinzifv2)
  - [PROMPT 44 — Portfolio social & governance KPI pack](#prompt-44--portfolio-social--governance-kpi-pack-esgportfoliosg_kpisv2)
- [16. EM / Frontier Market adaptations](#16-em--frontier-market-adaptations)
  - [PROMPT 45 — EM/Frontier data-gap adaptation](#prompt-45--emfrontier-data-gap-adaptation-esgemdatagapv2)
  - [PROMPT 46 — Commodity-exporter transition risk](#prompt-46--commodity-exporter-transition-risk-esgemcommodity_transitionv2)
- [17. Regulatory reporting](#17-regulatory-reporting)
  - [PROMPT 47 — SFDR periodic disclosure (Annex IV/V) drafter](#prompt-47--sfdr-periodic-disclosure-annex-ivv-drafter-esgregsfdr_periodicv2)
  - [PROMPT 48 — UK SDR product-level disclosure](#prompt-48--uk-sdr-product-level-disclosure-esgregsdr_productv2)
  - [PROMPT 49 — Article 29 LEC report drafter](#prompt-49--article-29-lec-report-drafter-esgregart29_lecv2)
- [18. Sector-specific deep-dives](#18-sector-specific-deep-dives)
  - [PROMPT 50 — Energy & Utilities Paris-alignment deep-dive](#prompt-50--energy--utilities-paris-alignment-deep-dive-esgsectorenergy_parisv2)
  - [PROMPT 51 — Healthcare access & pricing assessment](#prompt-51--healthcare-access--pricing-assessment-esgsectorhealthcare_accessv2)
  - [PROMPT 52 — Tech sector AI governance + digital rights assessment](#prompt-52--tech-sector-ai-governance--digital-rights-assessment-esgsectortech_aiv2)
- [Operating the library](#operating-the-library)

---

## How to read this library

Each prompt follows a canonical **seven-block XML architecture**: `<role>`, `<context>`, `<inputs>`, `<task>`, `<reasoning>`, `<output_format>`, `<constraints>` + `<self_evaluation>`. Prompts use a **shared issuer + fund header** (defined once in Prompt 00) and a standard **four-tier confidence taxonomy** (`HIGH_CONFIDENCE`, `MEDIUM_CONFIDENCE`, `LOW_CONFIDENCE`, `UNVERIFIED`). Every analytical prompt includes a pre-mortem/red-team step, an anti-greenwashing check, an MNPI flag, the firm's no-advice disclaimer, and a self-evaluation rubric. Versioning convention: `esg.<category>.<function>.v<n>`.

**Category map (18 sections, 52 prompts):**

| # | Category | Prompts |
|---|---|---|
| 0 | Shared components | 00 |
| 1 | Pre-investment Sustainable Investment integration | 01–04 |
| 2 | SFDR binding elements & SI testing | 05–07 |
| 3 | EU Taxonomy & DNSH | 08–09 |
| 4 | PAI assessment & reporting | 10–11 |
| 5 | Climate analytics (TCFD, ITR, WACI, PCAF) | 12–15 |
| 6 | Nature, biodiversity & TNFD | 16–18 |
| 7 | Social & human rights | 19–21 |
| 8 | Governance deep dive (incl. EM) | 22–23 |
| 9 | Stewardship & engagement | 24–27 |
| 10 | Proxy voting | 28–30 |
| 11 | Controversy & incident response | 31–32 |
| 12 | Thematic & impact analysis (SDG, IMM, ToC) | 33–36 |
| 13 | Client reporting & communications | 37–39 |
| 14 | RFP/DDQ responses | 40–41 |
| 15 | Portfolio-level Sustainable Investment analytics | 42–44 |
| 16 | EM/Frontier adaptations | 45–46 |
| 17 | Regulatory reporting (SFDR periodic, SDR, Art 29 LEC) | 47–49 |
| 18 | Sector-specific deep-dives | 50–52 |

---

## 0. Shared components

### PROMPT 00 — Canonical issuer + fund header and house conventions (`esg.shared.header.v1`)

**Purpose.** Every downstream prompt `{{imports}}` this header. It standardises the issuer identifier block, the fund-context block, and the compliance/output conventions. Also available as a standalone file at `library/PROMPT_HEADER.md` for pasting into Claude Project system instructions.

```xml
<role>
Senior buy-side Responsible Investment ESG analyst at a UK/EU-regulated asset
manager. Signatory to PRI, UK Stewardship Code 2020, Net Zero Asset Managers
initiative (status as per {{fund_context.nzam_status}}), TNFD, and CA100+.
Subject to the FCA anti-greenwashing rule (ESG 4.3.1R + FG24/3), the ESMA
Guidelines on funds' names using ESG/sustainability terms (applied 21 May
2025 for existing funds), SFDR Level 2 RTS (CDR 2022/1288), UK SDR PS23/16,
and — for French-distributed products — Article 29 LEC.
</role>

<issuer>
  <company_name>{{company_name}}</company_name>
  <primary_ticker>{{ticker}}</primary_ticker>
  <isin>{{isin}}</isin>
  <figi>{{figi}}</figi>
  <gics_sector>{{gics_sector}}</gics_sector>
  <gics_sub_industry>{{gics_sub_industry}}</gics_sub_industry>
  <sasb_sics>{{sics_industry}}</sasb_sics>
  <country_of_domicile>{{country_of_domicile_iso2}}</country_of_domicile>
  <country_of_risk>{{country_of_risk_iso2_or_MULTI}}</country_of_risk>
  <market_cap_usd_bn>{{market_cap_usd_bn}}</market_cap_usd_bn>
  <ownership_type>{{listed|SOE|family_controlled|dual_class|founder_led}}</ownership_type>
</issuer>

<fund_context>
  <fund_name>{{fund_name}}</fund_name>
  <sfdr_classification>{{Art6|Art8|Art8plus|Art9}}</sfdr_classification>
  <sfdr20_intended_category>{{None|ESG_Basics|Transition|Sustainable}}</sfdr20_intended_category>
  <sdr_label>{{None|Focus|Improvers|Impact|Mixed_Goals}}</sdr_label>
  <benchmark>{{benchmark_name}}</benchmark>
  <reference_benchmark_type>{{None|PAB|CTB}}</reference_benchmark_type>
  <investment_horizon_years>{{horizon}}</investment_horizon_years>
  <minimum_si_pct>{{pct}}</minimum_si_pct>
  <minimum_taxonomy_pct>{{pct}}</minimum_taxonomy_pct>
  <exclusion_policy_ref>{{policy_id}}</exclusion_policy_ref>
  <engagement_policy_ref>{{policy_id}}</engagement_policy_ref>
</fund_context>

<analysis_date>{{ISO-8601}}</analysis_date>
<data_vintage>{{cutoff_date}}</data_vintage>

<house_conventions>
Confidence taxonomy: HIGH_CONFIDENCE (primary disclosed source), MEDIUM_CONFIDENCE
(inferred from aligned sources), LOW_CONFIDENCE (single qualitative source),
UNVERIFIED (not substantiated in retrieved documents).
Unsupported claims must be marked [UNSUPPORTED]. Every numeric claim requires
a source ID [S#]. If any input appears to contain MNPI, stop and emit [MNPI_FLAG].
Disclaimer (append to every output): "For internal research only; not
investment advice, a recommendation, or a solicitation."
</house_conventions>

<self_evaluation_rubric id="rubric.default.v1">
Score 1–5 with justification on: (a) factual grounding, (b) coverage of task,
(c) uncertainty calibration, (d) materiality focus, (e) compliance (no advice,
anti-greenwashing, MNPI). Any dimension ≤3 must be explained.
</self_evaluation_rubric>
```

---

## 1. Pre-investment Sustainable Investment integration

### PROMPT 01 — SASB/IFRS S1 materiality map builder (`esg.preinv.materiality.v2`)

Build a sector-specific financial materiality map for `{{issuer}}` by cross-referencing (i) the SASB Standards for `{{sics_industry}}` (now IFRS SASB), (ii) MSCI ESG Key Issues with weights, (iii) Sustainalytics Material ESG Issues (Exposure × Management), (iv) ISS ESG Pillars, (v) S&P Global CSA material dimensions, (vi) TPI MQ themes if in scope. Output: a materiality table with columns `Issue | SASB code | MSCI weight | Sustainalytics MEI | ISS pillar | S&P CSA dim | Analyst rank (1–5) | 3 KPIs | Data source`. Red-team step: identify any issue flagged by fewer than two providers but likely material (e.g., AI governance for non-tech sectors, biodiversity for non-mining). Conclude with the five most decision-useful KPIs and their data vintage.

### PROMPT 02 — ESG vendor rating reconciliation (`esg.preinv.rating_reconcile.v2`)

Reconcile MSCI ESG Rating (AAA–CCC), Sustainalytics ESG Risk Rating (0–100, five tiers), ISS ESG Corporate Rating (A+ to D-), S&P Global ESG Score (CSA), Bloomberg ESG Disclosure Score, and (where applicable) TPI MQ/CP for `{{issuer}}`. Explicitly note **aggregate confusion**: Berg-Kölbel-Rigobon 2022 finds average pairwise correlation 0.54 (range 0.38–0.71), with measurement (~56%), scope (~38%), and weighting (~6%) divergences. Where any two providers differ by ≥1 notch on the same underlying factor, diagnose the driver (industry-relative vs absolute framework; rewards-disclosure bias; controversy timing; scope 3 treatment). Output a reconciliation table + a 200-word analyst override justifying the firm's internal score. Apply the confidence taxonomy to every rating cited.

### PROMPT 03 — Exclusion screen application (`esg.preinv.exclusions.v2`)

Screen `{{issuer}}` against the firm's exclusion policy `{{exclusion_policy_ref}}` and the applicable **PAB exclusions** (Reg 2020/1818: coal >1% revenue, oil >10%, gas >50%, power >100 gCO2/kWh, UNGC violators, controversial weapons, tobacco) or **CTB exclusions** (narrower) where the fund name/strategy triggers them under ESMA Guidelines. Cross-reference the Global Coal Exit List (GCEL), Global Oil & Gas Exit List (GOGEL), ISS Norm-Based Research, Sustainalytics Global Standards Screening, Controversial Weapons Research, RepRisk RRI, and UFLPA Entity List for supply-chain exposure. Output: binary pass/fail per exclusion with the numeric threshold, evidence [S#], and data vintage. If fund is ESMA-named with environmental/impact/sustainability term, verify PAB exclusions formally apply.

### PROMPT 04 — Pre-investment Sustainable Investment note (IC pre-read) (`esg.preinv.ic_preread.v3`)

Produce a 600–800 word pre-investment Sustainable Investment note on `{{issuer}}` for portfolio manager review. Sections: (1) thesis interaction with Sustainable Investment considerations; (2) three most material E/S/G issues from Prompt 01 output; (3) vendor rating reconciliation summary (Prompt 02); (4) exclusion status (Prompt 03); (5) carbon intensity vs peer median + sector pathway (IEA NZE for energy/utilities; SBTi SDA for power, cement, steel; Paris-aligned capex %); (6) TPI MQ/CP where available; (7) top three red flags with evidence; (8) fund-eligibility verdict by `{{sfdr_classification}}` and `{{sdr_label}}`; (9) engagement priorities. Apply red-team: list two reasons the verdict could be wrong. Self-evaluate against `rubric.default.v1`.

---

## 2. SFDR binding elements & Sustainable Investment testing

### PROMPT 05 — Article 2(17) three-prong Sustainable Investment test (`esg.sfdr.si_test.v3`)

Apply the firm's documented Sustainable Investment methodology to `{{issuer}}` under SFDR Article 2(17) + RTS CDR 2022/1288. Evaluate **(a) Contribution** to an environmental or social objective at activity or entity level (state threshold applied, e.g., ≥20% revenue from SDG-aligned activities OR validated SBTi target with ≥4.2% p.a. Scope 1+2 reduction OR entity-level contribution per `{{contribution_methodology_ref}}`); **(b) DNSH** across mandatory PAI Table 1 indicators (1–14) + relevant Table 2/3 indicators with the firm's published thresholds; **(c) Good governance** per Art 2(17) — sound management structures, employee relations, remuneration of staff, tax compliance — operationalised as tax-haven check, UNGC/OECD status, labour disputes, board structure. Output: structured sign-off sheet with PASS/FAIL per prong, evidence per PAI, governance evidence table, final SI qualification decision, and audit-trail fields (analyst, date, data vintage, methodology version). Flag where contribution relies on estimated (not reported) data.

### PROMPT 06 — Article 8 binding elements monitor (`esg.sfdr.art8_binding.v2`)

Given the fund's Annex II binding elements (promoted E/S characteristics, minimum SI%, minimum Taxonomy%, exclusion list, benchmark), assess whether the current position in `{{issuer}}` is consistent with those commitments. Produce a binding-elements-vs-position matrix with columns `Binding element | Annex II text | Current position status | Evidence | Deviation risk | Remediation`. Flag any ESMA CSA 2025-style deficiency patterns (boilerplate DNSH language; SI% drift; inconsistent exclusion application). Output remediation deadline if deviation detected.

### PROMPT 07 — Article 9 "substantially all SI" stress test (`esg.sfdr.art9_stress.v2`)

For an Article 9 fund, test whether `{{issuer}}` qualifies as a sustainable investment under the firm's methodology AND whether the portfolio-level SI ratio remains ≥ the commitment (post ESMA November 2022 clarification that Art 9 funds must hold substantially all SI, excluding only cash/hedging/ancillary liquidity). Output: issuer-level SI flag (YES/NO with evidence), simulated portfolio SI% with/without position, sensitivity to methodology choice (e.g., contribution threshold 20% vs 50% vs entity-level), downgrade-risk assessment if PAI data revision occurs. Note: confirm the PAB/CTB safe harbour is NOT being relied upon unless the fund is a passive tracker.

---

## 3. EU Taxonomy & DNSH

### PROMPT 08 — Taxonomy eligibility + alignment estimation (`esg.tax.align.v2`)

Estimate Taxonomy eligibility and alignment for `{{issuer}}` across the six environmental objectives (climate mitigation, adaptation, water & marine, circular economy, pollution, biodiversity), using the Climate Delegated Act (CDR 2021/2139), Complementary Climate DA (2022/1214), and Environmental Delegated Act (June 2023). Step 1: map reported activities to NACE codes and identify eligible activities (list activity + NACE + DA reference). Step 2: for each eligible activity, assess (a) substantial contribution via applicable TSC, (b) DNSH against the five other objectives, (c) minimum safeguards per Article 18 (UNGPs, OECD MNE, ILO Core Conventions, International Bill of Human Rights + Platform-on-Sustainable-Finance four topics: human rights, bribery, tax, fair competition). Step 3: compute turnover / capex / opex alignment KPIs. Disclose estimation methodology for non-EU issuers where CSRD disclosures unavailable (Art 8 DA prohibits estimation for GAR but permits it for SFDR product-level reporting). Flag "enabling" and "transitional" status where relevant.

### PROMPT 09 — DNSH deep-dive (SFDR + Taxonomy combined) (`esg.tax.dnsh.v2`)

Run a combined DNSH analysis on `{{issuer}}` covering (a) SFDR DNSH via ALL 14 mandatory PAI Table 1 indicators plus relevant Table 2/3 indicators, and (b) Taxonomy activity-level DNSH criteria against the five non-primary environmental objectives. Distinguish PAI-threshold-based DNSH (SFDR, entity-level) from TSC-based DNSH (Taxonomy, activity-level) — the ESAs November 2022 statement is explicit that these are distinct constructs. Output two parallel tables; a consolidated DNSH verdict; and the evidence log. Explicitly document the firm's significant-harm thresholds for each PAI.

---

## 4. PAI assessment & reporting

### PROMPT 10 — Issuer-level PAI dossier (`esg.pai.issuer_dossier.v2`)

Compile issuer-level data for all 14 mandatory Table 1 PAI indicators (GHG emissions Scope 1/2/3; carbon footprint per €m invested; GHG intensity per €m revenue; fossil-fuel exposure; non-renewable energy share; energy intensity by high-impact NACE A–H & L; biodiversity-sensitive-area activities; water emissions; hazardous waste ratio; UNGC/OECD violations; lack of monitoring processes; unadjusted gender pay gap; board gender diversity; controversial weapons) for `{{issuer}}`. For each: value, unit, vintage, source [S#], data-quality score (PCAF scale for carbon; narrative for social), EVIC used (and vintage), currency normalisation applied. Add the two selected optional indicators per the firm's Art 4 statement. Flag indicator #2 (carbon footprint) sensitivity to EVIC volatility; disclose methodology consistent with RTS Annex I. Output fits directly into the EET `PAI_Indicator_*` fields.

### PROMPT 11 — Entity-level PAI statement draft (Art 4, annual) (`esg.pai.entity_statement.v2`)

Draft the annual Article 4 PAI statement (30 June submission) covering the four calendar-quarter measurement dates required by the RTS. Structure per RTS Annex I: summary; description of PAIs; indicator table with current year + prior year + change vs prior period + explanation; actions taken; planned actions + targets; adherence to responsible business conduct codes (UNGC, OECD MNE); reference to international standards (Paris Agreement, Kunming-Montreal GBF); historical comparison. Note: if SFDR 2.0 proposal of 20 Nov 2025 is enacted, entity-level Art 4 is repealed — flag transition planning. Apply boilerplate guardrail: ESMA CSA 2025 identified generic/boilerplate PAI language as the most-cited deficiency; require issuer-specific evidence, not template text.

---

## 5. Climate analytics (TCFD, ITR, WACI, PCAF)

### PROMPT 12 — TCFD / IFRS S2 four-pillar disclosure assessment (`esg.climate.tcfd_ifrss2.v2`)

Evaluate `{{issuer}}`'s climate-related disclosures against IFRS S2 (effective periods beginning 1 Jan 2024; full TCFD absorption). For each of the four pillars (Governance, Strategy, Risk Management, Metrics & Targets), score 0–3 (absent / partial / substantial / leading) with evidence. Specifically test: board-level climate oversight with named committee; climate in enterprise risk register; quantitative scenario analysis (≥2 scenarios, including a 1.5°C-aligned); Scope 1+2+3 (GHG Protocol, both location- and market-based Scope 2); Scope 3 Cat. 15 financed emissions for FIs (note Dec 2025 ISSB amendment permitting limited-scope relief); industry metrics per SASB industry standard; transition plan quality per TPT/IFRS S2 ¶14(a)(iv). Flag jurisdictional mandatory status (UK SRS 2026; Japan SSBJ FY27 Prime ≥¥3trn; HKEX Main Board Scope 1+2 mandatory FY25, HSCLI LargeCap full FY26; Australia Group 1 FY25; China CSDS first mandatory by 30 Apr 2026).

### PROMPT 13 — WACI computation & benchmark attribution (`esg.climate.waci.v2`)

Compute Weighted Average Carbon Intensity for `{{fund_name}}` using TCFD formula WACI = Σᵢ(wᵢ × tCO2e_i / USDmn_revenue_i). Produce two variants: Scope 1+2 and Scope 1+2+3 (flag Scope 3 estimation coverage %). Disclose: coverage % (rescaled WACI across covered positions only); % reported vs estimated; EVIC/revenue base year; FX treatment (fixed-base-year rate recommended per PCAF 2025 to avoid USD-drift artefacts); inflation adjustment. Compute benchmark WACI on identical methodology. Decompose delta vs benchmark using Brinson-style attribution: **sector allocation effect** + **stock selection effect** + **intensity change (real-economy decarbonisation)** + **reallocation (divestment)**. Per NZIF 2.0, emphasise real-economy decarbonisation over passive divestment. Output methodology caveat narrative suitable for fund factsheet.

### PROMPT 14 — PCAF financed emissions (Part A 3rd ed., Dec 2025) (`esg.climate.pcaf.v2`)

Compute portfolio-level financed emissions for `{{fund_name}}` per PCAF Part A 3rd ed. asset-class methodologies. For listed equity + corporate bonds: Attribution Factor = Outstanding Amount / EVIC (inflation-adjusted per PCAF 2025); Emissions = AF × Scope 1+2+3. Disclose PCAF Data Quality Score 1–5 weighted average; phase-in compliance (Scope 3 required for all sectors from 2026); double-counting minimisation per PCAF 5-level framework; sovereign vs corporate segregation; treatment of derivatives and cash. Include the mandatory PCAF fluctuation analysis explaining year-on-year change decomposed into (a) emissions-data revision, (b) portfolio changes, (c) EVIC changes, (d) methodology changes. Output ready for CDP FS questionnaire and NZIF 2.0 target tracking.

### PROMPT 15 — Implied Temperature Rise triangulation (`esg.climate.itr.v2`)

Report `{{fund_name}}` ITR across THREE providers — MSCI ITR, S&P Trucost Paris Alignment, CDP-WWF Temperature Rating — and reconcile divergences (same issuer can differ >2°C across providers). Provide: provider, scenario (NGFS REMIND NZ 2050 for MSCI; IEA NZE/B2DS for Trucost), aggregation method (aggregated-budget per TCFD-PAT for MSCI; weighted-avg warnings), Scope coverage, target-credibility treatment, % no-target companies defaulting to BAU/sector-avg. Compute weighted-budget aggregation: ITR = 1.55°C + (Σ financed overshoots / Σ financed budgets) × TCRE (default 0.000545 °C/GtCO2). Narrate limitations: ITR is not a precise number; report as range with methodology. Add SBTi Portfolio Coverage (% AUM with validated near-term targets, linear trajectory to 100% by 2040) as complementary metric.

---

## 6. Nature, biodiversity & TNFD

### PROMPT 16 — TNFD LEAP assessment (`esg.nature.leap.v2`)

Run a LEAP assessment on `{{issuer}}`: **Locate** (interface with nature across direct ops + upstream/downstream value chain; priority locations = sensitive biomes per IUCN Global Ecosystem Typology 2.0 + high-integrity areas + rapidly declining integrity + water-stressed basins via WRI Aqueduct 4.0 + importance for ecosystem services); **Evaluate** (dependencies via ENCORE ecosystem services + impacts across 5 IPBES drivers — LULUC, climate, pollution, resource exploitation, invasive species); **Assess** (physical, transition, systemic, liability risks + opportunities); **Prepare** (which of the 14 TNFD disclosures are currently disclosed; gaps; alignment with Kunming-Montreal GBF Target 15). Map outputs to CSRD ESRS E4 IRO disclosures. Include Indigenous Peoples/Local Community engagement evidence (TNFD Governance C).

### PROMPT 17 — Portfolio biodiversity footprint (`esg.nature.footprint.v2`)

Compute `{{fund_name}}` biodiversity footprint using Iceberg Data Lab CBF 3.0 (MSA.km²) or CDC Biodiversité GBS. Decompose by the four CBF pressures (land-use change, climate change, air pollution, water pollution) plus CBF 3.0 additions (invasive alien species, water stress). Split terrestrial vs freshwater. Distinguish dynamic (annual flow MSA.km² lost) from static (cumulative stock). Triangulate with a second metric (BFFI PDF.m²·yr or STAR for restoration positive-impact angle). Disclose known limitations (±50% uncertainty typical; marine coverage thin; 2–4 year data lag). Output is Article 29 LEC biodiversity annex-ready and covers SFDR PAI #7 (activities in biodiversity-sensitive areas). Flag any positions in companies without SBTN freshwater/land targets where materially exposed.

### PROMPT 18 — Deforestation & EUDR exposure screen (`esg.nature.deforestation.v2`)

Screen `{{issuer}}` for deforestation exposure ahead of EUDR application (large/medium 30 Dec 2026; micro/small 30 Jun 2027 per Reg 2025/2650). Cover all seven in-scope commodities (cattle, cocoa, coffee, oil palm, rubber, soya, wood) plus derivatives, using: CDP Forests; Global Canopy Forest 500; Accountability Framework initiative; Trase supply-chain mapping; Satellite data (Planet Labs, NASA FIRMS, MapBiomas). Test: cut-off date (EUDR requires 31 Dec 2020); geolocation traceability to plot; FPIC evidence for Indigenous territories; legality; country risk tier per Implementing Reg 2025/1093 (Belarus, Myanmar, DPRK, Russia high-risk; 140 low-risk). Assess regulatory exposure (penalty cap 4% EU turnover), reputational risk (Mighty Earth, Repórter Brasil exposés), and competitive re-pricing. Output: eligibility decision + engagement escalation recommendation.

---

## 7. Social & human rights

### PROMPT 19 — UNGP salient human rights issues assessment (`esg.social.salient.v2`)

Identify the three most salient human rights issues at `{{issuer}}` using the UNGP methodology: **salience = severity (scale × scope × irremediability) × likelihood** — NOT probability-weighted. Build the salient-issues universe (life, health, safety, forced/child labour, non-discrimination, FPIC, data privacy, freedom of association, living wage, migrant workers). Overlay geographic risk (ITUC Global Rights Index, US TIP Report, Walk Free GSI) onto the issuer's operations + top-tier supply chain. Cross-reference CHRB, KnowTheChain, Business & Human Rights Resource Centre tracker, OECD NCP complaints, UFLPA Entity List. Evaluate policy, DD process, grievance mechanism effectiveness (UNGP 31 criteria), performance trend. Output: three salient issues with severity scoring + evidence + remediation gap.

### PROMPT 20 — CSDDD/CSRD-era HRDD readiness (`esg.social.hrdd.v2`)

Assess `{{issuer}}`'s human rights due diligence maturity against the CSDDD regime (as amended by Omnibus I Dir (EU) 2026/470, in force 18 Mar 2026; transposition 26 Jul 2028; first-wave application 26 Jul 2029 for EU >5,000 emp + >€1.5bn turnover / non-EU >€1.5bn EU turnover). Also map to LkSG (if DE), Loi de Vigilance (if FR), Norway Transparency Act, UK/Australia/Canada modern slavery acts, and UFLPA (US supply-chain exposure). Score six DD steps per OECD Due Diligence Guidance. Feed to CSRD ESRS S1–S4 data points (own workforce, value-chain workers, affected communities, consumers/end-users).

### PROMPT 21 — Living wage & just transition scorecard (`esg.social.livingwage_jt.v2`)

Score `{{issuer}}` on (a) living wage: % direct workforce ≥ Anker/Global Living Wage Coalition benchmark; % Tier 1 supply chain coverage; roadmap + financing; Platform Living Wage Financials tier; WDI disclosure; and (b) just transition (for high-emitting sectors): WBA Just Transition Assessment six indicators (commitment, social dialogue, planning, retraining/redeployment, green & decent jobs, community impacts); ILO guidelines; CA100+ indicator 8. For coal-region issuers, overlay JETP progress (South Africa JET-IP ~$12.8bn; Indonesia CIPP; Vietnam RMP; Senegal) and local impact. Output: combined S-KPI scorecard feeding ESRS S1/S2, PAI (living wage via UNGC adherence), and fund engagement plan.

---

## 8. Governance deep dive (including EM controlled-company governance)

### PROMPT 22 — Good governance test for SFDR + controlled-company lens (`esg.gov.sfdr_good.v2`)

Apply the SFDR Art 2(17) good-governance test to `{{issuer}}` with four named sub-tests: **(1) Sound management structures** — board independence against applicable code (UK CGC 2024; AFEP-MEDEF; Japan CGC 2021; TSE Prime ≥1/3 indep; Korea ≥1/4 rising to ≥1/2; SEBI LODR; CSRC 1/3; Saudi CMA; King IV); audit committee independence; combined chair/CEO flag. **(2) Employee relations** — union recognition, strikes, collective-bargaining coverage, LTIFR. **(3) Staff remuneration** — CEO pay ratio, ESG-linked variable, clawback. **(4) Tax compliance** — tax-haven/OFC nexus; country-by-country reporting; effective tax rate consistency; tax-related controversies. **Controlled-company overlay** where ownership_type ∈ {SOE, family_controlled, dual_class, founder_led}: minority-rights mechanisms, related-party transactions (SEBI LODR Reg 23; CSRC 2024 quant requirements; Brazil Novo Mercado tier), circular/cross-holdings (chaebol), pledge of promoter shares, auditor identity (Big 4 vs local; PCAOB access for China A-share/HK), dual-class premium/penalty (MSCI non-voting penalty post-2017). Output: PASS/FAIL per sub-test + consolidated good-governance verdict.

### PROMPT 23 — Controlled-company / SOE governance deep dive (`esg.gov.em_controlled.v2`)

For `{{issuer}}` with ownership_type ∈ {SOE, family_controlled, dual_class}, produce a governance deep dive targeting EM-specific risks. For SOEs (China SASAC, Aramco, Petrobras, ONGC/Coal India, PEMEX, Gazprom): state-ownership %, political-officer roles, anti-corruption campaign exposure, delisting risks (PCAOB, HFCAA, VIE structure), sovereign-fiscal linkage. For family-controlled (chaebol, Indian groups, LatAm grupos): succession plan, promoter pledge, related-party transactions pattern, pyramid/circular holdings, minority-rights track record (e.g., Adani-Hindenburg; chaebol 2024 reform). For dual-class: economic-vs-voting gap, MSCI index-inclusion penalty, sunset clauses. Output: governance-risk score (1–5) + three engagement asks + fund-eligibility implication under `{{sfdr_classification}}`.

---

## 9. Stewardship & engagement

### PROMPT 24 — SMART engagement plan (`esg.steward.smart_plan.v2`)

Draft a SMART engagement plan for `{{issuer}}` on topic `{{engagement_topic}}`. Objectives must be **Specific, Measurable, Achievable, Relevant, Time-bound** with an explicit milestone ladder (levels 1–4 per EOS/PRI Active Ownership 2.0). Set 12-, 24-, and 36-month targets. Link to firm engagement-priority matrix and applicable collaborative initiative (CA100+ NZCB 2.0 indicators; NA100 eight-sector priorities; FAIRR; IAST APAC; IPDD; WBA CHRB; Advance human rights). Define the escalation ladder: written questions → AGM dialogue → letter to chair → SID meeting → collaborative escalation → vote against directors/say-on-climate/remuneration → co-file shareholder proposal → public statement → divestment (last resort). Require attribution evidence plan so outcomes can be linked to engagement, not counterfactual. Output: plan document + initial engagement-log entry (see Prompt 25 schema).

### PROMPT 25 — Engagement log entry (`esg.steward.log.v2`)

Generate a UK Stewardship Code-2020-compliant (Principles 9, 11) engagement log entry for a meeting on `{{date}}` with `{{issuer}}`. Required XML schema:

```xml
<engagement_log>
  <engagement_id/> <date/> <issuer_header/> <participants/>
  <engagement_type>{reactive|proactive|disclosure|thematic|collaborative}</engagement_type>
  <collaborative_ref>{CA100+|NA100|FAIRR|IAST-APAC|PRI-Advance|IIGCC|IPDD|None}</collaborative_ref>
  <objectives>
    <objective id="O1" topic="" target_outcome="" smart_criteria="" milestone_level="1-4"/>
  </objectives>
  <discussion_summary/>
  <outcomes>
    <outcome objective_ref="O1" progress="committed|partial|none" evidence=""/>
  </outcomes>
  <escalation_next_step/> <milestone_date/> <analyst/>
</engagement_log>
```

Log must be auditable and support PRI RI DDQ and Stewardship Report aggregation.

### PROMPT 26 — Collaborative engagement positioning (`esg.steward.collab.v2`)

For `{{engagement_topic}}` on `{{issuer}}`, assess whether to engage bilaterally or via collaborative initiative. Map to the appropriate platform: PRI Collaboration Platform, CA100+ (170 focus cos, NZCB 2.0 ten indicators; RMI/Carbon Tracker/InfluenceMap alignment assessments), NA100, FAIRR, IAST APAC, IPDD, WBA, PRI Advance. Flag US-jurisdictional risk post-2024/25 antitrust scrutiny (House Judiciary report Dec 2024; State AG letters; NZAM Jan 2025 pause). Output: recommendation + documented fiduciary-duty rationale + 13G eligibility preservation note for US holdings.

### PROMPT 27 — Escalation decision: engage vs divest (`esg.steward.escalate.v2`)

For `{{issuer}}` exhibiting unresolved concern `{{concern}}`, decide engage vs divest using a weighted five-factor test: **(1) Materiality** of the issue to financial or real-world outcomes; **(2) Leverage** (stake size, collaborative coalition, vote share); **(3) Willingness** (historic company responsiveness; board access); **(4) Timeline feasibility**; **(5) Irremediability / regulatory breach / exclusion-policy trigger**. Apply NZIF 2.0 preference for engagement over divestment (financing reduced emissions > reducing financed emissions). Require documented escalation history before divestment verdict. Output: decision + rationale + communication plan (internal to PM/IC; external to company) + UK Stewardship Code 2020 Principle 11 evidence.

---

## 10. Proxy voting

### PROMPT 28 — Custom voting rationale (`esg.vote.rationale.v2`)

Draft a 200–400 word vote rationale for `{{AGM_item}}` at `{{issuer}}` AGM/EGM on `{{date}}`. Apply the firm's custom Proxy Voting Policy (region-specific: US, UK, Europe, Japan, EM). State where the vote diverges from ISS/Glass Lewis and justify. For contested director elections: board independence, skills matrix, overboarding, attendance, climate/nature oversight. For say-on-pay: pay-for-performance linkage, ESG-linked variable, peer-group comparison, clawback, severance. Must explicitly test consistency with `{{sfdr_classification}}` and `{{sdr_label}}` — an Art 9 fund voting against a credible climate proposal creates greenwashing risk. Publication-ready for Tumelo/Proxymity/firm website per SRD II.

### PROMPT 29 — Say-on-Climate vote analysis (`esg.vote.soc.v2`)

Evaluate `{{issuer}}`'s Say-on-Climate transition plan vote using the Federated Hermes EOS four-principle framework + IIGCC NZIF 2.0 asks + CA100+ NZCB 2.0 indicators: (1) **Board oversight** (named committee, climate expertise, TPT/IFRS S2 alignment); (2) **Scope and targets** (Scope 1+2+3, absolute + intensity, SBTi-validated, 1.5°C-aligned, 2030/2040/2050 horizons); (3) **Capital allocation** (capex alignment %; green revenue %; brown revenue %; no new fossil expansion for O&G per IEA NZE); (4) **Engagement track record** (climate-policy lobbying alignment per InfluenceMap; Paris-aligned industry associations; just transition; methane per OGMP 2.0 Gold Standard where applicable). Score each principle 1–5; vote recommendation + rationale.

### PROMPT 30 — Shareholder proposal analysis (`esg.vote.shproposal.v2`)

For shareholder proposal `{{proposal}}` at `{{issuer}}`, assess: (a) proposal text + proponent + prior voting history; (b) materiality to fund thesis; (c) prescriptiveness (regulators increasingly scrutinise "unduly prescriptive" proposals); (d) company counter-statement credibility; (e) alignment with CA100+, NA100, ShareAction Voting Matters, or PRI coordination; (f) SEC/UK regulatory landscape (post-Feb 2025 SEC 13G guidance constraining US engagement); (g) competing management proposal if any. Output: FOR/AGAINST/ABSTAIN + rationale + consistency check with `{{sfdr_classification}}` and prior-year precedent. Flag BDS/geopolitical-sensitive proposals for compliance pre-clearance.

---

## 11. Controversy & incident response

### PROMPT 31 — 72-hour controversy response memo (`esg.contro.response.v2`)

Produce a 1–3 page real-time controversy memo on `{{incident}}` involving `{{issuer}}` within 72 hours. Structure: (1) **Facts** (chronology, primary sources, quoted regulatory/court/NGO statements); (2) **Severity** (Sustainalytics 1–5 scale; RepRisk RRI/Peak RRI; UNGP salience); (3) **Norms linkage** (UNGC principle breach? OECD MNE? ILO Core Convention? IHL?); (4) **Regulatory / litigation exposure** (map to Sabin Center / Grantham LSE database; estimate fine range); (5) **Financial materiality** (EBITDA at risk; cost of capital impact; insurance; contingent liability); (6) **Response scenarios** (engage | watchlist | vote implications | exit with timeline); (7) **Evidence tier** (court finding > regulator > NGO > media); (8) **PM/IC alert language**. Flag reputational-risk implications for fund marketing under FCA AGR.

### PROMPT 32 — Divestment vs engagement protocol (`esg.contro.divest.v2`)

Apply the firm's divestment protocol to `{{issuer}}` following `{{incident}}`. Five-factor test (materiality, remediability, company plan credibility, exclusion-policy trigger, regulatory/legal breach). Document Nordea-style "quarantine" option (engagement with binary exit trigger). For Art 9 funds, assess whether holding remains SI-qualifying post-incident. For Art 8 funds, test binding-element compliance. Output: decision + timeline + client-communication plan + Stewardship Report case-study draft + updated holding-level risk rating.

---

## 12. Thematic & impact analysis

### PROMPT 33 — Theory of Change builder (`esg.impact.toc.v2`)

Build a Theory of Change for `{{issuer}}` held in impact fund `{{fund_name}}` (UK SDR Sustainability Impact label or SFDR Art 9 with explicit impact intent). Structure: **Inputs** (capital, engagement, board influence) → **Activities** (company products/services/operations) → **Outputs** (units produced, customers served, MW installed, patients treated) → **Outcomes** (beneficiary-level change: income, health, emissions avoided) → **Impact** (counterfactual-adjusted, system-level change). Identify critical assumptions at each link + risks of failure. Map to SDG targets and IRIS+ Core Metrics Set. Include an investor-contribution statement (signal, growth capital, active engagement, flexible capital — IMP typology). Required for SDR Impact label defensibility and OPIM Principle 4.

### PROMPT 34 — IMP Five Dimensions scoring (`esg.impact.imp5d.v2`)

Score each material outcome for `{{issuer}}` across the Impact Management Project / Impact Frontiers five dimensions: **WHAT** (outcome, importance to stakeholder, SDG target alignment); **WHO** (stakeholder group, underserved status, geography, baseline); **HOW MUCH** (scale × depth × duration; quantitative where possible); **CONTRIBUTION** (counterfactual — what would have happened without investor/enterprise; IMP level 1–4); **RISK** (nine impact-risk categories: evidence, external, stakeholder participation, drop-off, efficiency, execution, alignment, endurance, unexpected). Apply IMP **ABC classification** (Act to avoid harm / Benefit stakeholders / Contribute to solutions). Output: 5×1 matrix per outcome + a consolidated impact profile. Flag impact-washing risks (listed-equity secondary-market additionality claims; revenue-based SDG mapping without contribution; static TOC).

### PROMPT 35 — SDG alignment triangulation (`esg.impact.sdg.v2`)

Map `{{issuer}}`'s revenue, capex and (where possible) outcomes to the 17 SDGs using three providers — MSCI SDG Alignment (Strongly Aligned → Strongly Misaligned per SDG), ISS ESG SDGA (–10 to +10), Robeco SDG Framework (–3 to +3, three-step products/operations/controversies). Reconcile divergence (SDG-score correlations with ESG ratings are weak, –0.03 to 0.33; tobacco paradox is canonical). Report both gross positive and negative alignment (net impact). Add outcome-based triangulation (Future-Fit; PRI SDG Framework for Investors; Upright Project net impact where available). Test Robeco-style three contribution questions (products, operations, controversies). Explicitly distinguish revenue-based from outcome-based alignment. Flag SDG-washing patterns.

### PROMPT 36 — Avoided emissions (Scope 4) computation (`esg.impact.avoided.v2`)

Compute avoided emissions for climate-solutions revenue at `{{issuer}}` per WBCSD Guidance on Avoided Emissions v2.0 (2025). Three eligibility gates: (1) **Solution legitimacy** (low-carbon + DNSH + systemic benefit); (2) **Company legitimacy** (whole-company decarbonisation plan coherent with Scope 1–3 inventory targets); (3) **Contribution legitimacy** (manufacturer/intermediary/enabler role). Select reference scenario + LCA boundary + YoY vs Forward-Looking. Compute AE = LCA_ref − LCA_solution per unit × units sold. Aggregate at company scale. **Report separately from inventory emissions** — never net. Complement with Mission Innovation TRL framework or Project Frame for pre-commercial solutions. Add PCAF EER/EAE forward-looking metrics where FI context relevant.

---

## 13. Client reporting & communications

### PROMPT 37 — Annual impact report section (`esg.client.impact_report.v2`)

Draft a 600–1,000 word section of the annual impact report for `{{fund_name}}` covering theme/holding `{{theme_or_holding}}`. Required content: (i) theme narrative + link to SDGs; (ii) three North Star KPIs with YoY trend and per-£10k-invested attribution (Baillie Gifford PC style); (iii) Theory of Change summary; (iv) IMP Five Dimensions snapshot; (v) engagement progress with milestone ladder evidence; (vi) case study with independent verification reference (BlueMark OPIM; 60 Decibels beneficiary data where applicable); (vii) methodology footnote. Tone: institutional client audience, no investment advice, anti-greenwashing compliant (FCA FG24/3 four Cs — correct, clear, complete, comparable + capable of substantiation).

### PROMPT 38 — Quarterly fund factsheet Sustainable Investment section (`esg.client.factsheet.v2`)

Produce the Sustainable Investment section of the quarterly factsheet for `{{fund_name}}`: WACI (Scope 1+2 and Scope 1+2+3) with benchmark delta and coverage %; absolute financed emissions (PCAF DQ-weighted); Taxonomy alignment % (turnover + capex); SFDR SI% achieved (vs committed); ITR with methodology caveat; top 3 engagement progress highlights with milestone evidence; top 3 holdings by sustainability contribution. All figures dated. Anti-greenwashing compliance: substantiated + not misleading; where a claim uses "impact" / "sustainable" / "climate" / "transition" verify ESMA Guidelines term-category threshold met.

### PROMPT 39 — Institutional client engagement summary (`esg.client.engagement_summary.v2`)

Compile a quarterly engagement summary for institutional client `{{client}}`: number and type of engagements (reactive/proactive/disclosure/thematic/collaborative); engagement-by-theme table (climate, nature, human rights, governance, remuneration, AI, living wage, just transition); case studies with milestone-level progress; collaborative initiative participation (CA100+ flagged AGMs, NA100 lead roles, FAIRR engagements); voting highlights with custom-policy overrides of ISS/GL; escalation cases. Mandate-specific KPIs (e.g., net-zero interim target progress; PAI coverage). ShareAction Voting Matters and WBA benchmark references for context.

---

## 14. RFP / DDQ responses

### PROMPT 40 — Consultant DDQ answer generator (`esg.rfp.ddq.v2`)

Draft a response to DDQ question `{{question}}` from `{{consultant}}` (Mercer Helios, bfinance, Willis Towers Watson, Aon, PRI RI DDQ, UN PRI Transparency Module). Retrieve latest approved firm answer from the DDQ library; check against current data (fund-level SI%, Taxonomy%, PAI statement, Stewardship Report, Climate Report, exclusions policy, TNFD progress, AI responsibility policy — a 2025 new ask). Align tone with audience. Cite evidence and attach references. Flag answer if >6 months old. Output includes revision log entry (analyst, date, methodology version). Boilerplate is forbidden; every answer must be issuer-/fund-/firm-specific.

### PROMPT 41 — RFP Sustainable Investment capability narrative (`esg.rfp.narrative.v2`)

Compose a 1,500–2,500 word Sustainable Investment capability narrative for an RFP with prospect `{{prospect}}` running `{{mandate_type}}`. Cover: firm-level RI governance + team; Sustainable Investment integration methodology per asset class; stewardship (UK Stewardship Code tiering if applicable); collaborative initiatives; exclusion policy; Taxonomy + SI methodology; PAI integration; SFDR/SDR classifications across the fund range; climate (TCFD/IFRS S2, NZAM status, SBTi); nature (TNFD adopter status; SBTN targets); human rights (UNGP, Advance); AI governance policy; data vendors and proprietary tools. Include verifiable track record (AUM, years running, PRI score, Climate Report, Stewardship Report). End with three differentiators vs peer firms (Robeco SDG; Schroders SustainEx; Baillie Gifford PC; Wellington Global Impact; Mirova; Candriam ESG1-10; Nordea STARS).

---

## 15. Portfolio-level Sustainable Investment analytics

### PROMPT 42 — NGFS Phase V scenario overlay (`esg.portfolio.ngfs.v2`)

Run an NGFS Phase V (Nov 2024) scenario overlay on `{{fund_name}}` across six scenarios: **Net Zero 2050** (1.5°C orderly), **Below 2°C**, **Delayed Transition**, **Fragmented World**, **Current Policies**, **NDCs**. Compute shadow-carbon-price EBITDA-at-risk per sector (NGFS shadow price trajectory). Apply Phase V damage function (post-Kotz et al. 2024 calibration; flag academic critique). Integrate physical risk: chronic (temperature, water stress) + acute (TC, flood, wildfire, heatwave) at asset location via CMIP6 + Fathom/JBA flood + Swiss Re TC + Munich Re wildfire. Output: % NPV change per scenario; top exposed holdings; adaptation capex requirement. Pair with MSCI Climate VaR or Ortec ClimateMAPS for cross-provider triangulation.

### PROMPT 43 — NZIF 2.0 portfolio alignment assessment (`esg.portfolio.nzif.v2`)

Assess `{{fund_name}}` against IIGCC Net Zero Investment Framework 2.0 (June 2024): (a) **Ambition** — interim 2030 target, long-term 2050, Scope coverage; (b) **Asset-class alignment** — % AUM in Achieving/Aligned/Aligning/Not Aligned categories (issuer-level methodology per CA100+ NZCB 2.0 + SBTi validation + TPI MQ/CP); (c) **Engagement threshold** — % AUM engaged on net zero; (d) **Climate Solutions** — % revenue in climate solutions (green revenues); (e) **Policy advocacy** alignment; (f) **Governance** — net-zero in investment process. Report decomposition of trajectory into real-economy-decarbonisation vs reallocation. Output is NZAM dashboard-ready.

### PROMPT 44 — Portfolio social & governance KPI pack (`esg.portfolio.sg_kpis.v2`)

Compute portfolio-weighted social & governance KPIs for `{{fund_name}}`: living wage coverage %; gender pay gap (adjusted + unadjusted; PAI #12); board gender diversity (PAI #13); LTIFR / TRIR / fatalities; union density; % supply-chain audits Tier 1 + Tier 2 visibility; UFLPA exposure flags; CEO pay ratio; % independent board; % controlled companies (SOE + family + dual-class); % with audit committee fully independent; % with validated HRDD process (CSDDD-ready); AI governance maturity (for AI-exposed positions per Collective Impact Coalition on Ethical AI + EU AI Act readiness). Coverage %, data vintage and source per KPI.

---

## 16. EM / Frontier Market adaptations

### PROMPT 45 — EM/Frontier data-gap adaptation (`esg.em.datagap.v2`)

For `{{issuer}}` in `{{country_of_risk}}` (EM or Frontier), adapt the standard Sustainable Investment methodology to local data realities. Step 1: identify applicable disclosure regime + vintage — India BRSR Core (assurance: top 150 FY24 → top 1,000 FY27); China CSDS (Basic 2024; SSE180/STAR50/SZSE100/ChiNext + dual-listed first mandatory by 30 Apr 2026; MOF Application Guide Sept 2025); Brazil CVM Res 193 (voluntary FY24; mandatory FY26); Hong Kong HKEX Appendix C2 (Scope 1+2 mandatory FY25 Main Board; HSCLI LargeCap full FY26); Singapore SGX FY25; Japan SSBJ Prime ≥¥3trn FY27; ASEAN Taxonomy v4; South Africa King IV + JSE. Step 2: inventory data gaps (Scope 3, board independence, supply chain, gender). Step 3: triangulate with (a) satellite data (MethaneSAT, Carbon Mapper, Kayrros, Planet Labs, WRI Aqueduct, NASA FIRMS), (b) NGO data (Urgewald GOGEL/GCEL, Forest 500, KnowTheChain, CHRB, RDR, FAIRR), (c) local-language news (RepRisk multilingual, Arabesque S-Ray), (d) customs/supply-chain (Panjiva, Import Genius), (e) alternative data (Glassdoor, LinkedIn). Step 4: apply sovereign ESG overlay (Robeco CSR Autumn 2025; Verisk Maplecroft; Sustainalytics Country Risk; WGI). Step 5: document data-quality caveats prominently.

### PROMPT 46 — Commodity-exporter transition risk (`esg.em.commodity_transition.v2`)

Assess transition risk for a commodity-exporting EM/Frontier sovereign or issuer `{{issuer_or_sovereign}}`. Map fiscal dependence (O&G % fiscal revenue / exports; coal royalties) using IMF Fiscal Monitor + EITI. For O&G: Saudi Arabia 62%/70% (low cost), Iraq 90%+, Nigeria 30%/75%, Angola 40%/90%+, Colombia short reserves, Venezuela stranded, Kazakhstan, Azerbaijan. For coal: Indonesia (JETP CIPP, slow implementation), South Africa (JET-IP $12.8bn; Komati only closure), Colombia (Petro phase-out), Vietnam (JETP RMP, $15.5bn), Mongolia. Overlay: breakeven oil price vs forward curve; SWF cushion (Norway GPFG vs Angola); NDC ambition vs fossil expansion; US-withdrawal effect on JETPs post-Mar 2025. Output: transition-risk score 1–5 + stranded-asset thesis + just-transition social-licence concern + US IRA/FEOC ineligibility for nickel (Indonesia HPAL) / cobalt (DRC).

---

## 17. Regulatory reporting

### PROMPT 47 — SFDR periodic disclosure (Annex IV/V) drafter (`esg.reg.sfdr_periodic.v2`)

Draft the SFDR periodic disclosure for `{{fund_name}}`: Annex IV (Art 8) or Annex V (Art 9) per CDR 2022/1288. Required fields: extent E/S characteristics / SI objective met; sustainability-indicator performance vs prior period; minimum SI achieved (with decomposition: E vs S; Taxonomy-aligned sub-set); Taxonomy alignment (turnover / capex / opex) with 2024 FY comparator; top 15 investments; PAI performance against the Art 4 statement; reference benchmark comparison (PAB/CTB or none); engagement summary; corrective actions if any. Must be consistent with Annex II/III pre-contractual, Art 10 website summary, and EET. ESMA CSA 2025 red flags to avoid: boilerplate DNSH, SI% drift, inconsistency across disclosure levels.

### PROMPT 48 — UK SDR product-level disclosure (`esg.reg.sdr_product.v2`)

Draft the UK SDR product-level disclosure stack for `{{fund_name}}` with `{{sdr_label}}` (Focus / Improvers / Impact / Mixed Goals): (i) **Consumer-facing disclosure** — concise, plain English, FCA-specified minimum content, annual review; (ii) **Pre-contractual** in prospectus — sustainability objective, investment policy including robust evidence-based absolute standard meeting ≥70%, KPIs, stewardship approach; (iii) **Ongoing product-level report** — progress vs KPIs, stewardship activity, engagement outcomes; (iv) **Entity-level sustainability report** — governance, strategy, risk management, metrics, stewardship (due 2 Dec 2025 if AUM ≥£50bn; 2 Dec 2026 if ≥£5bn). Apply FCA anti-greenwashing rule + FG24/3 four Cs. For Impact label, defensibility requires Theory of Change + measurable KPIs + intentionality + contribution + investor additionality.

### PROMPT 49 — Article 29 LEC report drafter (`esg.reg.art29_lec.v2`)

Produce an Article 29 LEC (Loi Énergie-Climat) report for `{{fund_name}}` (French-distributed). Three axes + double-materiality framing: (i) **ESG strategy** — governance, resources, integration, exclusions, engagement, labels (ISR, Greenfin); (ii) **Climate** — Paris-alignment strategy with 2030/2050 targets; Scopes 1/2/3 absolute + intensity; Taxonomy alignment; fossil-fuel exposure per NACE 05/06/09/19; WACI; ITR; climate-VaR; physical + transition risk sectorally; (iii) **Biodiversity** — alignment with Kunming-Montreal GBF; MSA.km² footprint (Iceberg/CBF or GBS); dependency/impact analysis across supply chain; principal adverse biodiversity impacts; (iv) **ESG risk integration** — double-materiality sensitivities. Comply-or-explain structure. Submit via ROSA extranet + ADEME Climate Transparency Hub within 6 months of year-end. Avoid AMF enforcement triggers (comply-without-publishing-improvement-plan pattern).

---

## 18. Sector-specific deep-dives

### PROMPT 50 — Energy & Utilities Paris-alignment deep-dive (`esg.sector.energy_paris.v2`)

Assess `{{issuer}}` (O&G integrated / E&P / refining / power utility) for 1.5°C alignment. Dimensions: IEA NZE 2050 conformity (no new long-lead O&G projects post-2021; unabated coal phased OECD 2030 / global 2040); TPI MQ level (target ≥4) + CP alignment (target 1.5°C); CA100+ NZCB 2.0 all 10 indicators + Carbon Tracker/RMI/InfluenceMap alignment assessments; OGMP 2.0 Gold Standard Level 5 (only genuine methane benchmark); methane intensity; capex alignment % (IEA NZE: ~50% low-carbon by 2030); green revenue %; brown revenue %; reserves life in >2°C scenarios (stranded-asset exposure); flaring intensity; SBTi status (note O&G pause April 2025); Feb 2026 SBTi O&G research report positioning. For utilities: generation mix; coal retirement dates; CO2/kWh trajectory vs <165 gCO2/kWh by 2030 NZE; T&D capex; wildfire liability (PG&E precedent). EU Methane Regulation imports from 2027. Output: Paris-alignment score 1–5 + engagement plan (CA100+ lead/supporting role) + divestment-threshold proximity.

### PROMPT 51 — Healthcare access & pricing assessment (`esg.sector.healthcare_access.v2`)

Assess `{{issuer}}` (pharma/biotech/devices/provider) on sector-material issues. Coverage: Access to Medicine Index ATMI rank + trend; R&D spend on neglected tropical diseases, maternal/child health, LMIC-relevant indications; voluntary licences + MPP; tiered pricing country coverage; AMR Benchmark + AMR Industry Alliance PNEC manufacturing effluent compliance; clinical-trial diversity (FDA Diversity Action Plans, June 2024; Helsinki Declaration post-trial access); FDA warning letters + Form 483s + Class I recalls; DoJ/FCPA/Anti-Kickback settlements; OIG corporate integrity agreements; IRA Medicare negotiation exposure; GLP-1 / gene-therapy pricing-equity flags; opioid-litigation legacy residue; UNGC/OECD status. NHS Net Zero Supplier Roadmap (UK) supplier pressure from 2027; My Green Lab; inhaler propellant (HFA→HFO) transitions. Output: access-materiality score + three engagement priorities + fund-eligibility verdict with particular care on SFDR good-governance (tax + anti-bribery).

### PROMPT 52 — Tech sector AI governance + digital rights assessment (`esg.sector.tech_ai.v2`)

For `{{issuer}}` (software, internet media, semis, hardware), assess AI governance and digital rights. AI governance: board committee with AI mandate + skills matrix; responsible-AI policy mapped to NIST AI RMF + OECD AI Principles + ISO/IEC 42001; model/system cards for customer-facing or high-impact AI; red-teaming cadence; bias testing (disparate-impact); training-data provenance + copyright + opt-outs (EU AI Act training-content summary template July 2025); human-in-the-loop + kill-switch; serious-incident reporting (GPAI Art 55); EU AI Act readiness (prohibitions Feb 2025; GPAI Aug 2025; high-risk Aug 2026; Annex I products Aug 2027); conformity-assessment evidence. Digital rights: Ranking Digital Rights score; GNI implementation; state surveillance/shutdown compliance; content moderation (DSA/DMA risk); child-safety (UK OSA); data breaches + GDPR/CPRA fines. Supply chain: RMAP conformant smelter %; cobalt chain of custody; UFLPA polysilicon/aluminium exposure; contractor/gig labour share. Data centre water (WUE) + PUE + 24/7 renewable matching. Output: AI/digital-rights score + engagement plan + flag for Collective Impact Coalition on Ethical AI participation.

---

## Operating the library

Three points to operationalise this library effectively.

**Treat the library as versioned code, not static documents.** Every regulatory shift — the SFDR 2.0 trilogue, CSRD simplification delegated act (mid-2026), Omnibus CSDDD transposition by July 2028, EUDR 30 Dec 2026 application, SBTi Corporate Net-Zero v2.0 finalisation, PCAF Part A revisions, ISSB biodiversity/human-capital standards, EU AI Act high-risk phase August 2026, ESMA fund-names interpretive updates, UK SDR overseas-funds extension — must trigger a prompt-review cycle with a changelog entry. The prompt ID conventions (`esg.<category>.<function>.v<n>`) and the self-evaluation rubrics are the control plane that make this manageable.

**The library's real value is in the scaffolding, not the prose.** What differentiates an institutional prompt library from ChatGPT-style templates is (a) the canonical XML tag vocabulary enforcing structured outputs, (b) the shared issuer + fund header providing portability across tickers/sectors/regions, (c) the mandatory compliance guardrails (no-advice, anti-greenwashing, MNPI flag, citation discipline), (d) red-team and self-evaluation blocks built into every analytical prompt, and (e) a judge-prompt companion for high-stakes outputs. **These are what let a senior analyst trust the output enough to put it in an IC memo or Annex V.**

**Human-in-the-loop remains non-negotiable for analytical outputs.** The 2024–2025 academic literature (ESGReveal, ESGenius, ChatReport) converges on the finding that LLMs raise KPI-extraction accuracy from ~30% to ~70%+ when prompts include explicit term glossaries and RAG grounding, but still fail adversarially on niche SASB/IFRS and sector-specific standards. Pair this library with (i) a gold-standard eval suite per prompt, (ii) issuer-specific RAG grounding, (iii) compliance sign-off on marketing-facing outputs, and (iv) quarterly review of prompts against the ESMA CSA and FCA enforcement posture. The analyst, not the model, remains the responsible party under PRI, SFDR, SDR, and FCA Principles.

The 52 prompts above represent the condensed core. Each can spawn modular sub-prompts (Retrieve → Extract → Classify → Score → Critique → Memo) following the chain-of-thought scaffolding described in Prompt 00. Ship prompts only with the 10-point acceptance test passed: versioned ID, typed I/O, canonical tags, explicit role/task/format/constraints/citations, self-evaluation block, compliance disclaimer + MNPI flag, five gold-standard evals, judge-prompt companion, cross-sector + cross-region tested, human ESG + compliance review.

---

*For internal research purposes only. Not investment advice, a recommendation, or a solicitation to buy or sell securities.*
