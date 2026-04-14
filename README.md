# 🚀 CRUD DE EMPLEADOS - PYTHON + SQLite

Aplicación completa para gestionar empleados con **3 interfaces diferentes** (Gráfica, Web, CLI). Ahora utiliza **SQLite local**, sin necesidad de instalar SQL Server.

## ✨ Novedades - Eliminación en Búsqueda y Edición

✅ **Botón de eliminar** en la búsqueda web  
✅ **Botón de eliminar** en la edición web  
✅ **Botón de eliminar** en la GUI (Tkinter)  
✅ **Confirmación** antes de eliminar  
✅ **Datos de muestra** cargados automáticamente la primera vez  

---

## 📋 Requisitos

- Python 3.8+
- Flask (para interfaz web, opcional)

## 📥 Instalación Rápida

### Paso 1: Instalar dependencias
```bash
pip install -r requirements.txt
```

### Paso 2: Ejecutar la aplicación
```bash
python app.py
```

### Paso 3: Abrir la interfaz web
```bash
python web_app.py
```

Accede a: http://localhost:5000

---

## ▶️ Formas de Ejecutar

### 🎯 Opción 1: Menú Launcher (Recomendado)
```bash
python app.py
# O haz doble clic en: run.bat
```
Elige entre interfaz gráfica o CLI

### 🖥️ Opción 2: Interfaz Gráfica (Tkinter)
```bash
python gui.py
```
**Características:**
- ➕ Crear nuevo empleado
- 📋 Ver tabla de empleados
- 🔍 Buscar en tiempo real
- ✏️ Editar información
- ❌ Eliminar con confirmación
- 👁️ Ver detalles completos

### 🌐 Opción 3: Interfaz Web (Flask)
```bash
python web_app.py
```
Accede a: http://localhost:5000

**Rutas:**
- `/` - Lista de empleados
- `/crear` - Crear nuevo
- `/buscar` - Buscar y **eliminar**
- `/editar/<id>` - Editar y **eliminar**

### 💻 Opción 4: Línea de Comandos (CLI)
```bash
python main.py
```
Menú interactivo con todas las opciones

---

## 🗑️ Cómo Usar la Eliminación

### En la Interfaz Gráfica:
1. Selecciona un empleado en la tabla
2. Haz clic en **"❌ Eliminar"**
3. Confirma la acción

### En la Búsqueda Web:
1. Ingresa el ID del empleado
2. Haz clic en **"Buscar"**
3. Haz clic en **"🗑️ Eliminar"** (nuevo botón)
4. Confirma

### En la Edición Web:
1. Accede a un empleado
2. Haz clic en **"🗑️ Eliminar"** (nuevo botón)
3. Confirma

---

## 📊 10 Empleados Precargados

| ID | Nombre | Apellido | Email | Estado | Salario |
|---|---|---|---|---|---|
| 1 | Juan | Perez | juan.perez@gmail.com | Activo | $2,500,000 |
| 2 | María | Gomez | maria.gomez@gmail.com | Activo | $4,200,000 |
| 3 | Luis | Rojas | luis.rojas@gmail.com | Incapacitado | $3,800,000 |
| 4 | Carlos | Martinez | carlos.martinez@gmail.com | Activo | $3,200,000 |
| 5 | Ana | Sanchez | ana.sanchez@gmail.com | Vacaciones | $2,800,000 |
| 6 | Fernando | Garcia | fernando.garcia@gmail.com | Activo | $5,200,000 |
| 7 | Isabel | Lopez | isabel.lopez@gmail.com | Activo | $3,600,000 |
| 8 | Roberto | Hernandez | roberto.hernandez@gmail.com | Activo | $4,800,000 |
| 9 | Patricia | Castillo | patricia.castillo@gmail.com | Incapacitado | $2,900,000 |
| 10 | Miguel | Vargas | miguel.vargas@gmail.com | Activo | $3,500,000 |

---

## 📁 Estructura de Archivos

```
crud.prueba IA/
├── app.py                                  # Launcher
├── gui.py                                  # GUI Tkinter
├── main.py                                 # CLI
├── web_app.py                              # Web Flask
├── config.py                               # Configuración SQLite
├── crud_operations.py                      # Operaciones CRUD
├── empleados.db                            # Base de datos SQLite
├── requirements.txt                        # Dependencias
├── README.md                               # Este archivo
├── templates/
│   ├── index.html          # Lista web
│   ├── crear.html          # Crear web
│   ├── buscar.html         # Buscar + ELIMINAR ✨
│   └── editar.html         # Editar + ELIMINAR ✨
└── ejemplos.py             # Código de ejemplo
```

---

## 🔧 Funciones CRUD

### `CRUDEmpleado.crear_empleado()`
Crear nuevo empleado con validaciones

### `CRUDEmpleado.leer_todos()`
Obtener lista de todos los empleados

### `CRUDEmpleado.leer_por_id(id)`
Buscar un empleado específico

### `CRUDEmpleado.actualizar_empleado()`
Editar información del empleado

### `CRUDEmpleado.eliminar_empleado(id)`
Eliminar empleado (con confirmación)

---

## ✅ Validaciones

- **ID**: Generado automáticamente (1, 2, 3...)
- **Nombre/Apellido**: Una palabra, sin espacios
- **Email**: Formato nombre.apellido@gmail.com
- **Teléfono**: Exactamente 10 dígitos
- **Fecha Ingreso**: A partir de 2025-01-01
- **Salario**: Entre $2,000,000 y $5,999,999
- **Estado**: Activo, Incapacitado o Vacaciones

---

## 🌳 Estructura de Carpetas

```
crud.prueba IA/
├── app.py                                  # Launcher
├── gui.py                                  # GUI Tkinter
├── main.py                                 # CLI
├── web_app.py                              # Web Flask
├── config.py                               # Configuración BD
├── crud_operations.py                      # Operaciones CRUD
├── empleados.db                            # Base de datos SQLite
├── requirements.txt                        # Dependencias
├── README.md                               # Este archivo
├── templates/
│   ├── index.html          # Lista web
│   ├── crear.html          # Crear web
│   ├── buscar.html         # Buscar + ELIMINAR ✨
│   └── editar.html         # Editar + ELIMINAR ✨
└── ejemplos.py             # Código de ejemplo
```


---

## 🎨 Interfaz Visual

### GUI (Tkinter)
- Tabla con scroll
- Búsqueda en tiempo real
- Formularios modales
- Botones con colores
- Confirmaciones

### Web (Flask + Bootstrap)
- Diseño moderno
- Gradientes
- Responsive
- Íconos
- Animaciones

### CLI
- Menú interactivo
- Validación de entrada
- Formateo de salida
- Manejo de errores

---

## 🚀 Próximos Pasos

1. ✅ Ejecuta `python app.py`
2. ✅ Elige interfaz (GUI o CLI)
3. ✅ Prueba crear, buscar, editar y eliminar
4. ✅ ¡Explora los empleados!

---

## ❓ Troubleshooting

**Error: "No module named 'flask'"**
- Ejecuta `pip install -r requirements.txt`

**Error: "Cannot connect to database"**
- La base de datos SQLite se crea automáticamente
- Verifica que tengas permisos de escritura en la carpeta

**Error: "Table does not exist"**
- Borra `empleados.db` y ejecuta de nuevo para recrear la tabla

## 📝 Ejemplo de uso

```python
# Crear empleado
from crud_operations import CRUDEmpleado
CRUDEmpleado.crear_empleado('Juan', 'Pérez', 'juan.perez@gmail.com', '3123456789', '2025-01-15', 2500000, 'Activo')

# Ver todos
empleados = CRUDEmpleado.leer_todos()

# Actualizar
CRUDEmpleado.actualizar_empleado(1, 'Carlos', 'López', 'carlos.lopez@gmail.com', '3123456789', '2025-01-15', 3000000, 'Activo')

# Eliminar
CRUDEmpleado.eliminar_empleado(1)
```

## ✅ Pruebas

Ejecuta los tests unitarios:
```bash
python test_crud.py
```

O usa los ejemplos avanzados:
```bash
python ejemplos.py
```
(Descomenta los ejemplos que desees ejecutar)

## 📞 Soporte

Para problemas, revisa:
1. Que Python 3.8+ esté instalado
2. Que las dependencias estén instaladas (`pip install -r requirements.txt`)
3. Que tengas permisos de escritura en la carpeta del proyecto
4. Los logs de la aplicación (ejecuta con `python web_app.py` para ver errores)

