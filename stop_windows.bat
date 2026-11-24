@echo off
setlocal EnableExtensions
echo Looking for Network Configurator on TCP port 8000...
for /f "tokens=5" %%P in ('netstat -ano ^| findstr /R /C:":8000 .*LISTENING"') do (
  echo Stopping PID %%P...
  taskkill /PID %%P /T >nul 2>nul
  if errorlevel 1 taskkill /PID %%P /T /F >nul 2>nul
  echo Stopped.
  exit /b 0
)
echo No process is listening on TCP port 8000.
exit /b 0
