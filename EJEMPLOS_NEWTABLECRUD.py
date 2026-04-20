"""
Ejemplos de configuración y cómo usar NewTableCrud
"""

# ============================================================================
# EJEMPLO 1: Conectarse a SQL Server Express LOCAL
# ============================================================================

# Archivo: .env
"""
SQL_SERVER=localhost\SQLEXPRESS
SQL_DATABASE=LC-PRU-NephroCalc
SQL_USER=
SQL_PASSWORD=
"""

# ============================================================================
# EJEMPLO 2: Conectarse a SQL Server en Red (con credenciales)
# ============================================================================

# Archivo: .env
"""
SQL_SERVER=TEST\CLBSTEST01
SQL_DATABASE=LC-PRU-NephroCalc
SQL_USER=subd-pru-NephroCalc
SQL_PASSWORD=56X&C31Wdq*E
"""

# ============================================================================
# EJEMPLO 3: Crear registros programáticamente
# ============================================================================

from crud_newtablecrud import CRUDNewTableCrud
from config import initialize_newtablecrud

# Paso 1: Inicializar la tabla (solo la primera vez)
initialize_newtablecrud()

# Paso 2: Crear registros
CRUDNewTableCrud.crear_registro(
    nombre="Mi Primer Registro",
    descripcion="Este es mi primer registro en NewTableCrud",
    estado="activo"
)

CRUDNewTableCrud.crear_registro(
    nombre="Segundo Registro",
    descripcion="Descripción del segundo registro",
    estado="activo"
)

# Paso 3: Leer registros
registros = CRUDNewTableCrud.leer_todos()
for reg in registros:
    print(f"ID: {reg[0]}, Nombre: {reg[1]}, Estado: {reg[3]}")

# Paso 4: Actualizar un registro
CRUDNewTableCrud.actualizar_registro(
    id_registro=1,
    nombre="Registro Actualizado",
    descripcion="Nueva descripción",
    estado="activo"
)

# Paso 5: Eliminar (soft delete)
CRUDNewTableCrud.eliminar_registro(id_registro=2)

# Paso 6: Ver eliminados
eliminados = CRUDNewTableCrud.leer_eliminados()
for reg in eliminados:
    print(f"ID: {reg[0]}, Nombre: {reg[1]}, Eliminado")

# Paso 7: Restaurar
CRUDNewTableCrud.restaurar_registro(id_registro=2)

# ============================================================================
# EJEMPLO 4: Integrar con Flask (web_app.py)
# ============================================================================

from flask import Flask, render_template, request, jsonify
from crud_newtablecrud import CRUDNewTableCrud
from datetime import datetime

app = Flask(__name__)

@app.route('/api/registros', methods=['GET'])
def obtener_registros():
    """Obtiene todos los registros en formato JSON"""
    registros = CRUDNewTableCrud.leer_todos()
    return jsonify(registros)

@app.route('/api/registros', methods=['POST'])
def crear_registro():
    """Crea un nuevo registro"""
    data = request.get_json()
    exito = CRUDNewTableCrud.crear_registro(
        nombre=data.get('nombre'),
        descripcion=data.get('descripcion'),
        estado=data.get('estado', 'activo')
    )
    return jsonify({'exito': exito})

@app.route('/api/registros/<int:id_registro>', methods=['GET'])
def obtener_registro(id_registro):
    """Obtiene un registro específico"""
    registro = CRUDNewTableCrud.leer_por_id(id_registro)
    return jsonify(registro) if registro else jsonify({'error': 'No encontrado'}), 404

@app.route('/api/registros/<int:id_registro>', methods=['PUT'])
def actualizar_registro(id_registro):
    """Actualiza un registro"""
    data = request.get_json()
    exito = CRUDNewTableCrud.actualizar_registro(
        id_registro=id_registro,
        nombre=data.get('nombre'),
        descripcion=data.get('descripcion'),
        estado=data.get('estado')
    )
    return jsonify({'exito': exito})

@app.route('/api/registros/<int:id_registro>', methods=['DELETE'])
def eliminar_registro(id_registro):
    """Elimina un registro"""
    exito = CRUDNewTableCrud.eliminar_registro(id_registro)
    return jsonify({'exito': exito})

# ============================================================================
# EJEMPLO 5: Usar en una CLI (línea de comandos)
# ============================================================================

import sys
from config import initialize_newtablecrud

def main():
    if len(sys.argv) < 2:
        print("Uso: python crud_cli.py [crear|leer|actualizar|eliminar] [args...]")
        return
    
    comando = sys.argv[1].lower()
    initialize_newtablecrud()
    
    if comando == 'crear':
        nombre = sys.argv[2]
        descripcion = sys.argv[3]
        CRUDNewTableCrud.crear_registro(nombre, descripcion)
    
    elif comando == 'leer':
        registros = CRUDNewTableCrud.leer_todos()
        for reg in registros:
            print(f"{reg[0]}: {reg[1]} - {reg[2]}")
    
    elif comando == 'actualizar':
        id_reg = int(sys.argv[2])
        nombre = sys.argv[3]
        descripcion = sys.argv[4]
        CRUDNewTableCrud.actualizar_registro(id_reg, nombre, descripcion, 'activo')
    
    elif comando == 'eliminar':
        id_reg = int(sys.argv[2])
        CRUDNewTableCrud.eliminar_registro(id_reg)

if __name__ == '__main__':
    main()

# ============================================================================
# EJEMPLO 6: Ejecutar desde CLI
# ============================================================================

# Crear registro
# python crud_cli.py crear "Mi Registro" "Descripción"

# Listar registros
# python crud_cli.py leer

# Actualizar registro
# python crud_cli.py actualizar 1 "Nuevo Nombre" "Nueva Descripción"

# Eliminar registro
# python crud_cli.py eliminar 1
