from pathlib import Path
import yaml
ROOT=Path(__file__).parents[2]
def test_c3850_and_wireless_catalog():
    c=yaml.safe_load((ROOT/'catalog/cisco/platforms.yaml').read_text())['platforms']
    p=next(x for x in c if x['id']=='catalyst_3850')
    assert 'WS-C3850-48P' in p['models'] and '16.12.16' in [str(v) for v in p['versions']]
    w=next(x for x in c if x['id']=='cisco_3504')
    assert 'wpa2_wpa3_transition' in w['capabilities']
