from copy import deepcopy
from pathlib import Path
import yaml
from validators.common.project import validate
from validators.common.topology import shortest_path

ROOT = Path(__file__).parents[2]
def sample():
    return yaml.safe_load((ROOT / 'examples/bill-home-lab/project.yaml').read_text())

def codes(project):
    return {item['code'] for item in validate(project)}

def test_sample_schema_and_ipam():
    assert validate(sample()) == []

def test_topology_path():
    assert shortest_path(sample(), 'wlc01', 'fw01') == ['wlc01', 'sw01', 'fw01']

def test_gateway_must_be_inside_subnet():
    project = sample()
    project['networks']['clients']['ipv4']['gateway'] = '10.99.99.1'
    assert 'IPAM-005' in codes(project)

def test_interface_references_existing_network():
    project = sample()
    project['interfaces']['sw01']['GigabitEthernet1/0/10']['ethernet']['access_network'] = 'missing'
    assert 'REF-002' in codes(project)

def test_link_references_existing_interface():
    project = sample()
    project['links'][0]['endpoint_a']['interface'] = 'missing'
    assert 'REF-005' in codes(project)
