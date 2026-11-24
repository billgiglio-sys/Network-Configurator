from fastapi.testclient import TestClient
from app.backend.main import app
client=TestClient(app)
def test_endpoints():
    p=client.get('/api/sample').json()
    assert client.post('/api/validate',json=p).status_code==200
    r=client.post('/api/render',json=p)
    assert r.status_code==200 and 'sw01' in r.json()['configs']
    z=client.post('/api/export/bundle',json=p)
    assert z.status_code==200 and z.headers['content-type']=='application/zip'
