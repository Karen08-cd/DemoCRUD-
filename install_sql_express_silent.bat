@echo off
echo ========================================
echo INSTALACION DE SQL SERVER EXPRESS 2022
echo ========================================
echo.
echo Este script instalara SQL Server Express 2022
echo.
echo NOTA: Necesitas permisos de administrador
echo.

REM Verificar permisos de administrador
net session >nul 2>&1
if %errorLevel% == 0 (
    echo ✅ Permisos de administrador verificados
) else (
    echo ❌ ERROR: Necesitas ejecutar como administrador
    echo.
    echo Para ejecutar como administrador:
    echo 1. Clic derecho en este archivo
    echo 2. "Ejecutar como administrador"
    pause
    exit /b 1
)

echo.
echo Descargando SQL Server Express 2022...
echo.

REM Descargar SQL Server Express
powershell -Command "& {try { Invoke-WebRequest -Uri 'https://go.microsoft.com/fwlink/?linkid=2215160&clcid=0x409&culture=en-us&country=us' -OutFile 'SQLServerExpress.exe' -TimeoutSec 300 } catch { Write-Host 'Error descargando. Intentando URL alternativa...'; Invoke-WebRequest -Uri 'https://download.microsoft.com/download/5/1/4/5145fe04-4d30-4b85-b0d1-39533663ae36/SQLServer2022-SSEI-Expr.exe' -OutFile 'SQLServerExpress.exe' -TimeoutSec 300 }}"

if not exist SQLServerExpress.exe (
    echo ❌ ERROR: No se pudo descargar SQL Server Express
    echo.
    echo Descargalo manualmente desde:
    echo https://www.microsoft.com/en-us/sql-server/sql-server-downloads
    echo.
    echo Luego ejecuta el instalador y selecciona "Basic" installation
    pause
    exit /b 1
)

echo ✅ Descarga completada
echo.
echo Ejecutando instalador...
echo.
echo IMPORTANTE: Durante la instalacion selecciona:
echo - Installation type: Basic
echo - Accept license terms
echo - Instance name: SQLEXPRESS (default)
echo.

REM Ejecutar instalador
SQLServerExpress.exe /ACTION=Install /FEATURES=SQLEngine /INSTANCENAME=SQLEXPRESS /SQLSVCACCOUNT="NT AUTHORITY\Network Service" /SQLSYSADMINACCOUNTS="BUILTIN\ADMINISTRATORS" /TCPENABLED=1 /IACCEPTSQLSERVERLICENSETERMS /QUIET /HIDEPROGRESSBAR

if %errorLevel% == 0 (
    echo.
    echo ✅ INSTALACION COMPLETADA EXITOSAMENTE
    echo.
    echo Ahora ejecuta: python create_database.py
    echo.
) else (
    echo.
    echo ❌ ERROR en la instalacion (codigo: %errorLevel%)
    echo.
    echo Intenta instalacion manual desde:
    echo https://www.microsoft.com/en-us/sql-server/sql-server-downloads
    echo.
)

pause