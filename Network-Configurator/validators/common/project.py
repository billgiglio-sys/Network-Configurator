from __future__ import annotations
import ipaddress
from pathlib import Path
import json
from jsonschema import Draft202012Validator

SCHEMA = json.loads((Path(__file__).parents[2] / 'schemas/project.schema.json').read_text())

def validate(project: dict) -> list[dict]:
    findings=[]
    for error in Draft202012Validator(SCHEMA).iter_errors(project):
        findings.append({'severity':'error','code':'SCHEMA','message':error.message})
    seen_vlans={}; seen_nets=[]
    for key, item in project.get('networks',{}).items():
        vlan=item.get('vlan',{}).get('id')
        if vlan in seen_vlans:
            findings.append({'severity':'error','code':'IPAM-001','message':f'Duplicate VLAN {vlan}: {seen_vlans[vlan]} and {key}'})
        seen_vlans[vlan]=key
        try:
            net=ipaddress.ip_network(item['ipv4']['subnet'],strict=False)
            for previous_key,previous in seen_nets:
                if net.overlaps(previous):
                    findings.append({'severity':'error','code':'IPAM-002','message':f'Overlapping subnets: {previous_key} and {key}'})
            seen_nets.append((key,net))
        except (ValueError,KeyError) as exc:
            findings.append({'severity':'error','code':'IPAM-003','message':f'{key}: {exc}'})
    return findings
