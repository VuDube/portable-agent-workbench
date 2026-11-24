#!/usr/bin/env python3
"""Low-dependency structural checks for Portable Agent Workbench."""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
errors=[]
def fail(msg): errors.append(msg)

required = ['README.md','LICENSE','NOTICE.md','CHANGELOG.md','CONTRIBUTING.md','SECURITY.md','CODE_OF_CONDUCT.md','CITATION.cff','docs/PRODUCT-SPECIFICATION.md','docs/ACCEPTANCE-TESTS.md']
for rel in required:
    if not (ROOT/rel).is_file(): fail(f'missing required file: {rel}')

for p in ROOT.rglob('*.json'):
    if '.git' in p.parts: continue
    try: json.loads(p.read_text())
    except Exception as exc: fail(f'invalid JSON {p.relative_to(ROOT)}: {exc}')

ids=[]
for p in ROOT.glob('03-AGENTS/**/AGENT.md'):
    text=p.read_text()
    if not text.startswith('---\n'):
        fail(f'agent frontmatter missing: {p.relative_to(ROOT)}')
        continue
    end=text.find('\n---\n', 4)
    if end < 0:
        fail(f'agent frontmatter unterminated: {p.relative_to(ROOT)}')
        continue
    front=text[4:end]
    nm=re.search(r'(?m)^name:\s*([^\n]+)$', front)
    ds=re.search(r'(?m)^description:\s*(.+)$', front)
    if not nm or not ds:
        fail(f'agent name/description missing: {p.relative_to(ROOT)}')
        continue
    name=nm.group(1).strip().strip('"\'')
    if name != p.parent.name:
        fail(f'agent name does not match directory: {p.relative_to(ROOT)}')
    ids.append(name)
for p in ROOT.glob('04-SKILLS/**/SKILL.md'):
    text=p.read_text()
    if not text.startswith('---\n'): fail(f'skill frontmatter missing: {p.relative_to(ROOT)}'); continue
    end=text.find('\n---\n',4)
    if end < 0: fail(f'skill frontmatter unterminated: {p.relative_to(ROOT)}'); continue
    front=text[4:end]
    nm=re.search(r'(?m)^name:\s*([^\n]+)$', front); ds=re.search(r'(?m)^description:\s*(.+)$', front)
    if not nm or not ds: fail(f'skill name/description missing: {p.relative_to(ROOT)}'); continue
    name=nm.group(1).strip().strip('"\'')
    if name != p.parent.name: fail(f'skill name does not match directory: {p.relative_to(ROOT)}')
    if not re.fullmatch(r'[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?', name) or '--' in name: fail(f'invalid skill name: {name}')
    if len(ds.group(1).strip().strip('"\'')) > 1024: fail(f'skill description too long: {p.relative_to(ROOT)}')

for p in ROOT.rglob('*'):
    if p.is_file() and '.git' not in p.parts and p.stat().st_size == 0: fail(f'empty file: {p.relative_to(ROOT)}')

if errors:
    print('VALIDATION FAILED')
    print('\n'.join(f'- {e}' for e in errors))
    sys.exit(1)
print('VALIDATION PASSED')
