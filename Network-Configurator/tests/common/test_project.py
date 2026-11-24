from pathlib import Path
import yaml
from validators.common.project import validate
from validators.common.topology import shortest_path
ROOT=Path(__file__).parents[2]
def sample(): return yaml.safe_load((ROOT/'examples/bill-home-lab/project.yaml').read_text())
def test_sample_schema_and_ipam(): assert validate(sample()) == []
def test_topology_path(): assert shortest_path(sample(),'wlc01','fw01') == ['wlc01','sw01','fw01']
