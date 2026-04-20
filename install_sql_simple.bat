@echo off
echo ========================================
echo DESCARGA E INSTALACION DE SQL SERVER EXPRESS
echo ========================================
echo.

echo Descargando SQL Server Express 2022...
echo.

REM Descargar usando PowerShell
powershell -Command "& {Invoke-WebRequest -Uri 'https://go.microsoft.com/fwlink/?linkid=2215160&clcid=0x409&culture=en-us&country=us' -OutFile 'SQLServerExpress.exe'}"

if not exist SQLServerExpress.exe (
    echo ❌ ERROR: No se pudo descargar SQL Server Express
    echo.
    echo Intenta descargar manualmente desde:
    echo https://www.microsoft.com/en-us/sql-server/sql-server-downloads
    echo.
    echo Luego ejecuta el instalador como administrador
    pause
    exit /b 1
)

echo ✅ Descarga completada
echo.
echo Instalando SQL Server Express...
echo.
echo IMPORTANTE: Si aparece una ventana de UAC, haz clic en "Si"
echo.

REM Ejecutar instalador como administrador
powershell -Command "& {Start-Process 'SQLServerExpress.exe' -Verb RunAs -Wait}"

echo.
echo ✅ INSTALACION COMPLETADA
echo.
echo Ahora ejecuta: python create_database.py
echo.

pause