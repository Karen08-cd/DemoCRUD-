@echo off
echo ========================================
echo GUIA DE INSTALACION DE SQL SERVER EXPRESS
echo ========================================
echo.
echo OPCION 1: Instalacion automatica (recomendada)
echo Ejecuta: install_sql_express_silent.bat
echo.
echo OPCION 2: Instalacion manual paso a paso
echo.

echo PASO 1: Descargar SQL Server Express
echo -----------------------------------
echo Ve a: https://www.microsoft.com/en-us/sql-server/sql-server-downloads
echo - Selecciona "Download now" en SQL Server 2022 Express Edition
echo - Guarda el archivo como "SQLServerExpress.exe"
echo.

echo PASO 2: Ejecutar el instalador
echo -----------------------------
echo - Clic derecho en SQLServerExpress.exe
echo - "Ejecutar como administrador"
echo - Selecciona "Basic" installation
echo - Acepta los terminos de licencia
echo - El nombre de instancia sera: SQLEXPRESS
echo - Autenticacion: Windows Authentication
echo.

echo PASO 3: Verificar instalacion
echo ---------------------------
echo Despues de instalar, ejecuta:
echo python create_database.py
echo.

echo PASO 4: Probar la aplicacion
echo ---------------------------
echo python app.py
echo.

pause