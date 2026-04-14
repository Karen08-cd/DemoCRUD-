"""
Tests para las operaciones CRUD
"""
import unittest
from crud_operations import CRUDEmpleado

class TestCRUDEmpleado(unittest.TestCase):
    """Tests para las operaciones CRUD"""
    
    def setUp(self):
        """Ejecuta antes de cada test"""
        self.nombre_test = "TestEmpleado"
        self.apellido_test = "Prueba"
    
    def test_crear_empleado(self):
        """Test: Crear un empleado"""
        resultado = CRUDEmpleado.crear_empleado(
            self.nombre_test,
            self.apellido_test,
            "test@email.com",
            "555-1234",
            40000
        )
        self.assertTrue(resultado)
    
    def test_leer_empleados(self):
        """Test: Leer todos los empleados"""
        empleados = CRUDEmpleado.leer_todos()
        self.assertIsInstance(empleados, list)
    
    def test_leer_por_id(self):
        """Test: Leer empleado por ID"""
        # Primero crear un empleado
        CRUDEmpleado.crear_empleado("Juan", "Test", "juan@test.com")
        
        # Luego buscarlo
        empleados = CRUDEmpleado.leer_todos()
        if empleados:
            empleado = CRUDEmpleado.leer_por_id(empleados[0][0])
            self.assertIsNotNone(empleado)
    
    def test_actualizar_empleado(self):
        """Test: Actualizar un empleado"""
        # Crear empleado
        CRUDEmpleado.crear_empleado("Pedro", "Prueba", "pedro@test.com")
        
        # Obtener el último empleado creado
        empleados = CRUDEmpleado.leer_todos()
        if empleados:
            id_emp = empleados[0][0]
            resultado = CRUDEmpleado.actualizar_empleado(
                id_emp,
                "PedroActualizado",
                "PruebaActualizada"
            )
            self.assertTrue(resultado)
    
    def test_eliminar_empleado(self):
        """Test: Eliminar un empleado"""
        # Crear empleado
        CRUDEmpleado.crear_empleado("Ana", "Test", "ana@test.com")
        
        # Obtener el último empleado
        empleados = CRUDEmpleado.leer_todos()
        if empleados:
            id_emp = empleados[0][0]
            resultado = CRUDEmpleado.eliminar_empleado(id_emp)
            self.assertTrue(resultado)

if __name__ == "__main__":
    print("\n" + "="*50)
    print("    EJECUTANDO TESTS DEL CRUD")
    print("="*50 + "\n")
    
    unittest.main(verbosity=2)
