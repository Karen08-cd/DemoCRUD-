# 📋 Conexión a Base de Datos NewTableCrud

## Resumen de cambios realizados

### 1. Actualización de `config.py`
- ✅ Ahora lee las variables de entorno del archivo `.env`
- ✅ Soporta autenticación SQL Server (con usuario y contraseña)
- ✅ Soporta autenticación integrada de Windows (alternativa)
- ✅ Nueva función `initialize_newtablecrud()` para crear la tabla en esquema `dbo`

### 2. Nuevo archivo: `crud_newtablecrud.py`
Clase `CRUDNewTableCrud` con operaciones completas:

#### Métodos disponibles:
- **`crear_registro(nombre, descripcion, estado='activo')`** - Crea un nuevo registro
- **`leer_todos()`** - Obtiene todos los registros activos
- **`leer_por_id(id_registro)`** - Obtiene un registro específico
- **`actualizar_registro(id, nombre, descripcion, estado)`** - Actualiza un registro
- **`eliminar_registro(id_registro)`** - Marca como eliminado (soft delete)
- **`leer_eliminados()`** - Obtiene registros eliminados
- **`restaurar_registro(id_registro)`** - Restaura un registro eliminado

### 3. Script de prueba: `test_newtablecrud.py`
Script completo con todas las pruebas de conexión y CRUD.

## 🚀 Cómo usar

### Paso 1: Verificar el archivo `.env`
Asegúrate de que tu archivo `.env` tiene las credenciales correctas:
```
SQL_SERVER=
SQL_DATABASE=
SQL_USER=
SQL_PASSWORD=
```

### Paso 2: Ejecutar las pruebas
```bash
python test_newtablecrud.py
```

### Paso 3: Usar en tu código
```python
from crud_newtablecrud import CRUDNewTableCrud

# Crear un registro
CRUDNewTableCrud.crear_registro("Mi Registro", "Descripción", "activo")

# Leer todos
registros = CRUDNewTableCrud.leer_todos()

# Actualizar
CRUDNewTableCrud.actualizar_registro(1, "Nuevo nombre", "Nueva desc", "activo")

# Eliminar
CRUDNewTableCrud.eliminar_registro(1)
```

## 📊 Estructura de la tabla NewTableCrud

```sql
CREATE TABLE [dbo].[NewTableCrud] (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre NVARCHAR(100) NOT NULL,
    descripcion NVARCHAR(500),
    estado NVARCHAR(50) NOT NULL DEFAULT 'activo',
    fecha_creacion DATETIME NOT NULL DEFAULT GETDATE(),
    fecha_actualizacion DATETIME
)
```

## ⚙️ Configuración de conexión

La conexión se realiza automáticamente usando:
- **Servidor**: `TEST\CLBSTEST01` (desde `.env`)
- **Base de datos**:  (desde `.env`)
- **Usuario** (desde `.env`)
- **Contraseña**: Cargada del archivo `.env`
- **Esquema**: `dbo`
- **Tabla**: `NewTableCrud`

## ✅ Próximos pasos

1. Ejecuta `test_newtablecrud.py` para verificar la conexión
2. Si la prueba es exitosa, usa `CRUDNewTableCrud` en tus aplicaciones
3. Integra con `web_app.py` si necesitas una interfaz web

