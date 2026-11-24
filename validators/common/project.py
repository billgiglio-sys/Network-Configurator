from __future__ import annotations
import ipaddress
from pathlib import Path
import json
from jsonschema import Draft202012Validator

SCHEMA = json.loads((Path(__file__).parents[2] / 'schemas/project.schema.json').read_text())

def finding(code, message):
    return {'severity': 'error', 'code': code, 'message': message}

def validate(project: dict) -> list[dict]:
    findings = []
    for error in Draft202012Validator(SCHEMA).iter_errors(project):
        path = '.'.join(str(part) for part in error.absolute_path)
        findings.append(finding('SCHEMA', f'{path}: {error.message}' if path else error.message))

    seen_vlans = {}
    seen_nets = []
    networks = project.get('networks', {})
    for key, item in networks.items():
        vlan = item.get('vlan', {}).get('id')
        if vlan in seen_vlans:
            findings.append(finding('IPAM-001', f'Duplicate VLAN {vlan}: {seen_vlans[vlan]} and {key}'))
        elif vlan is not None:
            seen_vlans[vlan] = key
        try:
            network = ipaddress.ip_network(item['ipv4']['subnet'], strict=False)
            if str(network) != item['ipv4']['subnet']:
                findings.append(finding('IPAM-004', f'{key}: subnet must use canonical network notation {network}'))
            gateway = item.get('ipv4', {}).get('gateway')
            if gateway and ipaddress.ip_address(gateway) not in network:
                findings.append(finding('IPAM-005', f'{key}: gateway {gateway} is outside {network}'))
            for previous_key, previous in seen_nets:
                if network.overlaps(previous):
                    findings.append(finding('IPAM-002', f'Overlapping subnets: {previous_key} and {key}'))
            seen_nets.append((key, network))
        except (ValueError, KeyError) as exc:
            findings.append(finding('IPAM-003', f'{key}: {exc}'))

    devices = project.get('devices', {})
    interfaces = project.get('interfaces', {})
    for device_id in interfaces:
        if device_id not in devices:
            findings.append(finding('REF-001', f'Interfaces reference undefined device {device_id}'))
    for device_id, group in interfaces.items():
        for interface_name, interface in group.items():
            ethernet = interface.get('ethernet', {})
            access_network = ethernet.get('access_network')
            if access_network and access_network not in networks:
                findings.append(finding('REF-002', f'{device_id}:{interface_name} references undefined access network {access_network}'))
            for network_id in ethernet.get('trunk', {}).get('allowed_networks', []):
                if network_id not in networks:
                    findings.append(finding('REF-003', f'{device_id}:{interface_name} references undefined trunk network {network_id}'))
            address = interface.get('ipv4', {}).get('address')
            if address:
                try:
                    ipaddress.ip_interface(address)
                except ValueError as exc:
                    findings.append(finding('IPAM-006', f'{device_id}:{interface_name}: {exc}'))

    for link in project.get('links', []):
        for endpoint_name in ('endpoint_a', 'endpoint_b'):
            endpoint = link.get(endpoint_name, {})
            device_id, interface_name = endpoint.get('device'), endpoint.get('interface')
            if device_id not in devices:
                findings.append(finding('REF-004', f'{link.get("id", "link")}: undefined device {device_id}'))
            elif interface_name not in interfaces.get(device_id, {}):
                findings.append(finding('REF-005', f'{link.get("id", "link")}: undefined interface {device_id}:{interface_name}'))
    return findings
