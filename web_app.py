"""
Aplicación web CRUD de Empleados con Flask
"""
from flask import Flask, render_template, request, redirect, url_for, flash
from crud_operations import CRUDEmpleado
from config import verificar_conexion
from datetime import datetime, date
import re
import unicodedata

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # Cambia esto por una clave segura

ESTADOS_VALIDOS = ['Activo', 'Incapacitado', 'Vacaciones']


def normalizar_email_parte(texto):
    texto = unicodedata.normalize('NFKD', texto)
    texto = texto.encode('ascii', 'ignore').decode('ascii')
    texto = texto.lower().strip()
    return re.sub(r'[^a-z0-9]', '', texto)


def generar_email(nombre, apellido):
    return f"{normalizar_email_parte(nombre)}.{normalizar_email_parte(apellido)}@gmail.com"


def validar_fecha_ingreso(valor):
    try:
        fecha = datetime.strptime(valor, '%Y-%m-%d').date()
        return fecha >= date(2025, 1, 1), fecha
    except ValueError:
        return False, None


def validar_telefono(telefono):
    return bool(re.fullmatch(r'\d{10}', telefono))


def validar_nombre_o_apellido(valor):
    return bool(valor) and ' ' not in valor


@app.route('/')
def index():
    """Página principal: lista de empleados"""
    if not verificar_conexion():
        flash("Error de conexión a la base de datos. Verifica tu configuración.", "error")
        empleados = []
    else:
        empleados = CRUDEmpleado.leer_todos()
    return render_template('index.html', empleados=empleados)

@app.route('/crear', methods=['GET', 'POST'])
def crear():
    """Crear nuevo empleado"""
    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        apellido = request.form['apellido'].strip()
        email = request.form.get('email', '').strip()
        telefono = request.form.get('telefono', '').strip()
        fecha_ingreso_str = request.form.get('fecha_ingreso', '').strip()
        salario_str = request.form.get('salario', '').strip()
        estado = request.form.get('estado', '').strip()

        if not validar_nombre_o_apellido(nombre) or not validar_nombre_o_apellido(apellido):
            flash("Nombre y apellido deben ser de una sola palabra.", "error")
            return redirect(url_for('crear'))

        if not fecha_ingreso_str:
            flash("La fecha de ingreso es obligatoria.", "error")
            return redirect(url_for('crear'))

        valid_fecha, fecha_ingreso = validar_fecha_ingreso(fecha_ingreso_str)
        if not valid_fecha:
            flash("La fecha de ingreso debe ser a partir de 2025.", "error")
            return redirect(url_for('crear'))

        if estado not in ESTADOS_VALIDOS:
            flash("El estado seleccionado no es válido.", "error")
            return redirect(url_for('crear'))

        if not salario_str:
            flash("El salario es obligatorio.", "error")
            return redirect(url_for('crear'))

        try:
            salario = float(salario_str)
        except ValueError:
            flash("El salario debe ser un número válido.", "error")
            return redirect(url_for('crear'))

        if salario < 2000000 or salario >= 6000000:
            flash("El salario debe estar entre 2.000.000 y menos de 6.000.000.", "error")
            return redirect(url_for('crear'))

        if telefono and not validar_telefono(telefono):
            flash("El teléfono debe tener exactamente 10 dígitos.", "error")
            return redirect(url_for('crear'))

        if not email:
            email = generar_email(nombre, apellido)

        expected_email = generar_email(nombre, apellido)
        if email.lower() != expected_email.lower():
            flash(f"El email debe ser '{expected_email}'.", "error")
            return redirect(url_for('crear'))

        if CRUDEmpleado.crear_empleado(nombre, apellido, email, telefono, fecha_ingreso, salario, estado):
            flash("Empleado creado exitosamente.", "success")
            return redirect(url_for('index'))
        else:
            flash("Error al crear empleado.", "error")
            return redirect(url_for('crear'))

    return render_template('crear.html')

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    """Buscar empleado por ID"""
    empleado = None
    if request.method == 'POST':
        if not verificar_conexion():
            flash("Error de conexión a la base de datos. Verifica tu configuración.", "error")
            return render_template('buscar.html', empleado=empleado)

        try:
            id_emp = int(request.form['id'])
            empleado = CRUDEmpleado.leer_por_id(id_emp)
            if not empleado:
                flash(f"No se encontró empleado con ID {id_emp}.", "warning")
            elif empleado[7] == 'Eliminado':
                empleado = None
                flash(f"El empleado con ID {id_emp} está eliminado.", "warning")
        except ValueError:
            flash("ID inválido.", "error")
    return render_template('buscar.html', empleado=empleado)

@app.route('/editar/<int:id_emp>', methods=['GET', 'POST'])
def editar(id_emp):
    """Editar empleado"""
    empleado = CRUDEmpleado.leer_por_id(id_emp)
    if not empleado or empleado[7] == 'Eliminado':
        flash("Empleado no encontrado o eliminado.", "error")
        return redirect(url_for('index'))

    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        apellido = request.form['apellido'].strip()
        email = request.form.get('email', '').strip()
        telefono = request.form.get('telefono', '').strip()
        fecha_ingreso_str = request.form.get('fecha_ingreso', '').strip()
        salario_str = request.form.get('salario', '').strip()
        estado = request.form.get('estado', '').strip()

        if not validar_nombre_o_apellido(nombre) or not validar_nombre_o_apellido(apellido):
            flash("Nombre y apellido deben ser de una sola palabra.", "error")
            return redirect(url_for('editar', id_emp=id_emp))

        if not fecha_ingreso_str:
            flash("La fecha de ingreso es obligatoria.", "error")
            return redirect(url_for('editar', id_emp=id_emp))

        valid_fecha, fecha_ingreso = validar_fecha_ingreso(fecha_ingreso_str)
        if not valid_fecha:
            flash("La fecha de ingreso debe ser a partir de 2025.", "error")
            return redirect(url_for('editar', id_emp=id_emp))

        if estado not in ESTADOS_VALIDOS:
            flash("El estado seleccionado no es válido.", "error")
            return redirect(url_for('editar', id_emp=id_emp))

        if not salario_str:
            flash("El salario es obligatorio.", "error")
            return redirect(url_for('editar', id_emp=id_emp))

        try:
            salario = float(salario_str)
        except ValueError:
            flash("El salario debe ser un número válido.", "error")
            return redirect(url_for('editar', id_emp=id_emp))

        if salario < 2000000 or salario >= 6000000:
            flash("El salario debe estar entre 2.000.000 y menos de 6.000.000.", "error")
            return redirect(url_for('editar', id_emp=id_emp))

        if telefono and not validar_telefono(telefono):
            flash("El teléfono debe tener exactamente 10 dígitos.", "error")
            return redirect(url_for('editar', id_emp=id_emp))

        if not email:
            email = generar_email(nombre, apellido)

        expected_email = generar_email(nombre, apellido)
        if email.lower() != expected_email.lower():
            flash(f"El email debe ser '{expected_email}'.", "error")
            return redirect(url_for('editar', id_emp=id_emp))

        if CRUDEmpleado.actualizar_empleado(id_emp, nombre, apellido, email, telefono, fecha_ingreso, salario, estado):
            flash("Empleado actualizado exitosamente.", "success")
            return redirect(url_for('index'))
        else:
            flash("Error al actualizar empleado.", "error")

    return render_template('editar.html', empleado=empleado)

@app.route('/eliminar/<int:id_emp>', methods=['POST'])
def eliminar(id_emp):
    """Eliminar empleado"""
    if CRUDEmpleado.eliminar_empleado(id_emp):
        flash("Empleado eliminado exitosamente.", "success")
    else:
        flash("Error al eliminar empleado.", "error")
    return redirect(url_for('index'))

@app.route('/restaurar/<int:id_emp>', methods=['POST'])
def restaurar(id_emp):
    """Restaurar empleado eliminado"""
    if CRUDEmpleado.restaurar_empleado(id_emp):
        flash("Empleado restaurado exitosamente.", "success")
    else:
        flash("Error al restaurar empleado.", "error")
    return redirect(url_for('eliminados'))

@app.route('/restaurar-todos', methods=['POST'])
def restaurar_todos():
    """Restaurar todos los empleados eliminados"""
    if CRUDEmpleado.restaurar_todos():
        flash("Todos los empleados eliminados fueron restaurados.", "success")
    else:
        flash("Error al restaurar empleados eliminados.", "error")
    return redirect(url_for('eliminados'))

@app.route('/eliminados')
def eliminados():
    """Página de empleados eliminados"""
    if not verificar_conexion():
        flash("Error de conexión a la base de datos. Verifica tu configuración.", "error")
        empleados_eliminados = []
    else:
        empleados_eliminados = CRUDEmpleado.leer_eliminados()
    return render_template('eliminados.html', empleados_eliminados=empleados_eliminados)

if __name__ == '__main__':
    app.run(debug=True)