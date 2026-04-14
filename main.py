"""
Aplicacion CRUD de Empleados
Menu interactivo para gestionar empleados
"""
from crud_operations import CRUDEmpleado
from config import verificar_conexion
import os
import sys

def limpiar_pantalla():
    """Limpia la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    """Muestra el menu principal"""
    print("\n" + "="*50)
    print("       CRUD DE EMPLEADOS - MENU PRINCIPAL")
    print("="*50)
    print("1. ➕ Crear nuevo empleado")
    print("2. 📋 Ver todos los empleados")
    print("3. 🔍 Buscar empleado por ID")
    print("4. ✏️  Actualizar empleado")
    print("5. ❌ Eliminar empleado")
    print("6. 🚪 Salir")
    print("="*50)

def crear_empleado():
    """Opcion para crear empleado"""
    limpiar_pantalla()
    print("\n📝 CREAR NUEVO EMPLEADO")
    print("-" * 50)
    
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    email = input("Email (opcional): ").strip() or None
    telefono = input("Telefono (opcional): ").strip() or None
    
    try:
        salario = input("Salario (opcional, número): ").strip()
        salario = float(salario) if salario else None
    except ValueError:
        print("❌ Salario inválido")
        salario = None
    
    if nombre and apellido:
        CRUDEmpleado.crear_empleado(nombre, apellido, email, telefono, salario)
    else:
        print("❌ Nombre y Apellido son requeridos")
    
    input("\n📌 Presiona Enter para continuar...")

def ver_todos():
    """Opcion para ver todos los empleados"""
    limpiar_pantalla()
    print("\n📋 LISTA DE EMPLEADOS")
    print("-" * 50)
    
    empleados = CRUDEmpleado.leer_todos()
    
    if not empleados:
        print("No hay empleados registrados")
    else:
        print(f"{'ID':<5} {'Nombre':<20} {'Apellido':<20} {'Email':<25} {'Telefono':<15} {'Salario':<10} {'Estado':<8}")
        print("-" * 120)
        for emp in empleados:
            id_emp, nombre, apellido, email, telefono, fecha_ingreso, salario, estado = emp
                estado_txt = estado or 'N/A'
    input("\n📌 Presiona Enter para continuar...")

def buscar_por_id():
    """Opcion para buscar empleado por ID"""
    limpiar_pantalla()
    print("\n🔍 BUSCAR EMPLEADO POR ID")
    print("-" * 50)
    
    try:
        id_emp = int(input("ID del empleado: "))
        empleado = CRUDEmpleado.leer_por_id(id_emp)
        
        if empleado:
            id_emp, nombre, apellido, email, telefono, fecha_ingreso, salario, estado = empleado
            estado_txt = estado or 'N/A'
            print(f"\n✅ Empleado encontrado:")
            print(f"ID: {id_emp}")
            print(f"Nombre: {nombre}")
            print(f"Apellido: {apellido}")
            print(f"Email: {email or 'N/A'}")
            print(f"Telefono: {telefono or 'N/A'}")
            print(f"Fecha Ingreso: {fecha_ingreso}")
            print(f"Salario: {salario or 'N/A'}")
            print(f"Estado: {estado_txt}")
        else:
            print(f"❌ No se encontró empleado con ID {id_emp}")
    except ValueError:
        print("❌ ID inválido")
    
    input("\n📌 Presiona Enter para continuar...")

def actualizar_empleado():
    """Opcion para actualizar empleado"""
    limpiar_pantalla()
    print("\n✏️  ACTUALIZAR EMPLEADO")
    print("-" * 50)
    
    try:
        id_emp = int(input("ID del empleado: "))
        empleado = CRUDEmpleado.leer_por_id(id_emp)
        
        if not empleado:
            print(f"❌ No se encontró empleado con ID {id_emp}")
        else:
            id_emp, nombre, apellido, email, telefono, fecha_ingreso, salario, estado = empleado
            
            print(f"\nDatos actuales:")
            print(f"Nombre: {nombre}")
            print(f"Apellido: {apellido}")
            print(f"Email: {email or 'N/A'}")
            print(f"Telefono: {telefono or 'N/A'}")
            print(f"Salario: {salario or 'N/A'}")
                print(f"Estado: {estado or 'N/A'}")
                print("❌ Salario inválido")
                nuevo_salario = salario
            
            CRUDEmpleado.actualizar_empleado(id_emp, nuevo_nombre, nuevo_apellido, nuevo_email, nuevo_telefono, nuevo_salario)
    except ValueError:
        print("❌ ID inválido")
    
    input("\n📌 Presiona Enter para continuar...")

def eliminar_empleado():
    """Opcion para eliminar empleado"""
    limpiar_pantalla()
    print("\n❌ ELIMINAR EMPLEADO")
    print("-" * 50)
    
    try:
        id_emp = int(input("ID del empleado a eliminar: "))
        confirmacion = input(f"¿Seguro que deseas eliminar el empleado ID {id_emp}? (s/n): ").lower()
        
        if confirmacion == 's':
            CRUDEmpleado.eliminar_empleado(id_emp)
        else:
            print("Operacion cancelada")
    except ValueError:
        print("❌ ID inválido")
    
    input("\n📌 Presiona Enter para continuar...")

def main():
    """Funcion principal"""
    limpiar_pantalla()
    
    print("\n🔍 Verificando conexion a SQL Server...")
    if not verificar_conexion():
        print("\n⚠️  Actualiza los datos de conexion en el archivo '.env'")
        input("Presiona Enter para salir...")
        sys.exit(1)
    
    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input("Selecciona una opcion (1-6): ").strip()
        
        if opcion == '1':
            crear_empleado()
        elif opcion == '2':
            ver_todos()
        elif opcion == '3':
            buscar_por_id()
        elif opcion == '4':
            actualizar_empleado()
        elif opcion == '5':
            eliminar_empleado()
        elif opcion == '6':
            print("\n👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opcion inválida")
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()
