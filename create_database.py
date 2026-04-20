"""
Script para crear la base de datos LC-PRU-NephroCalc en SQL Server Express
Ejecutar después de instalar SQL Server Express
"""
import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

def crear_base_datos():
    """Crea la base de datos y tabla de empleados"""
    try:
        # Conectar al master para crear la base de datos
        conn_str = "DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost\\SQLEXPRESS;DATABASE=master;Trusted_Connection=yes"
        print("Conectando a SQL Server Express...")

        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Crear la base de datos si no existe
        print("Creando base de datos LC-PRU-NephroCalc...")
        cursor.execute("""
            IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'LC-PRU-NephroCalc')
            BEGIN
                CREATE DATABASE [LC-PRU-NephroCalc]
                PRINT 'Base de datos LC-PRU-NephroCalc creada exitosamente'
            END
            ELSE
            BEGIN
                PRINT 'La base de datos LC-PRU-NephroCalc ya existe'
            END
        """)
        conn.commit()

        # Cambiar a la nueva base de datos
        conn.close()
        conn_str_db = "DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost\\SQLEXPRESS;DATABASE=LC-PRU-NephroCalc;Trusted_Connection=yes"
        conn = pyodbc.connect(conn_str_db)
        cursor = conn.cursor()

        # Crear tabla de empleados
        print("Creando tabla empleados...")
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='empleados' AND xtype='U')
            BEGIN
                CREATE TABLE empleados (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    nombre NVARCHAR(100) NOT NULL,
                    apellido NVARCHAR(100) NOT NULL,
                    email NVARCHAR(255) NOT NULL UNIQUE,
                    telefono NVARCHAR(10) NOT NULL CHECK (LEN(telefono) = 10 AND telefono LIKE '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),
                    fecha_ingreso DATE NOT NULL,
                    salario DECIMAL(10,2) NOT NULL,
                    estado NVARCHAR(20) NOT NULL DEFAULT 'activo'
                )
                PRINT 'Tabla empleados creada exitosamente'
            END
            ELSE
            BEGIN
                PRINT 'La tabla empleados ya existe'
            END
        """)
        conn.commit()

        print("✅ Base de datos y tabla creadas exitosamente!")
        print("\nAhora puedes ejecutar tu aplicación CRUD.")
        print("Prueba con: python app.py")

    except pyodbc.Error as e:
        print(f"❌ Error: {e}")
        print("\nAsegúrate de que:")
        print("1. SQL Server Express esté instalado y ejecutándose")
        print("2. Los servicios de SQL Server estén activos")
        print("3. Tienes permisos de administrador")

    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    crear_base_datos()
