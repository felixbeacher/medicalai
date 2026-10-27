#!/usr/bin/env python3
"""Check provenance completeness, numerical bounds, and absence of old test outputs."""
import json,math,re
from pathlib import Path
root=Path(__file__).resolve().parents[1]
site=root/'dist' if (root/'dist/index.html').exists() else root
data=json.loads((site/'data/bcg.json').read_text());html=(site/'index.html').read_text()
ids=[s['id'] for s in data['sources']];assert len(ids)==len(set(ids))
for s in data['sources']:
 assert s['url'].startswith('https://') and s['title'] and s['locator'] and s['accessed']
estids=[e['id'] for e in data['estimates']];assert len(estids)==len(set(estids))
for e in data['estimates']:
 for key in ['population','time_period','outcome','measure','limitations','source_ids']:assert e.get(key),f'Missing {key}: {e["id"]}'
 assert set(e['source_ids'])<=set(ids)
 if 'interval' in e:assert e['interval']['low']<=e['value']<=e['interval']['high']
 if 'derived' in e:
  for dest,value in [('value',e['value']),('low',e['interval']['high']),('high',e['interval']['low'])]:assert math.isclose(e['derived'][dest],100*(1-value))
 if e['measure']=='label_frequency_band':
  assert 0<e['lower']<e['upper']<1 and e['upper_exclusive']
  assert math.isclose(e['display_lower'],e['lower']*e['denominator'])
  assert math.isclose(e['display_upper'],e['upper']*e['denominator'])
assert all(v is None for v in data['missing_data'].values())
snapshot=re.search(r'<script\b(?=[^>]*\bid="bcg-evidence-data")[^>]*>(.*?)</script>',html,re.S)[1]
assert json.loads(snapshot)==data,'Embedded snapshot differs from canonical JSON'
assert 'const BCG_TEST=' not in html and '100 vs 40' not in html
assert 'input[type="range"]' not in html and 'id="severity-weight"' not in html
m=data['research_model'];by_id={e['id']:e for e in data['estimates']};prev=by_id[m['prevalence_record_id']];weight=by_id[m['severity_record_id']];expected=prev['value']/prev['denominator']*weight['value']
assert math.isclose(m['value_fraction'],expected) and math.isclose(m['value_per_100'],expected*100)
assert m['uncertainty_interval'] is None and m['assumptions'] and m['status']=='exploratory_not_clinically_validated'
assert data['schema_version']==2
print(f'PASS: {len(data["estimates"])} records, provenance, bounds, derived arithmetic, explicit model assumptions and offline snapshot.')
