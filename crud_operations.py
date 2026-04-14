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
            cursor.execute('SELECT id, nombre, apellido, email, telefono, fecha_ingreso, salario, estado FROM empleados ORDER BY id DESC')
            empleados = cursor.fetchall()
            return empleados
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
            cursor.execute('SELECT id, nombre, apellido, email, telefono, fecha_ingreso, salario, estado FROM deleted_empleados ORDER BY id DESC')
            empleados = cursor.fetchall()
            return empleados
        except sqlite3.Error as e:
            print(f"❌ Error al leer empleados eliminados: {e}")
            return []
        finally:
            conexion.close()

    @staticmethod
    def leer_por_id(id_empleado):
        """Lee un empleado por ID."""
        conexion = conectar()
        if not conexion:
            return None

        try:
            cursor = conexion.cursor()
            cursor.execute('SELECT id, nombre, apellido, email, telefono, fecha_ingreso, salario, estado FROM empleados WHERE id = ?', (id_empleado,))
            empleado = cursor.fetchone()
            return empleado
        except sqlite3.Error as e:
            print(f"❌ Error al leer empleado: {e}")
            return None
        finally:
            conexion.close()

    @staticmethod
    def actualizar_empleado(id_empleado, nombre, apellido, email, telefono, fecha_ingreso, salario, estado):
        """Actualiza un empleado."""
        conexion = conectar()
        if not conexion:
            return False

        try:
            cursor = conexion.cursor()
            cursor.execute(
                'UPDATE empleados SET nombre = ?, apellido = ?, email = ?, telefono = ?, fecha_ingreso = ?, salario = ?, estado = ? WHERE id = ?',
                (nombre, apellido, email, telefono, fecha_ingreso, salario, estado, id_empleado)
            )
            conexion.commit()
            print(f"✅ Empleado ID {id_empleado} actualizado exitosamente")
            return True
        except sqlite3.Error as e:
            print(f"❌ Error al actualizar empleado: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def eliminar_empleado(id_empleado):
        """Elimina un empleado moviéndolo a la tabla de eliminados."""
        conexion = conectar()
        if not conexion:
            return False

        try:
            cursor = conexion.cursor()
            cursor.execute('SELECT id, nombre, apellido, email, telefono, fecha_ingreso, salario, estado FROM empleados WHERE id = ?', (id_empleado,))
            empleado = cursor.fetchone()
            if not empleado:
                return False

            cursor.execute(
                'INSERT OR REPLACE INTO deleted_empleados (id, nombre, apellido, email, telefono, fecha_ingreso, salario, estado) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                (empleado[0], empleado[1], empleado[2], empleado[3], empleado[4], empleado[5], empleado[6], 'Eliminado')
            )
            cursor.execute('DELETE FROM empleados WHERE id = ?', (id_empleado,))
            conexion.commit()
            print(f"✅ Empleado ID {id_empleado} movido a eliminados exitosamente")
            return True
        except sqlite3.Error as e:
            print(f"❌ Error al eliminar empleado: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def restaurar_todos():
        """Restaura todos los empleados desde la tabla de eliminados."""
        conexion = conectar()
        if not conexion:
            return False

        try:
            cursor = conexion.cursor()
            cursor.execute('SELECT id, nombre, apellido, email, telefono, fecha_ingreso, salario, estado FROM deleted_empleados')
            empleados = cursor.fetchall()
            if not empleados:
                return True

            cursor.executemany(
                'INSERT OR REPLACE INTO empleados (id, nombre, apellido, email, telefono, fecha_ingreso, salario, estado) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                [(emp[0], emp[1], emp[2], emp[3], emp[4], emp[5], emp[6], 'Activo') for emp in empleados]
            )
            cursor.execute('DELETE FROM deleted_empleados')
            conexion.commit()
            print("✅ Todos los empleados eliminados restaurados exitosamente")
            return True
        except sqlite3.Error as e:
            print(f"❌ Error al restaurar todos los empleados: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def restaurar_empleado(id_empleado):
        """Restaura un empleado desde la tabla de eliminados."""
        conexion = conectar()
        if not conexion:
            return False

        try:
            cursor = conexion.cursor()
            cursor.execute('SELECT id, nombre, apellido, email, telefono, fecha_ingreso, salario, estado FROM deleted_empleados WHERE id = ?', (id_empleado,))
            empleado = cursor.fetchone()
            if not empleado:
                return False

            cursor.execute(
                'INSERT OR REPLACE INTO empleados (id, nombre, apellido, email, telefono, fecha_ingreso, salario, estado) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                (empleado[0], empleado[1], empleado[2], empleado[3], empleado[4], empleado[5], empleado[6], 'Activo')
            )
            cursor.execute('DELETE FROM deleted_empleados WHERE id = ?', (id_empleado,))
            conexion.commit()
            print(f"✅ Empleado ID {id_empleado} restaurado exitosamente")
            return True
        except sqlite3.Error as e:
            print(f"❌ Error al restaurar empleado: {e}")
            return False
        finally:
            conexion.close()
