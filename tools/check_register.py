"""Validate register structure/freshness; never certify legal compliance."""
import argparse
from datetime import date
import json
from pathlib import Path
from urllib.parse import urlparse

STATES={'unverified','proposal','adopted_not_applicable','applicable','superseded'}


def assess(records, as_of, max_age_days=90):
    cutoff=date.fromisoformat(as_of)
    if not isinstance(max_age_days,int) or max_age_days < 1: raise ValueError('Review age must be positive')
    if not isinstance(records,list) or not records: raise ValueError('Register must contain records')
    ids=set();pending=[]
    for r in records:
        required={'id','jurisdiction','instrument','source_url','status','effective_date','last_reviewed','reviewed_by','provision','prompt_ids'}
        if not isinstance(r,dict) or set(r)!=required: raise ValueError('Register schema mismatch')
        if not isinstance(r['id'],str) or not r['id'] or r['id'] in ids: raise ValueError('Duplicate/empty ID')
        ids.add(r['id'])
        if r['status'] not in STATES: raise ValueError('Unknown regulatory status')
        if not r['jurisdiction'] or not r['instrument']: raise ValueError('Scope and instrument required')
        if urlparse(r['source_url']).scheme != 'https' or not urlparse(r['source_url']).netloc: raise ValueError('HTTPS authority/source locator required')
        if not isinstance(r['prompt_ids'],list) or not r['prompt_ids'] or any(not isinstance(i,str) or len(i)!=2 or not i.isdigit() or not 1<=int(i)<=52 for i in r['prompt_ids']): raise ValueError('Invalid prompt mapping')
        reviewed=date.fromisoformat(r['last_reviewed']) if r['last_reviewed'] else None
        effective=date.fromisoformat(r['effective_date']) if r['effective_date'] else None
        if reviewed and reviewed>cutoff: raise ValueError('Review date after analysis cutoff')
        if r['status']!='unverified' and (not reviewed or not r['reviewed_by'] or not r['provision']): raise ValueError('A reviewed status needs a reviewer, date and exact provision')
        if r['status']=='applicable' and (not effective or effective>cutoff): raise ValueError('Applicable status needs an effective date no later than cutoff')
        if r['status'] in ('unverified','proposal','adopted_not_applicable','superseded') or not reviewed or (cutoff-reviewed).days>max_age_days:
            pending.append(r['id'])
    return {'status':'REVIEW_REQUIRED' if pending else 'REGISTER_FIELDS_CURRENT','review_required':pending,'as_of':as_of,'review_age_limit_days':max_age_days,'human_legal_review_required':True,
            'limitation':'Schema and date checks do not verify source contents, completeness, jurisdictional interpretation or legal compliance.'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--as-of',default=date.today().isoformat());p.add_argument('--release-gate',action='store_true');args=p.parse_args()
    root=Path(__file__).resolve().parents[1]
    report=assess(json.loads((root/'regulatory/register.json').read_text())['records'],args.as_of)
    print(json.dumps(report,indent=2))
    if args.release_gate and report['status']!='REGISTER_FIELDS_CURRENT': raise SystemExit(2)


if __name__=='__main__': main()
