"""Generate eight-block XML wrappers without inventing regulatory verification."""
import argparse
from pathlib import Path
import re
import xml.etree.ElementTree as ET

TAGS = ('role','context','inputs','task','reasoning','output_format','constraints','self_evaluation')
HEAD = re.compile(r'^### PROMPT (\d{2})[^\n]*$', re.M)


def extract(text, expected=52):
    matches = list(HEAD.finditer(text))
    ids = [int(m.group(1)) for m in matches]
    if ids != list(range(expected+1)):
        raise ValueError(f'Expected ordered, unique prompt IDs 00 through {expected:02}')
    result = {}
    for i, match in enumerate(matches):
        ident = int(match.group(1))
        if ident == 0: continue
        end = matches[i+1].start() if i+1 < len(matches) else len(text)
        body = text[match.end():end]
        body = re.split(r'^## ', body, maxsplit=1, flags=re.M)[0].strip()
        body = re.sub(r'\n---\s*$', '', body).strip()
        if not body: raise ValueError(f'Empty prompt {ident}')
        result[f'{ident:02}'] = body
    return result


def render(ident, task):
    if not re.fullmatch(r'\d{2}', ident) or not task.strip():
        raise ValueError('Invalid prompt ID or empty task')
    blocks = {
        'role':'Support sustainable-investment research. Do not claim regulatory, legal or compliance sign-off.',
        'context':'Populate PROMPT_HEADER.md with actual issuer and fund information. Every legacy legal date, threshold and methodology claim in the task is UNVERIFIED until checked against a current authoritative source for the relevant jurisdiction and period.',
        'inputs':'Require issuer/fund identifiers, governing fund documents, source documents, analysis cutoff and applicable regulatory-register records. Mark missing inputs explicitly; never substitute zero or a guessed rule.',
        'task':task,
        'reasoning':'Provide an auditable summary of evidence, assumptions, conflicts, applicable scope, alternative interpretations and disconfirming facts. Do not treat a proposal as an operative requirement.',
        'output_format':'Use the task-specific deliverable and append source IDs, dates, units, methodology versions, jurisdiction, missing inputs and review status. Unverified law-dependent conclusions must be REVIEW_REQUIRED, not a certified pass/fail.',
        'constraints':'Apply REGULATORY_REVIEW.md before relying on hard-coded source-task claims. Keep proposal, adoption, entry-into-force and application dates distinct. Do not fabricate evidence or affiliation, infer compliance from model confidence, or publish confidential inputs. Marketing/legal-facing outputs require qualified human review.',
        'self_evaluation':'Score grounding, numerical correctness, source support, completeness and uncertainty handling with brief reasons. Scores are subjective and uncalibrated. A material unsupported legal or numerical claim is a critical failure regardless of average score.'
    }
    root = ET.Element('prompt', {'id':ident,'legal_review':'NOT_COMPLETED'})
    for tag in TAGS: ET.SubElement(root,tag).text = blocks[tag]
    ET.indent(root, space='  ')
    output = ET.tostring(root,encoding='unicode') + '\n'
    validate(output)
    return output


def validate(xml):
    root = ET.fromstring(xml)
    if root.tag != 'prompt' or tuple(c.tag for c in root) != TAGS:
        raise ValueError('Expected exactly eight ordered prompt blocks')
    if any(not (c.text or '').strip() for c in root):
        raise ValueError('Empty XML block')


def normalize_docs(text):
    text = text.replace('Each prompt follows a canonical **seven-block XML architecture**:', 'Generated XML prompts use an **eight-block XML architecture**:')
    for old,new in [('library/PROMPT_HEADER.md','PROMPT_HEADER.md'),('library/PROMPT_LIBRARY.md','PROMPT_LIBRARY.md'),('docs/CATEGORIES.md','CATEGORIES.md'),('docs/GITHUB_DESKTOP_SETUP.md','GITHUB_DESKTOP_SETUP.md')]:
        text = text.replace(old,new)
    return text


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--write',action='store_true');args=p.parse_args()
    root=Path(__file__).resolve().parents[1];source=root/'PROMPT_LIBRARY.md'
    old=source.read_text(encoding='utf-8');text=normalize_docs(old)
    if old != text:
        if not args.write: raise ValueError('Source documentation paths/architecture need normalization')
        source.write_text(text,encoding='utf-8')
    prompts=extract(text)
    directory=root/'generated'
    if args.write: directory.mkdir(exist_ok=True)
    for ident,body in prompts.items():
        output=render(ident,body);path=directory/f'{ident}.xml'
        if args.write: path.write_text(output,encoding='utf-8')
        elif not path.exists() or path.read_text(encoding='utf-8') != output: raise ValueError(f'Stale XML {ident}; run tools/build_prompts.py --write')
    if {p.name for p in directory.glob('*.xml')} != {f'{i}.xml' for i in prompts}:
        raise ValueError('Unexpected/missing generated prompt files')
    print(f'Validated {len(prompts)} eight-block XML prompts; legal verification is NOT implied')


if __name__=='__main__': main()
