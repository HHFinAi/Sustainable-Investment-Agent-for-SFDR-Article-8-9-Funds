# Sustainable Investment Prompt Library

A 52-prompt research library for sustainable-investment analysis, issuer/fund
assessment, stewardship and reporting workflows. It is not a certification of
current regulatory compliance or a substitute for legal/compliance review.

## Files and usage

The maintained source files are at the repository root:

- [PROMPT_LIBRARY.md](PROMPT_LIBRARY.md): source tasks and catalogue.
- [PROMPT_HEADER.md](PROMPT_HEADER.md): issuer/fund variables and conventions.
- [CATEGORIES.md](CATEGORIES.md): category navigation.
- [GITHUB_DESKTOP_SETUP.md](GITHUB_DESKTOP_SETUP.md): historical GitHub setup guide.
- [REGULATORY_REVIEW.md](REGULATORY_REVIEW.md): current source/status review contract.

Use the header plus the review contract before a selected task. The source
catalogue contains mainly prose tasks; it was not already a complete XML package.
This release generates `generated/01.xml` through `generated/52.xml`, each with
**eight blocks**: role, context, inputs, task, reasoning, output_format, constraints,
and self_evaluation. The original task text is preserved as escaped XML text.
Generated instructions explicitly treat unverified source-task legal assertions
as unverified rather than silently promoting them into current requirements.

```bash
python tools/build_prompts.py --write
python tools/build_prompts.py
python tools/check_register.py --as-of 2026-09-23
python -m unittest discover -s tests -v
```

Edit source tasks and rebuild the generated XML. The builder checks all 52 IDs,
exact block structure, non-empty blocks, escaping and generated-file consistency.
It also repairs the historical root-file path references and block-count wording.
Normal CI is read-only; a one-time branch-restricted build commits initial outputs
to the maintenance branch only.

## Regulatory status is not verified by this release

[regulatory/register.json](regulatory/register.json) is a **starter review register**,
not an exhaustive legal inventory. All seeded records are `unverified`: no effective
date, reviewer or provision has been fabricated. Add records for every material
instrument/methodology used in a specific task and verify the applicable scope,
version, provision and timing with primary sources.

`python tools/check_register.py --release-gate` deliberately fails while records
remain unverified, stale, proposed, not yet applicable or superseded. A successful
schema check in CI does **not** mean the release gate or legal review has passed.
Even `REGISTER_FIELDS_CURRENT` checks only recorded fields/dates, not legal truth.

Keep proposals, adoption, entry-into-force and application dates distinct. Do not
infer a legal threshold from a provider methodology or a fund's own policy. Source
evidence, jurisdiction and review status must accompany law-dependent outputs.

## Evaluation and limitations

Twelve deterministic tests cover XML structure/escaping/counts, documentation
paths and regulatory-register guards. They do not establish LLM extraction accuracy,
regulatory validity or investment performance. Prior unsupported quantitative
quality claims are not repeated. Marketing and legal-facing outputs require
qualified review; missing evidence produces REVIEW_REQUIRED, not certified pass/fail.

Historical prose is retained in `docs/archive/`. No repository visibility, fund
classification or external account setting is changed. License unchanged; see
[LICENSE](LICENSE).
