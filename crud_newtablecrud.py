"""
Operaciones CRUD para NewTableCrud usando SQL Server.
"""
import pyodbc
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

def conectar_sqlserver():
    """Establece conexión con SQL Server usando variables de entorno."""
    try:
        server = os.getenv('SQL_SERVER')
        database = os.getenv('SQL_DATABASE')
        user = os.getenv('SQL_USER')
        password = os.getenv('SQL_PASSWORD')
        
        if not server or not database:
            print("❌ Variables de entorno SQL_SERVER y SQL_DATABASE son requeridas")
            return None
        
        if user and password:
            # Conexión con credenciales
            conn_str = f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={user};PWD={password}"
        else:
            # Conexión con autenticación integrada de Windows
            conn_str = f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes"
        
        conn = pyodbc.connect(conn_str)
        return conn
    except pyodbc.Error as e:
        print(f"❌ Error al conectar a SQL Server: {e}")
        return None

class CRUDNewTableCrud:
    """Clase para gestionar operaciones CRUD en la tabla dbo.NewTableCrud"""
    
    @staticmethod
    def crear_registro(nombre, descripcion, estado='activo'):
        """Crea un nuevo registro en NewTableCrud."""
        conexion = conectar_sqlserver()
        if not conexion:
            print("❌ No se pudo establecer conexión")
            return False

        try:
            cursor = conexion.cursor()
            cursor.execute(
                'INSERT INTO [dbo].[NewTableCrud] (nombre, descripcion, estado, fecha_creacion) VALUES (?, ?, ?, ?)',
                (nombre, descripcion, estado, datetime.now())
            )
            conexion.commit()
            print(f"✅ Registro '{nombre}' creado exitosamente en NewTableCrud")
            return True
        except pyodbc.Error as e:
            print(f"❌ Error al crear registro: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def leer_todos():
        """Lee todos los registros activos de NewTableCrud."""
        conexion = conectar_sqlserver()
        if not conexion:
            print("❌ No se pudo establecer conexión")
            return []

        try:
            cursor = conexion.cursor()
            cursor.execute(
                'SELECT id, nombre, descripcion, estado, fecha_creacion, fecha_actualizacion FROM [dbo].[NewTableCrud] WHERE estado = ? ORDER BY id DESC',
                ('activo',)
            )
            registros = cursor.fetchall()
            return [list(row) for row in registros]
        except pyodbc.Error as e:
            print(f"❌ Error al leer registros: {e}")
            return []
        finally:
            conexion.close()

    @staticmethod
    def leer_por_id(id_registro):
        """Lee un registro específico por ID."""
        conexion = conectar_sqlserver()
        if not conexion:
            print("❌ No se pudo establecer conexión")
            return None

        try:
            cursor = conexion.cursor()
            cursor.execute(
                'SELECT id, nombre, descripcion, estado, fecha_creacion, fecha_actualizacion FROM [dbo].[NewTableCrud] WHERE id = ?',
                (id_registro,)
            )
            registro = cursor.fetchone()
            return list(registro) if registro else None
        except pyodbc.Error as e:
            print(f"❌ Error al leer registro: {e}")
            return None
        finally:
            conexion.close()

    @staticmethod
    def actualizar_registro(id_registro, nombre, descripcion, estado):
        """Actualiza un registro existente."""
        conexion = conectar_sqlserver()
        if not conexion:
            print("❌ No se pudo establecer conexión")
            return False

        try:
            cursor = conexion.cursor()
            cursor.execute(
                'UPDATE [dbo].[NewTableCrud] SET nombre = ?, descripcion = ?, estado = ?, fecha_actualizacion = ? WHERE id = ?',
                (nombre, descripcion, estado, datetime.now(), id_registro)
            )
            conexion.commit()
            print(f"✅ Registro con ID {id_registro} actualizado exitosamente")
            return True
        except pyodbc.Error as e:
            print(f"❌ Error al actualizar registro: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def eliminar_registro(id_registro):
        """Marca un registro como eliminado (soft delete)."""
        conexion = conectar_sqlserver()
        if not conexion:
            print("❌ No se pudo establecer conexión")
            return False

        try:
            cursor = conexion.cursor()
            cursor.execute(
                'UPDATE [dbo].[NewTableCrud] SET estado = ?, fecha_actualizacion = ? WHERE id = ?',
                ('eliminado', datetime.now(), id_registro)
            )
            conexion.commit()
            print(f"✅ Registro con ID {id_registro} eliminado exitosamente")
            return True
        except pyodbc.Error as e:
            print(f"❌ Error al eliminar registro: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def leer_eliminados():
        """Lee todos los registros marcados como eliminados."""
        conexion = conectar_sqlserver()
        if not conexion:
            print("❌ No se pudo establecer conexión")
            return []

        try:
            cursor = conexion.cursor()
            cursor.execute(
                'SELECT id, nombre, descripcion, estado, fecha_creacion, fecha_actualizacion FROM [dbo].[NewTableCrud] WHERE estado = ? ORDER BY id DESC',
                ('eliminado',)
            )
            registros = cursor.fetchall()
            return [list(row) for row in registros]
        except pyodbc.Error as e:
            print(f"❌ Error al leer registros eliminados: {e}")
            return []
        finally:
            conexion.close()

    @staticmethod
    def restaurar_registro(id_registro):
        """Restaura un registro eliminado."""
        conexion = conectar_sqlserver()
        if not conexion:
            print("❌ No se pudo establecer conexión")
            return False

        try:
            cursor = conexion.cursor()
            cursor.execute(
                'UPDATE [dbo].[NewTableCrud] SET estado = ?, fecha_actualizacion = ? WHERE id = ?',
                ('activo', datetime.now(), id_registro)
            )
            conexion.commit()
            print(f"✅ Registro con ID {id_registro} restaurado exitosamente")
            return True
        except pyodbc.Error as e:
            print(f"❌ Error al restaurar registro: {e}")
            return False
        finally:
            conexion.close()
