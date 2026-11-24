from __future__ import annotations
import io, json, zipfile
from pathlib import Path
import yaml
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, Response
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from validators.common.project import validate as validate_common

ROOT=Path(__file__).parents[2]
FRONT=ROOT/'app/frontend'
J2=Environment(loader=FileSystemLoader(ROOT/'renderers'),undefined=StrictUndefined,trim_blocks=True,lstrip_blocks=True)
app=FastAPI(title='Network Configurator',version='0.1.0')
app.mount('/assets',StaticFiles(directory=FRONT),name='assets')

def catalogs():
    out=[]
    for vendor in ('cisco','fortinet'):
        data=yaml.safe_load((ROOT/f'catalog/{vendor}/platforms.yaml').read_text())
        for p in data['platforms']:
            p=dict(p);p['vendor']=vendor;out.append(p)
    return out

def platform_for(model):
    return next((p for p in catalogs() if model in p['models']),None)

def validate_project(project):
    findings=validate_common(project)
    env=project.get('project',{}).get('environment','lab')
    for did,device in project.get('devices',{}).items():
        platform=platform_for(device.get('platform',{}).get('model'))
        if not platform:
            findings.append({'severity':'error','code':'CATALOG-001','message':f'{did}: model is not in the platform catalog'})
            continue
        version=str(device.get('software',{}).get('version'))
        if version not in [str(v) for v in platform['versions']]:
            findings.append({'severity':'error','code':'CATALOG-002','message':f'{did}: {version} is not approved for {device["platform"]["model"]}'})
        if platform.get('lifecycle') in {'end_of_sale','end_of_support'}:
            severity='error' if env=='production' else 'warning'
            findings.append({'severity':severity,'code':'LIFE-001','message':f'{did}: lifecycle is {platform["lifecycle"]}'})
    errors=sum(f['severity']=='error' for f in findings); warnings=sum(f['severity']=='warning' for f in findings)
    return {'status':'not_ready' if errors else ('ready_with_warnings' if warnings else 'ready'),'counts':{'errors':errors,'warnings':warnings},'findings':findings}

def render(project):
    configs={}
    for did,device in project['devices'].items():
        template=J2.get_template(device['renderer'])
        configs[did]=template.render(project=project,device=device,device_id=did).strip()+'\n'
    return configs

@app.get('/')
def index(): return FileResponse(FRONT/'index.html')
@app.get('/api/catalog')
def get_catalog(): return {'platforms':catalogs()}
@app.get('/api/sample')
def get_sample(): return yaml.safe_load((ROOT/'examples/bill-home-lab/project.yaml').read_text())
@app.post('/api/validate')
def validate(project:dict): return validate_project(project)
@app.post('/api/render')
def render_api(project:dict): return {'validation':validate_project(project),'configs':render(project)}
@app.post('/api/export/yaml')
def export_yaml(project:dict):
    return Response(yaml.safe_dump(project,sort_keys=False),media_type='application/yaml',headers={'Content-Disposition':f'attachment; filename="{project["project"]["id"]}.yaml"'})
@app.post('/api/export/bundle')
def export_bundle(project:dict):
    validation=validate_project(project); configs=render(project); project_id=project['project']['id']; b=io.BytesIO()
    with zipfile.ZipFile(b,'w',zipfile.ZIP_DEFLATED) as z:
        z.writestr(f'{project_id}/project.yaml',yaml.safe_dump(project,sort_keys=False))
        z.writestr(f'{project_id}/inventory.json',json.dumps(project['devices'],indent=2))
        z.writestr(f'{project_id}/reports/validation.json',json.dumps(validation,indent=2))
        z.writestr(f'{project_id}/reports/deployment-plan.md','# Deployment Plan\n\n1. Review validation.\n2. Back up devices.\n3. Apply underlay before services.\n4. Verify each dependency.\n')
        z.writestr(f'{project_id}/reports/rollback-plan.md','# Rollback Plan\n\n1. Stop on failed validation.\n2. Restore pre-change configurations.\n3. Verify management and traffic.\n')
        for did,cfg in configs.items(): z.writestr(f'{project_id}/configs/{project["devices"][did]["name"]}.cfg',cfg)
    return Response(b.getvalue(),media_type='application/zip',headers={'Content-Disposition':f'attachment; filename="{project_id}-deployment-bundle.zip"'})
