@echo off
echo ========================================
echo INSTALACION DE SQL SERVER EXPRESS 2022
echo ========================================
echo.
echo Este script descargara e instalara SQL Server Express 2022
echo.
echo NOTA: Necesitas permisos de administrador para continuar
echo.

pause

echo.
echo Descargando SQL Server Express 2022...
echo.

REM Descargar SQL Server Express
powershell -Command "& {Invoke-WebRequest -Uri 'https://go.microsoft.com/fwlink/?linkid=2215160&clcid=0x409&culture=en-us&country=us' -OutFile 'SQLServerExpress.exe'}"

if not exist SQLServerExpress.exe (
    echo ERROR: No se pudo descargar SQL Server Express
    echo Descargalo manualmente desde: https://www.microsoft.com/en-us/sql-server/sql-server-downloads
    pause
    exit /b 1
)

echo.
echo Ejecutando instalador de SQL Server Express...
echo.
echo IMPORTANTE: Durante la instalacion:
echo 1. Selecciona "Basic" installation
echo 2. Acepta los terminos
echo 3. El nombre de instancia sera: SQLEXPRESS
echo 4. La autenticacion sera: Windows Authentication
echo.

SQLServerExpress.exe

echo.
echo ========================================
echo INSTALACION COMPLETADA
echo ========================================
echo.
echo Para verificar que SQL Server esta funcionando:
echo 1. Abre SQL Server Management Studio (SSMS)
echo 2. Conectate a: localhost\SQLEXPRESS
echo 3. Crea una base de datos llamada: LC-PRU-NephroCalc
echo.
echo Luego actualiza tu .env:
echo SQL_SERVER=localhost\SQLEXPRESS
echo.

pause