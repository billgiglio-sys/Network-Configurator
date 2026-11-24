from pathlib import Path
ROOT=Path(__file__).parents[2]
def test_legacy_fortigate_builder_preserved():
    p=ROOT/'legacy/fortigate-builder/index.html'
    assert p.exists() and 'FortiGate Config Builder' in p.read_text()
