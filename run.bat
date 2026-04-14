@echo off
REM Script para instalar dependencias y ejecutar la aplicacion

ECHO.
ECHO ====================================================
ECHO   CRUD DE EMPLEADOS - INSTALACION Y EJECUCION
ECHO ====================================================
ECHO.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no está instalado o no está en PATH
    pause
    exit /b 1
)

echo. ✓ Python encontrado

REM Instalar dependencias
echo.
echo Instalando dependencias...
pip install -r requirements.txt

if errorlevel 1 (
    echo ERROR: No se pudieron instalar las dependencias
    pause
    exit /b 1
)

echo. ✓ Dependencias instaladas

REM Ejecutar la aplicacion
echo.
echo ====================================================
echo   Iniciando aplicacion...
echo ====================================================
echo.

python app.py

pause
