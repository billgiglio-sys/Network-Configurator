# Core editor overlay

Target repository commit: `10984ce6eae3d687c7ae0706b40dbc3daf66fa22`

Copy the contents of this overlay into the repository root, allowing existing files to be replaced.

## Files changed

- `run_windows.bat`
- `stop_windows.bat` (new)
- `app/backend/main.py`
- `app/frontend/index.html`
- `app/frontend/app.js`
- `app/frontend/app.css`
- `validators/common/project.py`
- `tests/test_api.py`
- `tests/common/test_project.py`

## Apply on Windows

From the cloned repository root:

```powershell
# Create a feature branch first
git switch -c core/editable-project-ui

# Extract the overlay ZIP into the repository root and overwrite files.

# Review
git diff --stat
git diff

# Test
.\.venv\Scripts\python.exe -m pytest

# Run from Windows Terminal or normal PowerShell, not PowerShell ISE
.\run_windows.bat
```

Open `http://127.0.0.1:8000`.

## Added behavior

- New, Open YAML, Save YAML, Validate, and Deployment Bundle controls
- Unsaved-change indicator and browser-close warning
- Editable project metadata
- Device add/edit/clone/delete using catalog-backed models
- Network add/edit/clone/delete
- Interface add/edit/delete
- Referential cleanup when IDs are renamed or objects are deleted
- Server-side YAML import and validated YAML/bundle export
- Rendering blocked when validation contains errors
- Gateway-in-subnet and interface/link reference validation
- Windows stop script for a server left on TCP/8000

## Known boundary

Wireless and topology remain read-only in this increment. The UI edits the current schema without changing shared schema contracts. Vendor-specific renderer expansion remains gated by reviewed Vendor Rules.
