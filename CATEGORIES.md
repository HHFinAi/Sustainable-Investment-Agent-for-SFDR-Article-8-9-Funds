# Prompt Categories Quick Reference

One-line summaries for all 52 prompts grouped by category, for fast lookup when you don't need the full XML spec. Prompt IDs link to the full prompt in `library/PROMPT_LIBRARY.md`.

---

## 0. Shared components

| ID | Title | One-line use |
|---|---|---|
| `esg.shared.header.v1` | Canonical issuer + fund header | Imported by every downstream prompt; standardises issuer + fund context + house conventions |

## 1. Pre-investment Sustainable Investment integration

| ID | Title | One-line use |
|---|---|---|
| `esg.preinv.materiality.v2` | SASB/IFRS S1 materiality map | Cross-reference SASB, MSCI, Sustainalytics, ISS, S&P CSA to produce decision-useful KPI set |
| `esg.preinv.rating_reconcile.v2` | ESG vendor rating reconciliation | Reconcile MSCI/Sustainalytics/ISS/S&P ratings explicitly diagnosing aggregate confusion |
| `esg.preinv.exclusions.v2` | Exclusion screen application | Apply firm exclusions + PAB/CTB exclusions per ESMA Guidelines with evidence audit trail |
| `esg.preinv.ic_preread.v3` | Pre-investment SI note (IC pre-read) | 600–800 word IC pre-read with fund-eligibility verdict + engagement priorities |

## 2. SFDR binding elements & Sustainable Investment testing

| ID | Title | One-line use |
|---|---|---|
| `esg.sfdr.si_test.v3` | Article 2(17) three-prong SI test | Structured PASS/FAIL sign-off on Contribution / DNSH / Good Governance with audit-trail fields |
| `esg.sfdr.art8_binding.v2` | Article 8 binding elements monitor | Binding-element-vs-position matrix flagging ESMA CSA 2025 deficiency patterns |
| `esg.sfdr.art9_stress.v2` | Article 9 "substantially all SI" stress test | Portfolio-level SI% simulation with sensitivity to methodology choice |

## 3. EU Taxonomy & DNSH

| ID | Title | One-line use |
|---|---|---|
| `esg.tax.align.v2` | Taxonomy eligibility + alignment | Six-objective alignment estimation with TSC + minimum safeguards check |
| `esg.tax.dnsh.v2` | DNSH deep-dive (SFDR + Taxonomy) | Parallel PAI-based + TSC-based DNSH analysis with consolidated verdict |

## 4. PAI assessment & reporting

| ID | Title | One-line use |
|---|---|---|
| `esg.pai.issuer_dossier.v2` | Issuer-level PAI dossier | All 14 mandatory PAI indicators + two optional, with PCAF DQ scoring |
| `esg.pai.entity_statement.v2` | Entity-level PAI statement (Art 4) | Annual Article 4 statement per RTS Annex I with ESMA CSA boilerplate guardrails |

## 5. Climate analytics (TCFD, ITR, WACI, PCAF)

| ID | Title | One-line use |
|---|---|---|
| `esg.climate.tcfd_ifrss2.v2` | TCFD / IFRS S2 four-pillar assessment | 0–3 scoring across Governance / Strategy / Risk Management / Metrics + jurisdictional mandatory status |
| `esg.climate.waci.v2` | WACI computation + benchmark attribution | Brinson-style attribution decomposing real-economy decarbonisation vs reallocation |
| `esg.climate.pcaf.v2` | PCAF financed emissions (Part A 3rd ed.) | Attribution factor + DQ score + fluctuation analysis |
| `esg.climate.itr.v2` | Implied Temperature Rise triangulation | Three-provider ITR reconciliation with weighted-budget aggregation |

## 6. Nature, biodiversity & TNFD

| ID | Title | One-line use |
|---|---|---|
| `esg.nature.leap.v2` | TNFD LEAP assessment | Locate-Evaluate-Assess-Prepare + IPBES 5 drivers + ESRS E4 mapping |
| `esg.nature.footprint.v2` | Portfolio biodiversity footprint | CBF 3.0 MSA.km² decomposition by pressure + uncertainty caveats |
| `esg.nature.deforestation.v2` | Deforestation & EUDR exposure screen | Seven-commodity EUDR exposure + country risk tier + engagement escalation |

## 7. Social & human rights

| ID | Title | One-line use |
|---|---|---|
| `esg.social.salient.v2` | UNGP salient human rights issues | Severity-first (not probability-weighted) identification of top three salient issues |
| `esg.social.hrdd.v2` | CSDDD/CSRD-era HRDD readiness | Six OECD DD steps mapped to CSRD ESRS S1–S4 |
| `esg.social.livingwage_jt.v2` | Living wage + just transition scorecard | WBA Just Transition six indicators + JETP progress overlay |

## 8. Governance deep dive

| ID | Title | One-line use |
|---|---|---|
| `esg.gov.sfdr_good.v2` | SFDR good governance + controlled-company lens | Four-sub-test PASS/FAIL with EM code overlay |
| `esg.gov.em_controlled.v2` | Controlled-company / SOE deep dive | SOE / family-controlled / dual-class risk scoring with engagement asks |

## 9. Stewardship & engagement

| ID | Title | One-line use |
|---|---|---|
| `esg.steward.smart_plan.v2` | SMART engagement plan | EOS/PRI milestone ladder levels 1–4 + 12/24/36m targets + escalation ladder |
| `esg.steward.log.v2` | Engagement log entry | UK Stewardship Code 2020 Principle 9/11 XML schema |
| `esg.steward.collab.v2` | Collaborative engagement positioning | Bilateral vs collaborative decision with US antitrust / 13G preservation |
| `esg.steward.escalate.v2` | Escalation decision: engage vs divest | Five-factor weighted test with NZIF 2.0 engagement preference |

## 10. Proxy voting

| ID | Title | One-line use |
|---|---|---|
| `esg.vote.rationale.v2` | Custom voting rationale | 200–400 word rationale with ISS/GL divergence + SFDR/SDR consistency test |
| `esg.vote.soc.v2` | Say-on-Climate vote analysis | EOS four-principle framework + NZIF 2.0 + CA100+ NZCB 2.0 scoring |
| `esg.vote.shproposal.v2` | Shareholder proposal analysis | FOR/AGAINST/ABSTAIN with prescriptiveness + US regulatory overlay |

## 11. Controversy & incident response

| ID | Title | One-line use |
|---|---|---|
| `esg.contro.response.v2` | 72-hour controversy response memo | 1–3 page Facts/Severity/Norms/Legal/Financial/Response memo with evidence tiering |
| `esg.contro.divest.v2` | Divestment vs engagement protocol | Five-factor test + Nordea-style quarantine option + Art 8/9 SI consistency check |

## 12. Thematic & impact analysis

| ID | Title | One-line use |
|---|---|---|
| `esg.impact.toc.v2` | Theory of Change builder | Inputs→Activities→Outputs→Outcomes→Impact with investor-contribution statement |
| `esg.impact.imp5d.v2` | IMP Five Dimensions scoring | WHAT/WHO/HOW MUCH/CONTRIBUTION/RISK + ABC classification |
| `esg.impact.sdg.v2` | SDG alignment triangulation | Three-provider reconciliation with outcome-based overlay + SDG-washing flags |
| `esg.impact.avoided.v2` | Avoided emissions (Scope 4) | WBCSD v2.0 three eligibility gates + separate-from-inventory reporting |

## 13. Client reporting & communications

| ID | Title | One-line use |
|---|---|---|
| `esg.client.impact_report.v2` | Annual impact report section | 600–1,000 word section with North Star KPIs + ToC + IMP 5D + case study |
| `esg.client.factsheet.v2` | Quarterly factsheet SI section | WACI + PCAF + Taxonomy + SI% + ITR + engagement highlights with FG24/3 compliance |
| `esg.client.engagement_summary.v2` | Institutional client engagement summary | Quarterly engagements by theme + collaborative + voting highlights |

## 14. RFP / DDQ responses

| ID | Title | One-line use |
|---|---|---|
| `esg.rfp.ddq.v2` | Consultant DDQ answer generator | Audience-adapted responses to Mercer / bfinance / WTW / Aon / PRI DDQs |
| `esg.rfp.narrative.v2` | RFP SI capability narrative | 1,500–2,500 word narrative with firm-level RI governance + differentiators |

## 15. Portfolio-level Sustainable Investment analytics

| ID | Title | One-line use |
|---|---|---|
| `esg.portfolio.ngfs.v2` | NGFS Phase V scenario overlay | Six-scenario NPV/EBITDA-at-risk with physical + transition risk integration |
| `esg.portfolio.nzif.v2` | NZIF 2.0 portfolio alignment | Ambition + Asset-class alignment + Engagement threshold + Climate Solutions % |
| `esg.portfolio.sg_kpis.v2` | Portfolio social & governance KPIs | Living wage, pay gap, board diversity, LTIFR, HRDD readiness, AI governance maturity |

## 16. EM / Frontier Market adaptations

| ID | Title | One-line use |
|---|---|---|
| `esg.em.datagap.v2` | EM/Frontier data-gap adaptation | Local disclosure regime + satellite/NGO/customs triangulation + sovereign overlay |
| `esg.em.commodity_transition.v2` | Commodity-exporter transition risk | Fiscal dependence + JETP progress + SWF cushion + IRA/FEOC eligibility |

## 17. Regulatory reporting

| ID | Title | One-line use |
|---|---|---|
| `esg.reg.sfdr_periodic.v2` | SFDR Annex IV/V periodic drafter | Full periodic disclosure with SI decomposition + PAI comparison + ESMA CSA guardrails |
| `esg.reg.sdr_product.v2` | UK SDR product-level disclosure | Full four-layer stack: consumer-facing + pre-contractual + ongoing + entity-level |
| `esg.reg.art29_lec.v2` | Article 29 LEC report drafter | Three-axis + double-materiality French-regulator-ready report |

## 18. Sector-specific deep-dives

| ID | Title | One-line use |
|---|---|---|
| `esg.sector.energy_paris.v2` | Energy & Utilities Paris-alignment | IEA NZE + TPI + CA100+ + OGMP 2.0 + capex alignment scoring |
| `esg.sector.healthcare_access.v2` | Healthcare access & pricing | ATMI + AMR + clinical-trial diversity + FDA enforcement + IRA exposure |
| `esg.sector.tech_ai.v2` | Tech AI governance + digital rights | NIST AI RMF + EU AI Act readiness + RDR + content moderation + supply chain |
