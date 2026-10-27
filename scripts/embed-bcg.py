#!/usr/bin/env python3
"""Regenerate the offline snapshot from the canonical JSON; no third-party packages."""
import json,re
from pathlib import Path
root=Path(__file__).resolve().parents[1]
site=root/'dist' if (root/'dist/index.html').exists() else root
data=json.loads((site/'data/bcg.json').read_text())
p=site/'index.html'
text=p.read_text();snapshot=json.dumps(data,ensure_ascii=False).replace('</','<\\/')
pattern=r'(<script\b(?=[^>]*\bid="bcg-evidence-data")[^>]*>).*?(</script>)'
text,n=re.subn(pattern,lambda m:m[1]+snapshot+m[2],text,count=1,flags=re.S)
assert n==1,'Expected exactly one embedded dataset'
p.write_text(text)
print('Offline snapshot regenerated from dist/data/bcg.json.')
