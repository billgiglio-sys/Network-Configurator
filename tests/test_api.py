from fastapi.testclient import TestClient
from app.backend.main import app

client = TestClient(app)

def test_endpoints():
    project = client.get('/api/sample').json()
    assert client.get('/api/schema/project').status_code == 200
    assert client.post('/api/validate', json=project).status_code == 200
    rendered = client.post('/api/render', json=project)
    assert rendered.status_code == 200 and 'sw01' in rendered.json()['configs']
    exported = client.post('/api/export/yaml', json=project)
    assert exported.status_code == 200
    assert 'application/yaml' in exported.headers['content-type']
    bundle = client.post('/api/export/bundle', json=project)
    assert bundle.status_code == 200 and bundle.headers['content-type'] == 'application/zip'

def test_yaml_round_trip():
    project = client.get('/api/sample').json()
    exported = client.post('/api/export/yaml', json=project)
    imported = client.post('/api/import/yaml', json={'yaml': exported.text})
    assert imported.status_code == 200
    assert imported.json()['project'] == project
    assert imported.json()['validation']['counts']['errors'] == 0

def test_invalid_project_cannot_export_or_render():
    project = client.get('/api/sample').json()
    project['networks']['clients']['vlan']['id'] = 10
    assert client.post('/api/export/yaml', json=project).status_code == 422
    rendered = client.post('/api/render', json=project).json()
    assert rendered['validation']['counts']['errors'] > 0
    assert rendered['configs'] == {}
