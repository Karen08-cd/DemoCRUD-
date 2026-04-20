"""
Script para probar diferentes nombres de servidor SQL Server
"""
import pyodbc
import time

def probar_conexion(servidor, base_datos="master", timeout=5):
    """Prueba conexión a un servidor SQL Server específico"""
    try:
        conn_str = f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={servidor};DATABASE={base_datos};Trusted_Connection=yes;Connection Timeout={timeout}"
        start = time.time()
        conn = pyodbc.connect(conn_str, timeout=timeout)
        elapsed = time.time() - start
        print(f"  ✅ {servidor} - Conexión exitosa ({elapsed:.2f}s)")
        conn.close()
        return True
    except pyodbc.Error as e:
        elapsed = time.time() - start
        error_msg = str(e)
        if "Login timeout expired" in error_msg:
            print(f"  ⏰ {servidor} - Timeout ({elapsed:.2f}s)")
        elif "Server is not found" in error_msg:
            print(f"  ❌ {servidor} - Servidor no encontrado")
        elif "18456" in error_msg or "login failed" in error_msg:
            print(f"  🔒 {servidor} - Error de autenticación")
        else:
            print(f"  ⚠️  {servidor} - Error: {error_msg[:50]}...")
        return False

def main():
    print("=" * 60)
    print("PRUEBA DE CONEXIÓN A DIFERENTES SERVIDORES SQL")
    print("=" * 60)

    # Lista de servidores a probar
    servidores_a_probar = [
        "TEST\\CLBSTEST01",  # Tu servidor original
        "localhost",
        "(local)",
        "127.0.0.1",
        ".\\SQLEXPRESS",
        "localhost\\SQLEXPRESS",
        "(local)\\SQLEXPRESS",
        "E036300UAVRPG3",  # Nombre de tu máquina
        "E036300UAVRPG3\\SQLEXPRESS",
    ]

    print("Probando conexiones con autenticación integrada de Windows...")
    print("(Esto puede tardar varios minutos)\n")

    exitosos = []
    for servidor in servidores_a_probar:
        print(f"Probando: {servidor}")
        if probar_conexion(servidor):
            exitosos.append(servidor)
        time.sleep(1)  # Pequeña pausa entre pruebas

    print("\n" + "=" * 60)
    if exitosos:
        print("✅ SERVIDORES QUE FUNCIONAN:")
        for srv in exitosos:
            print(f"   • {srv}")
        print(f"\nActualiza tu .env con:")
        print(f"SQL_SERVER={exitosos[0]}")
    else:
        print("❌ NINGÚN SERVIDOR RESPONDIÓ")
        print("\nPosibles causas:")
        print("• SQL Server no está instalado")
        print("• SQL Server no está ejecutándose")
        print("• El servidor está en otra máquina y no es accesible")
        print("• Firewall bloqueando conexiones")
        print("• Problemas de red")

    print("\nSi tienes SQL Server Management Studio:")
    print("1. Ábrelo")
    print("2. En 'Server name' verás el nombre correcto")
    print("3. Copia ese nombre exacto a tu .env")

if __name__ == "__main__":
    main()
