"""
Script para agregar datos de ejemplo a la base de datos
"""
from crud_operations import CRUDEmpleado

def agregar_datos_ejemplo():
    """Agrega algunos empleados de ejemplo"""
    empleados_ejemplo = [
        {
            "nombre": "Juan",
            "apellido": "Pérez",
            "email": "juan.perez@empresa.com",
            "telefono": "5551234567",
            "fecha_ingreso": "2025-01-15",
            "salario": 2500000.00,
            "estado": "Activo"
        },
        {
            "nombre": "María",
            "apellido": "García",
            "email": "maria.garcia@empresa.com",
            "telefono": "5552345678",
            "fecha_ingreso": "2025-03-20",
            "salario": 3200000.00,
            "estado": "Activo"
        },
        {
            "nombre": "Carlos",
            "apellido": "Rodríguez",
            "email": "carlos.rodriguez@empresa.com",
            "telefono": "5553456789",
            "fecha_ingreso": "2025-06-10",
            "salario": 2800000.00,
            "estado": "Activo"
        },
        {
            "nombre": "Ana",
            "apellido": "López",
            "email": "ana.lopez@empresa.com",
            "telefono": "5554567890",
            "fecha_ingreso": "2025-09-05",
            "salario": 3500000.00,
            "estado": "Activo"
        }
    ]

    print("📝 Agregando empleados de ejemplo...")

    for emp in empleados_ejemplo:
        resultado = CRUDEmpleado.crear_empleado(
            emp["nombre"],
            emp["apellido"],
            emp["email"],
            emp["telefono"],
            emp["fecha_ingreso"],
            emp["salario"],
            emp["estado"]
        )

        if resultado:
            print(f"✅ Agregado: {emp['nombre']} {emp['apellido']}")
        else:
            print(f"❌ Error al agregar: {emp['nombre']} {emp['apellido']}")

    print("\n🎉 ¡Datos de ejemplo agregados exitosamente!")
    print("Ahora puedes probar la aplicación con datos reales.")

if __name__ == "__main__":
    agregar_datos_ejemplo()