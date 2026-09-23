import importlib.util
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
def load(name):
    s=importlib.util.spec_from_file_location(name,ROOT/'tools'/f'{name}.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
b,r=load('build_prompts'),load('check_register')
def record():
    return {'id':'test','jurisdiction':'TEST','instrument':'Synthetic rule','source_url':'https://example.org/rule','status':'unverified','effective_date':None,'last_reviewed':None,'reviewed_by':None,'provision':None,'prompt_ids':['01']}
class ValidationTests(unittest.TestCase):
    def test_xml_eight_blocks(self): b.validate(b.render('01','A & B < C; {{issuer}}'))
    def test_xml_task_preserved(self):
        import xml.etree.ElementTree as ET
        self.assertEqual(ET.fromstring(b.render('01','A & B < C')).find('task').text,'A & B < C')
    def test_wrong_block_count(self):
        with self.assertRaises(ValueError): b.validate('<prompt><role>R</role></prompt>')
    def test_extract_sections(self):
        text='### PROMPT 00 — Header\nHeader\n### PROMPT 01 — Task\nDo this.\n\n---\n## End\n'
        self.assertEqual(b.extract(text,1),{'01':'Do this.'})
    def test_count_guard(self):
        with self.assertRaises(ValueError): b.extract('### PROMPT 00 — Header\n',1)
    def test_doc_paths(self): self.assertEqual(b.normalize_docs('library/PROMPT_HEADER.md'),'PROMPT_HEADER.md')
    def test_unverified_blocks_release(self): self.assertEqual(r.assess([record()],'2026-09-23')['status'],'REVIEW_REQUIRED')
    def test_proposal_not_operative(self):
        x=record();x.update(status='proposal',last_reviewed='2026-09-22',reviewed_by='Synthetic reviewer',provision='Draft 1')
        self.assertEqual(r.assess([x],'2026-09-23')['status'],'REVIEW_REQUIRED')
    def test_applicable_requires_date(self):
        x=record();x.update(status='applicable',last_reviewed='2026-09-22',reviewed_by='Synthetic reviewer',provision='Section 1')
        with self.assertRaises(ValueError): r.assess([x],'2026-09-23')
    def test_future_review_rejected(self):
        x=record();x['last_reviewed']='2026-09-24'
        with self.assertRaises(ValueError): r.assess([x],'2026-09-23')
    def test_stale_review(self):
        x=record();x.update(status='applicable',last_reviewed='2026-01-01',effective_date='2025-01-01',reviewed_by='Synthetic reviewer',provision='Section 1')
        self.assertEqual(r.assess([x],'2026-09-23')['status'],'REVIEW_REQUIRED')
    def test_duplicate_ids(self):
        with self.assertRaises(ValueError): r.assess([record(),record()],'2026-09-23')

if __name__=='__main__': unittest.main()
