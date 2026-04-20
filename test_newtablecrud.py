"""
Script de prueba para verificar conexión y CRUD de NewTableCrud
"""
from config import conectar, initialize_newtablecrud
from crud_newtablecrud import CRUDNewTableCrud

def test_conexion():
    """Prueba la conexión a la base de datos"""
    print("\n" + "="*60)
    print("🔍 PRUEBA DE CONEXIÓN A BASE DE DATOS")
    print("="*60)
    
    conn = conectar()
    if conn:
        print("✅ Conexión exitosa a SQL Server")
        print(f"✅ Base de datos: LC-PRU-NephroCalc")
        conn.close()
        return True
    else:
        print("❌ Falló la conexión a SQL Server")
        return False

def test_inicializar_tabla():
    """Inicializa la tabla NewTableCrud"""
    print("\n" + "="*60)
    print("🗂️  INICIALIZACIÓN DE TABLA NewTableCrud")
    print("="*60)
    initialize_newtablecrud()

def test_crud_operaciones():
    """Prueba las operaciones CRUD"""
    print("\n" + "="*60)
    print("🧪 PRUEBAS DE OPERACIONES CRUD")
    print("="*60)
    
    # Crear
    print("\n1️⃣  CREAR registros:")
    CRUDNewTableCrud.crear_registro("Registro 1", "Descripción del registro 1")
    CRUDNewTableCrud.crear_registro("Registro 2", "Descripción del registro 2")
    CRUDNewTableCrud.crear_registro("Registro 3", "Descripción del registro 3")
    
    # Leer todos
    print("\n2️⃣  LEER todos los registros activos:")
    registros = CRUDNewTableCrud.leer_todos()
    if registros:
        for reg in registros:
            print(f"   ID: {reg[0]}, Nombre: {reg[1]}, Descripción: {reg[2]}, Estado: {reg[3]}")
    else:
        print("   No hay registros activos")
    
    # Leer por ID
    print("\n3️⃣  LEER registro específico (ID=1):")
    registro = CRUDNewTableCrud.leer_por_id(1)
    if registro:
        print(f"   {registro}")
    else:
        print("   Registro no encontrado")
    
    # Actualizar
    print("\n4️⃣  ACTUALIZAR registro:")
    CRUDNewTableCrud.actualizar_registro(1, "Registro 1 Actualizado", "Nueva descripción", "activo")
    
    # Eliminar (soft delete)
    print("\n5️⃣  ELIMINAR registro (soft delete):")
    CRUDNewTableCrud.eliminar_registro(2)
    
    # Leer eliminados
    print("\n6️⃣  LEER registros eliminados:")
    eliminados = CRUDNewTableCrud.leer_eliminados()
    if eliminados:
        for reg in eliminados:
            print(f"   ID: {reg[0]}, Nombre: {reg[1]}, Estado: {reg[3]}")
    else:
        print("   No hay registros eliminados")
    
    # Restaurar
    print("\n7️⃣  RESTAURAR registro eliminado:")
    CRUDNewTableCrud.restaurar_registro(2)

if __name__ == "__main__":
    print("\n🚀 INICIANDO PRUEBAS DE CONEXIÓN Y CRUD\n")
    
    # Prueba 1: Conexión
    if not test_conexion():
        print("\n❌ No se puede continuar sin conexión")
        exit(1)
    
    # Prueba 2: Inicializar tabla
    test_inicializar_tabla()
    
    # Prueba 3: CRUD
    test_crud_operaciones()
    
    print("\n" + "="*60)
    print("✅ PRUEBAS COMPLETADAS")
    print("="*60 + "\n")
