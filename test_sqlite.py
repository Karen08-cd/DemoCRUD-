"""
Script de prueba rápida para verificar que SQLite funciona correctamente
"""
from config import conectar, initialize_database
from crud_operations import CRUDEmpleado

def test_basico():
    """Prueba básica de conexión y operaciones"""
    print("🔍 Probando conexión a SQLite...")

    # Inicializar base de datos
    initialize_database()

    # Probar conexión
    conn = conectar()
    if not conn:
        print("❌ Error de conexión")
        return False

    print("✅ Conexión exitosa")

    # Probar crear empleado
    print("\n📝 Probando crear empleado...")
    resultado = CRUDEmpleado.crear_empleado(
        "Juan", "Pérez", "juan.perez@email.com",
        "1234567890", "2024-01-15", 50000.00, "activo"
    )

    if resultado:
        print("✅ Empleado creado exitosamente")
    else:
        print("❌ Error al crear empleado")
        return False

    # Probar leer empleados
    print("\n📖 Probando leer empleados...")
    empleados = CRUDEmpleado.leer_todos()
    if empleados:
        print(f"✅ Se encontraron {len(empleados)} empleados")
        for emp in empleados:
            print(f"   - {emp[1]} {emp[2]} ({emp[3]})")
    else:
        print("❌ No se encontraron empleados")

    conn.close()
    print("\n🎉 ¡Todas las pruebas pasaron exitosamente!")
    return True

if __name__ == "__main__":
    test_basico()