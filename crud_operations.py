"""
Operaciones CRUD para Empleados usando SQLite.
"""
from config import conectar
import sqlite3

class CRUDEmpleado:
    @staticmethod
    def crear_empleado(nombre, apellido, email, telefono, fecha_ingreso, salario, estado):
        """Crea un nuevo empleado."""
        conexion = conectar()
        if not conexion:
            return False

        try:
            cursor = conexion.cursor()
            cursor.execute(
                'INSERT INTO empleados (nombre, apellido, email, telefono, fecha_ingreso, salario, estado) VALUES (?, ?, ?, ?, ?, ?, ?)',
                (nombre, apellido, email, telefono, fecha_ingreso, salario, estado)
            )
            conexion.commit()
            print(f"✅ Empleado '{nombre} {apellido}' creado exitosamente")
            return True
        except sqlite3.Error as e:
            print(f"❌ Error al crear empleado: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def leer_todos():
        """Lee todos los empleados activos."""
        conexion = conectar()
        if not conexion:
            return []

        try:
            cursor = conexion.cursor()
            cursor.execute('SELECT id, nombre, apellido, email, telefono, fecha_ingreso, salario, estado FROM empleados WHERE estado = ? ORDER BY id DESC', ('activo',))
            empleados = cursor.fetchall()
            return [list(row) for row in empleados]
        except sqlite3.Error as e:
            print(f"❌ Error al leer empleados: {e}")
            return []
        finally:
            conexion.close()

    @staticmethod
    def leer_eliminados():
        """Lee todos los empleados eliminados."""
        conexion = conectar()
        if not conexion:
            return []

        try:
            cursor = conexion.cursor()
            cursor.execute('SELECT id, nombre, apellido, email, telefono, fecha_ingreso, salario, estado FROM empleados WHERE estado = ? ORDER BY id DESC', ('eliminado',))
            empleados = cursor.fetchall()
            return [list(row) for row in empleados]
        except sqlite3.Error as e:
            print(f"❌ Error al leer empleados eliminados: {e}")
            return []
        finally:
            conexion.close()

    @staticmethod
    def actualizar_empleado(id, nombre, apellido, email, telefono, fecha_ingreso, salario, estado):
        """Actualiza un empleado existente."""
        conexion = conectar()
        if not conexion:
            return False

        try:
            cursor = conexion.cursor()
            cursor.execute(
                'UPDATE empleados SET nombre=?, apellido=?, email=?, telefono=?, fecha_ingreso=?, salario=?, estado=? WHERE id=?',
                (nombre, apellido, email, telefono, fecha_ingreso, salario, estado, id)
            )
            conexion.commit()
            if cursor.rowcount > 0:
                print(f"✅ Empleado ID {id} actualizado exitosamente")
                return True
            else:
                print(f"❌ No se encontró empleado con ID {id}")
                return False
        except sqlite3.Error as e:
            print(f"❌ Error al actualizar empleado: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def eliminar_empleado(id):
        """Elimina un empleado (borrado lógico)."""
        conexion = conectar()
        if not conexion:
            return False

        try:
            cursor = conexion.cursor()
            cursor.execute('UPDATE empleados SET estado=? WHERE id=?', ('eliminado', id))
            conexion.commit()
            if cursor.rowcount > 0:
                print(f"✅ Empleado ID {id} eliminado exitosamente")
                return True
            else:
                print(f"❌ No se encontró empleado con ID {id}")
                return False
        except sqlite3.Error as e:
            print(f"❌ Error al eliminar empleado: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def buscar_empleado(termino):
        """Busca empleados por nombre, apellido o email."""
        conexion = conectar()
        if not conexion:
            return []

        try:
            cursor = conexion.cursor()
            query = """
                SELECT id, nombre, apellido, email, telefono, fecha_ingreso, salario, estado
                FROM empleados
                WHERE (nombre LIKE ? OR apellido LIKE ? OR email LIKE ?) AND estado = 'activo'
                ORDER BY id DESC
            """
            search_term = f'%{termino}%'
            cursor.execute(query, (search_term, search_term, search_term))
            empleados = cursor.fetchall()
            return [list(row) for row in empleados]
        except sqlite3.Error as e:
            print(f"❌ Error al buscar empleados: {e}")
            return []
        finally:
            conexion.close()

    @staticmethod
    def buscar_empleado(termino):
        """Busca empleados por nombre, apellido o email."""
        conexion = conectar()
        if not conexion:
            return []

        try:
            cursor = conexion.cursor()
            query = """
                SELECT id, nombre, apellido, email, telefono, fecha_ingreso, salario, estado 
                FROM empleados 
                WHERE (nombre LIKE ? OR apellido LIKE ? OR email LIKE ?) AND estado = 'activo'
                ORDER BY id DESC
            """
            search_term = f'%{termino}%'
            cursor.execute(query, (search_term, search_term, search_term))
            empleados = cursor.fetchall()
            return empleados
        except sqlite3.Error as e:
            print(f"❌ Error al buscar empleados: {e}")
            return []
        finally:
            conexion.close()
