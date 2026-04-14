"""
Configuracion de conexion a SQLite local.
"""
from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / 'empleados.db'


def conectar():
    """Establece conexion con la base de datos SQLite local."""
    conexion = sqlite3.connect(DB_PATH)
    conexion.row_factory = sqlite3.Row
    return conexion


def initialize_database():
    """Crea la tabla de empleados y carga datos de muestra si es necesario."""
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS empleados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL CHECK (instr(nombre, ' ') = 0),
                apellido TEXT NOT NULL CHECK (instr(apellido, ' ') = 0),
                email TEXT NOT NULL CHECK (LOWER(email) = LOWER(nombre || '.' || apellido || '@gmail.com')),
                telefono TEXT NOT NULL CHECK (length(telefono) = 10 AND telefono GLOB '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),
                fecha_ingreso DATE NOT NULL CHECK (fecha_ingreso >= '2025-01-01'),
                salario REAL NOT NULL CHECK (salario >= 2000000 AND salario < 6000000),
                estado TEXT NOT NULL CHECK (estado IN ('Activo', 'Incapacitado', 'Vacaciones'))
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS deleted_empleados (
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL CHECK (instr(nombre, ' ') = 0),
                apellido TEXT NOT NULL CHECK (instr(apellido, ' ') = 0),
                email TEXT NOT NULL CHECK (LOWER(email) = LOWER(nombre || '.' || apellido || '@gmail.com')),
                telefono TEXT NOT NULL CHECK (length(telefono) = 10 AND telefono GLOB '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),
                fecha_ingreso DATE NOT NULL CHECK (fecha_ingreso >= '2025-01-01'),
                salario REAL NOT NULL CHECK (salario >= 2000000 AND salario < 6000000),
                estado TEXT NOT NULL
            )
        """)

        conexion.commit()

        # Migrar empleados viejos que quedaron con estado Eliminado a la tabla de eliminados
        cursor.execute("SELECT id, nombre, apellido, email, telefono, fecha_ingreso, salario, estado FROM empleados WHERE estado = ?", ('Eliminado',))
        empleados_eliminados = cursor.fetchall()
        if empleados_eliminados:
            cursor.executemany(
                'INSERT OR IGNORE INTO deleted_empleados (id, nombre, apellido, email, telefono, fecha_ingreso, salario, estado) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                [(emp[0], emp[1], emp[2], emp[3], emp[4], emp[5], emp[6], emp[7]) for emp in empleados_eliminados]
            )
            cursor.execute('DELETE FROM empleados WHERE estado = ?', ('Eliminado',))
            conexion.commit()
        conexion.commit()

        cursor.execute('SELECT COUNT(*) FROM empleados')
        total = cursor.fetchone()[0]
        if total == 0:
            muestra = [
                ('Juan', 'Perez', 'juan.perez@gmail.com', '3123456789', '2025-01-15', 2500000.00, 'Activo'),
                ('Maria', 'Gomez', 'maria.gomez@gmail.com', '3109876543', '2025-02-20', 4200000.00, 'Activo'),
                ('Luis', 'Rojas', 'luis.rojas@gmail.com', '3001234567', '2025-03-10', 3800000.00, 'Incapacitado'),
                ('Carlos', 'Martinez', 'carlos.martinez@gmail.com', '3145678901', '2025-04-05', 3200000.00, 'Activo'),
                ('Ana', 'Sanchez', 'ana.sanchez@gmail.com', '3167890123', '2025-05-12', 2800000.00, 'Vacaciones'),
                ('Fernando', 'Garcia', 'fernando.garcia@gmail.com', '3189012345', '2025-06-18', 5200000.00, 'Activo'),
                ('Isabel', 'Lopez', 'isabel.lopez@gmail.com', '3021234567', '2025-07-22', 3600000.00, 'Activo'),
                ('Roberto', 'Hernandez', 'roberto.hernandez@gmail.com', '3043456789', '2025-08-30', 4800000.00, 'Activo'),
                ('Patricia', 'Castillo', 'patricia.castillo@gmail.com', '3065678901', '2025-09-14', 2900000.00, 'Incapacitado'),
                ('Miguel', 'Vargas', 'miguel.vargas@gmail.com', '3087890123', '2025-10-08', 3500000.00, 'Activo')
            ]
            cursor.executemany(
                'INSERT INTO empleados (nombre, apellido, email, telefono, fecha_ingreso, salario, estado) VALUES (?, ?, ?, ?, ?, ?, ?)',
                muestra
            )
            conexion.commit()
    finally:
        conexion.close()


def verificar_conexion():
    """Verifica si la conexion es exitosa."""
    conexion = conectar()
    if conexion:
        print(f'✅ Conexion exitosa a SQLite: {DB_PATH}')
        conexion.close()
        return True
    print('❌ No se pudo establecer conexion con SQLite')
    return False


initialize_database()
