from config import conectar

if __name__ == '__main__':
    conexion = conectar()
    if not conexion:
        print('ERROR: No se pudo conectar a la base de datos.')
        exit(1)

    try:
        print('Conectado a SQL Server exitosamente.')
        cursor = conexion.cursor()

        cursor.execute('SELECT COUNT(*) FROM empleados')
        total = cursor.fetchone()[0]
        print(f'Total de registros en empleados: {total}')

        cursor.execute('SELECT * FROM empleados WHERE id = 1')
        fila = cursor.fetchone()
        if fila:
            print('Registro ID 1 encontrado:')
            print(dict(fila))
        else:
            print('Registro ID 1 NO encontrado.')
    except Exception as e:
        print('ERROR durante la verificación:', e)
    finally:
        conexion.close()