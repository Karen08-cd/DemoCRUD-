"""
Diagnóstico avanzado de conexión a SQL Server
"""
import pyodbc
import os
from dotenv import load_dotenv
import socket
import time

load_dotenv()

SERVER = os.getenv('SQL_SERVER')
DATABASE = os.getenv('SQL_DATABASE')
USER = os.getenv('SQL_USER')
PASSWORD = os.getenv('SQL_PASSWORD')

print("=" * 70)
print("DIAGNÓSTICO DE CONEXIÓN A SQL SERVER")
print("=" * 70)

print("\n📋 CONFIGURACIÓN DETECTADA:")
print(f"  • Servidor: {SERVER}")
print(f"  • Base de datos: {DATABASE}")
print(f"  • Usuario: {USER if USER else '(Autenticación integrada de Windows)'}")
print(f"  • Contraseña: {'Configurada' if PASSWORD else 'NO configurada'}")

# Verificar conectividad al servidor
print("\n🔍 Prueba 1: Conectividad de RED al servidor")
try:
    host = SERVER.split('\\')[0]  # Obtener el host del formato SERVIDOR\INSTANCIA
    print(f"  • Intentando contactar a: {host}")
    
    socket.setdefaulttimeout(3)  # Timeout de 3 segundos
    result = socket.create_connection((host, 1433), timeout=3)
    result.close()
    print(f"  ✅ Servidor {host} es accesible en puerto 1433")
except socket.timeout:
    print(f"  ❌ TIMEOUT: No se puede alcanzar {host} en puerto 1433")
    print(f"     - Verifica que el servidor SQL esté ejecutándose")
    print(f"     - Verifica la conectividad de red")
    print(f"     - Verifica firewall")
except socket.error as e:
    print(f"  ❌ ERROR: {e}")

# Verificar drivers
print("\n🔍 Prueba 2: Drivers ODBC disponibles")
drivers = pyodbc.drivers()
sql_drivers = [d for d in drivers if 'SQL' in d or 'sql' in d]
if sql_drivers:
    for driver in sql_drivers:
        print(f"  ✅ {driver}")
else:
    print(f"  ❌ No se encontraron drivers SQL Server")

# Intentar conexión con timeout
print("\n🔍 Prueba 3: Conexión a SQL Server (30 segundos máximo)")
print("  ⏳ Conectando... (esto puede tardar)")

try:
    # Usar signal para timeout en Windows
    start = time.time()
    
    if USER and PASSWORD:
        conn_str = f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USER};PWD={PASSWORD};Connection Timeout=5"
    else:
        conn_str = f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;Connection Timeout=5"
    
    conn = pyodbc.connect(conn_str, timeout=5)
    elapsed = time.time() - start
    print(f"  ✅ Conexión exitosa en {elapsed:.2f} segundos")
    conn.close()
    
except pyodbc.OperationalError as e:
    error_msg = str(e)
    elapsed = time.time() - start
    print(f"  ❌ Error operacional ({elapsed:.2f}s): {error_msg}")
    
    if "18456" in error_msg or "login failed" in error_msg:
        print(f"     → Problema: CREDENCIALES INCORRECTAS")
        print(f"     → Usuario o contraseña inválidos")
    elif "Cannot open server" in error_msg or "Named Pipes" in error_msg:
        print(f"     → Problema: SERVIDOR NO ENCONTRADO")
        print(f"     → Verifica el nombre del servidor: {SERVER}")
    else:
        print(f"     → Revisa el error anterior")
        
except Exception as e:
    elapsed = time.time() - start
    print(f"  ❌ Error ({elapsed:.2f}s): {e}")

print("\n" + "=" * 70)
print("SOLUCIONES POSIBLES:")
print("=" * 70)
print("""
1. Si el servidor NO es accesible (Prueba 1 falló):
   → SQL Server no está corriendo o no es accesible
   → Verifica: SQL Server Management Studio o Services.msc

2. Si las credenciales son incorrectas:
   → Verifica usuario y contraseña en .env
   → Prueba en SQL Server Management Studio manualmente

3. Si todo parece bien:
   → Intenta usar autenticación integrada (Trusted_Connection)
   → Deja USER y PASSWORD vacíos en .env
""")
print("=" * 70)
