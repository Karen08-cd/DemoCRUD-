"""
Script para detectar servidores SQL Server disponibles en la red
"""
import socket
import subprocess
import os

def detectar_servidores_sql():
    """Detecta servidores SQL Server disponibles en la red local"""
    print("=" * 60)
    print("DETECTANDO SERVIDORES SQL SERVER EN LA RED")
    print("=" * 60)

    servidores_encontrados = []

    # Método 1: Usar sqlcmd para listar servidores
    print("\n🔍 Método 1: Usando sqlcmd para detectar servidores")
    try:
        result = subprocess.run(['sqlcmd', '-L'], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')
            for line in lines:
                if line.strip() and not line.startswith('Servers:'):
                    servidor = line.strip()
                    if servidor and servidor != 'localhost':
                        servidores_encontrados.append(servidor)
                        print(f"  ✅ {servidor}")
        else:
            print("  ❌ sqlcmd no pudo detectar servidores")
    except Exception as e:
        print(f"  ❌ Error con sqlcmd: {e}")

    # Método 2: Escanear puertos comunes en localhost
    print("\n🔍 Método 2: Escaneando localhost en puertos SQL Server")
    puertos_sql = [1433, 1434]  # 1433 = SQL Server, 1434 = SQL Browser

    for puerto in puertos_sql:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex(('localhost', puerto))
            if result == 0:
                print(f"  ✅ localhost:{puerto} - Puerto abierto")
                if puerto == 1433:
                    servidores_encontrados.append('localhost')
                elif puerto == 1434:
                    servidores_encontrados.append('(local)')
            else:
                print(f"  ❌ localhost:{puerto} - Puerto cerrado")
            sock.close()
        except Exception as e:
            print(f"  ❌ Error escaneando puerto {puerto}: {e}")

    # Método 3: Verificar variables de entorno
    print("\n🔍 Método 3: Variables de entorno SQL Server")
    sql_vars = ['COMPUTERNAME', 'USERDNSDOMAIN']
    for var in sql_vars:
        value = os.environ.get(var)
        if value:
            print(f"  ℹ️  {var}: {value}")

    # Método 4: Verificar servicios SQL Server
    print("\n🔍 Método 4: Servicios SQL Server activos")
    try:
        result = subprocess.run(['sc', 'query', 'type=', 'service', 'state=', 'all'],
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            lines = result.stdout.split('\n')
            sql_services = []
            for line in lines:
                if 'SQL' in line.upper() and 'SERVICE_NAME' in line:
                    service_line = line.split(':')[1].strip()
                    sql_services.append(service_line)

            if sql_services:
                for service in sql_services:
                    print(f"  ✅ Servicio encontrado: {service}")
            else:
                print("  ℹ️  No se encontraron servicios SQL Server")
        else:
            print("  ❌ Error consultando servicios")
    except Exception as e:
        print(f"  ❌ Error consultando servicios: {e}")

    print("\n" + "=" * 60)
    print("SERVIDORES POSIBLES PARA PROBAR:")
    print("=" * 60)

    posibles_servidores = [
        'localhost',
        '(local)',
        '127.0.0.1',
        socket.gethostname(),
        '.\\SQLEXPRESS',  # Instancia por defecto de SQL Express
        'localhost\\SQLEXPRESS',
        '(local)\\SQLEXPRESS'
    ]

    # Agregar servidores encontrados
    for srv in servidores_encontrados:
        if srv not in posibles_servidores:
            posibles_servidores.append(srv)

    for i, servidor in enumerate(posibles_servidores, 1):
        print(f"{i:2d}. {servidor}")

    print("\n" + "=" * 60)
    print("PRÓXIMOS PASOS:")
    print("=" * 60)
    print("""
1. Prueba cada servidor de la lista anterior
2. Actualiza tu .env con el servidor correcto:
   SQL_SERVER=nombre_del_servidor_correcto

3. Si ninguno funciona, verifica:
   - Que SQL Server esté ejecutándose (Services.msc)
   - Que tengas permisos para conectarte
   - Que el firewall no bloquee el puerto 1433

4. Si usas SQL Server Express, el nombre podría ser:
   - .\\SQLEXPRESS
   - localhost\\SQLEXPRESS
   - (local)\\SQLEXPRESS
""")
    print("=" * 60)

if __name__ == "__main__":
    detectar_servidores_sql()
