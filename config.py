"""
Configuración de conexión a base de datos SQLite.
"""
import sqlite3
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Configuración para SQLite
DATABASE = os.getenv('SQLITE_DATABASE', 'empleados.db')

def conectar():
    """Establece conexión con la base de datos SQLite."""
    try:
        conn = sqlite3.connect(DATABASE)
        return conn
    except sqlite3.Error as e:
        print(f"❌ Error al conectar a SQLite: {e}")
        return None

def initialize_database():
    """Verifica que la tabla de empleados existe."""
    conn = conectar()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS empleados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                telefono TEXT NOT NULL,
                fecha_ingreso DATE NOT NULL,
                salario REAL NOT NULL,
                estado TEXT NOT NULL DEFAULT 'activo'
            )
        """)
        conn.commit()
        print("✅ Base de datos SQLite verificada correctamente")
    except sqlite3.Error as e:
        print(f"❌ Error al inicializar base de datos: {e}")
    finally:
        conn.close()

def initialize_newtablecrud():
    """Verifica que la tabla NewTableCrud existe."""
    conn = conectar()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS NewTableCrud (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                estado TEXT NOT NULL DEFAULT 'activo',
                fecha_creacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                fecha_actualizacion DATETIME
            )
        """)
        conn.commit()
        print("✅ Tabla NewTableCrud verificada correctamente")
    except sqlite3.Error as e:
        print(f"❌ Error al inicializar NewTableCrud: {e}")
    finally:
        conn.close()
