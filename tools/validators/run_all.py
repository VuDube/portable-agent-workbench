from pathlib import Path
import hashlib, json, re, subprocess, sys
root=Path(__file__).resolve().parents[2]
report_dir=root/'11-EVALUATION/REPORTS'; report_dir.mkdir(parents=True,exist_ok=True)
results=[]
def check(test_id, objective, status, actual, evidence):
    results.append({'test_id':test_id,'objective':objective,'status':status,'expected':'The declared acceptance condition is satisfied.','actual':actual,'evidence':evidence})

# JSON syntax and schema shape checks without third-party packages.
schemas={}
for p in sorted((root/'10-SCHEMAS').glob('*.json')):
    try:
        data=json.loads(p.read_text()); schemas[p.name]=data
        required=data.get('required',[])
        check('STRUCT-'+p.stem,'Parse and inspect JSON Schema', 'PASS' if data.get('type')=='object' and required else 'FAIL', 'JSON parsed; object schema and required properties present' if data.get('type')=='object' and required else 'Schema missing object type or required properties', str(p.relative_to(root)))
    except Exception as exc:
        check('STRUCT-'+p.stem,'Parse JSON Schema','FAIL',str(exc),str(p.relative_to(root)))

# Skills and agents.
skill_count=0; skill_fail=[]
for p in sorted((root/'04-SKILLS').glob('**/SKILL.md')):
    skill_count+=1; t=p.read_text()
    ok=t.startswith('---\n') and '\n---\n' in t[4:]
    front=t[4:t.find('\n---\n',4)] if ok else ''
    nm=re.search(r'(?m)^name:\s*([^\n]+)$',front); ds=re.search(r'(?m)^description:\s*(.+)$',front)
    name=nm.group(1).strip().strip('"\'') if nm else ''
    if not (ok and nm and ds and name==p.parent.name and re.fullmatch(r'[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?',name)):
        skill_fail.append(str(p.relative_to(root)))
check('SKILL-001','Validate every skill frontmatter and name', 'PASS' if not skill_fail else 'FAIL', f'{skill_count} skills checked; failures={len(skill_fail)}', 'tools/validators/validate.py')

agent_paths=sorted((root/'03-AGENTS').glob('**/AGENT.md')); ids=[]; agent_fail=[]
for p in agent_paths:
    t=p.read_text(); m=re.search(r'(?m)^name:\s*([^\n]+)$',t[:t.find('\n---\n',4)] if t.startswith('---\n') else '')
    name=m.group(1).strip().strip('"\'') if m else ''
    ids.append(name)
    if not name or name!=p.parent.name: agent_fail.append(str(p.relative_to(root)))
check('AGENT-001','Validate agent identifiers and directories','PASS' if not agent_fail and len(ids)==len(set(ids)) else 'FAIL',f'{len(agent_paths)} files; unique_ids={len(set(ids))}; failures={len(agent_fail)}','tools/validators/validate.py')

# Internal links.
link_fail=[]
for p in root.rglob('*.md'):
    if '.git' in p.parts: continue
    for raw in re.findall(r'\[[^]]+\]\(([^)]+)\)',p.read_text()):
        target=raw.split('#',1)[0]
        if not target or '://' in target or target.startswith('mailto:'): continue
        target=target.replace('%20',' ')
        if not ((p.parent/target).exists() or (root/target).exists()): link_fail.append(f'{p.relative_to(root)} -> {raw}')
check('DOC-001','Validate internal Markdown links','PASS' if not link_fail else 'FAIL',f'broken_links={len(link_fail)}','tools/validators/run_all.py')

# Placeholder/empty files.
empty=[str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and '.git' not in p.parts and p.stat().st_size==0]
check('DOC-002','Detect empty repository files','PASS' if not empty else 'FAIL',f'empty_files={len(empty)}','tools/validators/run_all.py')

# Secret patterns: report only paths and pattern class, never matched text.
secret_patterns=[('private-key',re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----')),('github-token',re.compile(r'\bgh[pousr]_[A-Za-z0-9]{20,}\b')),('aws-access-key',re.compile(r'\bAKIA[0-9A-Z]{16}\b')),('openai-key',re.compile(r'\bsk-[A-Za-z0-9]{20,}\b'))]
secret_hits=[]
for p in root.rglob('*'):
    if not p.is_file() or '.git' in p.parts or p.stat().st_size>2_000_000: continue
    try:t=p.read_text(errors='ignore')
    except:continue
    for label,rx in secret_patterns:
        if rx.search(t): secret_hits.append((str(p.relative_to(root)),label))
check('SEC-001','Scan tracked text for common credential patterns','PASS' if not secret_hits else 'FAIL',f'potential_hits={len(secret_hits)}' if not secret_hits else f'potential_hits={len(secret_hits)} (review required)', 'tools/validators/run_all.py')

# Required files and counts.
required=['README.md','LICENSE','NOTICE.md','CONTRIBUTING.md','SECURITY.md','CODE_OF_CONDUCT.md','CITATION.cff','docs/UPSTREAM-SOURCES.md','docs/LICENCE-AND-ATTRIBUTION-REVIEW.md','docs/RELEASE-READINESS.md','11-EVALUATION/EVALUATION-FRAMEWORK.md']
missing=[x for x in required if not (root/x).is_file()]
check('STRUCT-REQUIRED','Check mandatory repository records exist','PASS' if not missing else 'FAIL',f'missing={missing}', 'tools/validators/validate.py')
check('CAT-001','Check mandatory agent and skill coverage','PASS' if len(agent_paths)>=46 and skill_count>=40 else 'FAIL',f'agents={len(agent_paths)} skills={skill_count}', 'docs/AGENT-CATALOG.md; docs/SKILL-CATALOG.md')

# Re-run the project validator as a regression test.
proc=subprocess.run([sys.executable,str(root/'tools/validators/validate.py')],capture_output=True,text=True)
check('REG-001','Run repository structural validator','PASS' if proc.returncode==0 else 'FAIL',proc.stdout.strip() or proc.stderr.strip(),'tools/validators/validate.py')

# Baseline archive reconciliation.
import zipfile
archive_candidates=[Path('/home/ubuntu/upload/portable-agent-workbench-v0.1.0-blueprint.zip'),root.parent/'portable-agent-workbench-v0.1.0-blueprint.zip']
archive=next((p for p in archive_candidates if p.is_file()),None)
if archive:
    with zipfile.ZipFile(archive) as z: expected=sorted(n.removeprefix('portable-agent-workbench/') for n in z.namelist())
    base=[x for x in expected if (root/x).is_file()]
    check('BASE-001','Confirm every original baseline file remains present','PASS' if base==expected else 'FAIL',f'baseline_present={len(base)}/{len(expected)}', 'archive SHA-256 recorded in docs/BASELINE-AUDIT.md')
else:
    check('BASE-001','Confirm every original baseline file remains present','BLOCKED','Source ZIP is not available in this CI checkout; remote baseline manifest remains the evidence source','docs/BASELINE-AUDIT.md')

commit=subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True).strip()
passed=sum(r['status']=='PASS' for r in results); failed=sum(r['status']=='FAIL' for r in results); blocked=sum(r['status']=='BLOCKED' for r in results); not_run=sum(r['status']=='NOT RUN' for r in results)
report={'tested_commit':commit,'tests':results,'summary':{'passed':passed,'failed':failed,'blocked':blocked,'not_run':not_run}}
(root/'11-EVALUATION/REPORTS/validation-report.json').write_text(json.dumps(report,indent=2)+'\n')
md=['# Automated validation report','','- Tested commit: `'+commit+'`',f'- Passed: {passed}',f'- Failed: {failed}',f'- Blocked: {blocked}',f'- Not run: {not_run}','']
for r in results: md.append(f"## {r['test_id']} — {r['status']}\n\n{r['objective']} Actual: {r['actual']} Evidence: `{r['evidence']}`.\n")
(root/'11-EVALUATION/REPORTS/validation-report.md').write_text('\n'.join(md)+'\n')
print(json.dumps(report['summary']))
if failed: sys.exit(1)
