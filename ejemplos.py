"""
Ejemplos de uso avanzado del CRUD
"""
from crud_operations import CRUDEmpleado

# ============================================
# EJEMPLO 1: Crear múltiples empleados
# ============================================
def crear_empleados_ejemplo():
    """Crea varios empleados de ejemplo"""
    empleados_datos = [
        ("Juan", "Pérez", "juan.perez@email.com", "555-0001", 45000),
        ("María", "García", "maria.garcia@email.com", "555-0002", 50000),
        ("Carlos", "López", "carlos.lopez@email.com", "555-0003", 48000),
        ("Ana", "Martínez", "ana.martinez@email.com", "555-0004", 52000),
        ("Pedro", "Rodríguez", "pedro.rodriguez@email.com", "555-0005", 46000),
    ]
    
    print("📝 Creando empleados de ejemplo...\n")
    for nombre, apellido, email, telefono, salario in empleados_datos:
        CRUDEmpleado.crear_empleado(nombre, apellido, email, telefono, salario)


# ============================================
# EJEMPLO 2: Listar todos con formato
# ============================================
def listar_empleados_formateado():
    """Lista todos los empleados con formato mejorado"""
    print("\n📋 LISTA DE EMPLEADOS\n")
    empleados = CRUDEmpleado.leer_todos()
    
    if empleados:
        for emp in empleados:
            id_emp, nombre, apellido, email, telefono, fecha_ingreso, salario, estado = emp
            print(f"ID: {id_emp}")
            print(f"  Nombre: {nombre} {apellido}")
            print(f"  Email: {email or 'N/A'}")
            print(f"  Teléfono: {telefono or 'N/A'}")
            print(f"  Salario: ${salario:,.2f}" if salario else "  Salario: N/A")
            print(f"  Fecha Ingreso: {fecha_ingreso}")
            print(f"  Estado: {estado or 'N/A'}")
            print("-" * 50)


# ============================================
# EJEMPLO 3: Buscar empleados por criterios
# ============================================
def buscar_por_rango_salario(salario_min, salario_max):
    """Busca empleados en rango de salario"""
    print(f"\n🔍 Empleados con salario entre ${salario_min:,.2f} y ${salario_max:,.2f}\n")
    empleados = CRUDEmpleado.leer_todos()
    
    encontrados = 0
    for emp in empleados:
        id_emp, nombre, apellido, email, telefono, fecha_ingreso, salario, estado = emp
        if salario and salario_min <= salario <= salario_max:
            print(f"✓ {nombre} {apellido} - ${salario:,.2f}")
            encontrados += 1
    
    if encontrados == 0:
        print("No se encontraron empleados en ese rango")


# ============================================
# EJEMPLO 4: Generar reporte
# ============================================
def generar_reporte():
    """Genera un reporte de empleados"""
    print("\n📊 REPORTE DE EMPLEADOS\n")
    empleados = CRUDEmpleado.leer_todos()
    
    if not empleados:
        print("No hay empleados registrados")
        return
    
    total_empleados = len(empleados)
    total_salarios = sum([emp[6] for emp in empleados if emp[6]])
    promedio_salario = total_salarios / len([emp for emp in empleados if emp[6]]) if total_salarios > 0 else 0
    
    print(f"Total de empleados: {total_empleados}")
    print(f"Salario total: ${total_salarios:,.2f}")
    print(f"Salario promedio: ${promedio_salario:,.2f}")
    
    # Empleado con mayor salario
    empleados_con_salario = [emp for emp in empleados if emp[6]]
    if empleados_con_salario:
        mayor = max(empleados_con_salario, key=lambda x: x[6])
        print(f"\nEmpleado con mayor salario:")
        print(f"  {mayor[1]} {mayor[2]} - ${mayor[6]:,.2f}")
        
        # Empleado con menor salario
        menor = min(empleados_con_salario, key=lambda x: x[6])
        print(f"\nEmpleado con menor salario:")
        print(f"  {menor[1]} {menor[2]} - ${menor[6]:,.2f}")


# ============================================
# EJEMPLO 5: Actualización en lote
# ============================================
def aumentar_salario(id_empleado, porcentaje):
    """Aumenta el salario de un empleado por porcentaje"""
    empleado = CRUDEmpleado.leer_por_id(id_empleado)
    
    if not empleado:
        print(f"Empleado {id_empleado} no encontrado")
        return
    
    id_emp, nombre, apellido, email, telefono, fecha_ingreso, salario, estado = empleado
    
    if not salario:
        print(f"Empleado {nombre} {apellido} no tiene salario registrado")
        return
    
    nuevo_salario = salario * (1 + porcentaje / 100)
    CRUDEmpleado.actualizar_empleado(
        id_emp, nombre, apellido, email, telefono, nuevo_salario
    )
    print(f"Salario de {nombre} {apellido} actualizado:")
    print(f"  Anterior: ${salario:,.2f}")
    print(f"  Nuevo: ${nuevo_salario:,.2f}")
    print(f"  Aumento: {porcentaje}%")


# ============================================
# EJEMPLO 6: Exportar a CSV
# ============================================
def exportar_a_csv(nombre_archivo="empleados.csv"):
    """Exporta los empleados a un archivo CSV"""
    import csv
    from datetime import datetime
    
    empleados = CRUDEmpleado.leer_todos()
    
    if not empleados:
        print("No hay empleados para exportar")
        return
    
    try:
        with open(nombre_archivo, 'w', newline='', encoding='utf-8') as csvfile:
            campos = ['ID', 'Nombre', 'Apellido', 'Email', 'Teléfono', 'Fecha Ingreso', 'Salario', 'Estado']
            writer = csv.writer(csvfile)
            writer.writerow(campos)
            
            for emp in empleados:
                id_emp, nombre, apellido, email, telefono, fecha_ingreso, salario, estado = emp
                writer.writerow([
                    id_emp,
                    nombre,
                    apellido,
                    email or '',
                    telefono or '',
                    fecha_ingreso,
                    salario or '',
                    estado or ''
                ])
        
        print(f"✅ Archivo '{nombre_archivo}' creado exitosamente")
    except Exception as e:
        print(f"❌ Error al exportar: {e}")


# ============================================
# Ejecutar ejemplos
# ============================================
if __name__ == "__main__":
    print("="*50)
    print("    EJEMPLOS DE USO AVANZADO - CRUD EMPLEADOS")
    print("="*50)
    
    # Descomentar los ejemplos que desees ejecutar:
    
    # crear_empleados_ejemplo()
    # listar_empleados_formateado()
    # buscar_por_rango_salario(45000, 50000)
    # generar_reporte()
    # aumentar_salario(1, 10)  # Aumentar 10% al empleado ID 1
    # exportar_a_csv("reporte_empleados.csv")
    
    print("\n💡 Descomenta los ejemplos en el código para ejecutarlos")
