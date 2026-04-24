# Contributing

Thank you for considering a contribution. This library is actively maintained to stay aligned with a fast-moving regulatory landscape, and input from other buy-side Sustainable Investment practitioners, lawyers, academics, and data vendors is very welcome.

## Ways to contribute

**Regulatory updates.** As new Regulatory Technical Standards, Delegated Acts, Implementing Regulations, ESMA Q&As, FCA handbook updates, or ISSB standards publish, the existing prompts need to be updated. Open an issue with the regulation citation and the affected prompt IDs.

**New sector deep-dives.** The library currently includes deep-dive prompts for energy & utilities (Prompt 50), healthcare access (Prompt 51), and tech AI governance (Prompt 52). Pull requests for additional sectors — financials with PCAF, materials with GISTM and IRMA, consumer with living wage, real estate with CRREM, industrials with just transition — are welcome if they follow the canonical architecture.

**Gold-standard eval pairs.** Each prompt would benefit from 3–5 paired (input, expected output) examples for regression testing. If you have examples drawn from public filings you can share, please submit as a pull request under `evals/<prompt_id>/`.

**Translations and regional adaptations.** The consumer-facing disclosure prompts (Prompts 37–39, 48) are written for English-language UK/EU audiences. Translations into German (for PIB equivalents), French (for Article 29 LEC), and other European languages are welcome as additional files.

**Bug reports and clarifications.** If a prompt produces a misleading, stale, or regulation-incorrect output, open an issue with the prompt ID, the full input you used, the output received, and the expected output.

## Prompt schema template

All contributions must follow the canonical seven-block XML architecture. Use this template when writing a new prompt:

````markdown
### PROMPT <NN> — <Title> (`esg.<category>.<function>.v<n>`)

<One-sentence purpose statement.>

```xml
<role>
{{import esg.shared.header.v1 role}}
Additional role context specific to this prompt.
</role>

<context>
Why this prompt exists. Which regulation(s), methodology documents, or
NGO benchmarks anchor it. Relevant deadlines or vintage considerations.
</context>

<inputs>
Required inputs from the issuer + fund header (Prompt 00) plus any
prompt-specific inputs. State each input's type and expected vintage.
</inputs>

<task>
Numbered task steps. Be explicit about sequencing and intermediate
outputs. Include red-team / pre-mortem step.
</task>

<reasoning>
The analytical framework to apply. Cite primary standards (e.g.,
"per RTS Annex I, Table 1, PAI indicator #2"). Include methodology
caveats.
</reasoning>

<output_format>
Exact format for the deliverable. Specify tables, headers, word count,
and required evidence columns. Include the confidence taxonomy
requirement and source IDs [S#].
</output_format>

<constraints>
- Apply anti-greenwashing check (FCA AGR + FG24/3 four Cs).
- MNPI flag: stop if input contains MNPI.
- No-advice disclaimer at end of output.
- Any other prompt-specific constraints.
</constraints>

<self_evaluation>
Apply rubric.default.v1 (or a custom rubric if appropriate). Score 1-5
on grounding, coverage, calibration, materiality, compliance.
</self_evaluation>
```
````

## Standards

Every contribution must:

- **Use the canonical architecture.** All seven XML blocks, in order. No exceptions.
- **Cite authoritative sources.** Primary regulations, NGO benchmark methodology documents, peer-reviewed research, or asset manager published methodologies. Avoid consulting-firm summaries, press releases, and secondary commentary.
- **Mark confidence.** Use the four-tier confidence taxonomy (`HIGH_CONFIDENCE` / `MEDIUM_CONFIDENCE` / `LOW_CONFIDENCE` / `UNVERIFIED`) for any numeric or evaluative claim.
- **Respect MNPI.** No prompt should ask a user to input material non-public information. Include the MNPI flag in constraints.
- **Remain jurisdiction-aware.** SFDR applies to EU-domiciled and EU-marketed products; SDR to UK-domiciled retail funds; Article 29 LEC to French-distributed products. State the applicable regime explicitly.
- **Avoid investment advice.** Every output must end with the no-advice disclaimer. Prompts that recommend buy/sell/hold without analyst signoff will be rejected.
- **Follow the versioning convention.** `esg.<category>.<function>.v<n>`. Increment `v<n>` when changing logic; leave unchanged when fixing typos.

## Pull request process

1. Fork the repository and create a feature branch named `prompt/<short-description>` or `fix/<short-description>`.
2. Make your changes. Keep commits focused and use descriptive commit messages.
3. Update `CHANGELOG.md` under `Upcoming (unreleased)` with a one-line entry.
4. Update the prompt count and category table in `README.md` and `library/PROMPT_LIBRARY.md` if adding prompts.
5. Open a pull request with a clear description of what changes and why. Link to the regulation or methodology document if the change is regulatory-driven.
6. The maintainer will review within 2 weeks.

## Code of conduct

Be professional. This is a practitioner community. Technical disagreement is welcome and expected — personal attacks, political grandstanding about ESG more broadly, and vendor pitches are not.

## Licensing of contributions

By submitting a pull request, you agree that your contribution is licensed under the same Creative Commons Attribution 4.0 International (CC BY 4.0) licence as the rest of the library. You retain authorship credit.
