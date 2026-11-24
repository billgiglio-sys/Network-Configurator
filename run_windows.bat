@echo off
setlocal EnableExtensions
cd /d "%~dp0"

echo.
echo ============================================================
echo  Network Configurator
echo ============================================================
echo.

where py >nul 2>nul
if errorlevel 1 (
  where python >nul 2>nul
  if errorlevel 1 (
    echo ERROR: Python 3.11 or newer was not found.
    echo Install Python from https://www.python.org/downloads/windows/
    pause
    exit /b 1
  )
  set "PYTHON=python"
) else (
  set "PYTHON=py -3"
)

if not exist ".venv\Scripts\python.exe" (
  echo Creating virtual environment...
  %PYTHON% -m venv .venv || goto :error
)

set "VENV_PYTHON=%CD%\.venv\Scripts\python.exe"
echo Installing dependencies...
"%VENV_PYTHON%" -m pip install --disable-pip-version-check -r requirements.txt || goto :error

echo.
echo Network Configurator: http://127.0.0.1:8000
echo Press Ctrl+C in this window to stop the server.
echo PowerShell ISE is not supported for hosting the server.
echo.
"%VENV_PYTHON%" -m uvicorn app.backend.main:app --reload --host 127.0.0.1 --port 8000
set "EXIT_CODE=%ERRORLEVEL%"
echo.
echo Network Configurator stopped.
exit /b %EXIT_CODE%

:error
echo.
echo ERROR: Network Configurator could not start.
pause
exit /b 1
