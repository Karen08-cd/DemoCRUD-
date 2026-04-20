# 🛠️ Solución: SQL Server Express No Está Disponible

## Problema
```
❌ No se puede conectar a localhost\SQLEXPRESS
   El servidor no está corriendo o no es accesible
```

## Solución 1: Verificar si SQL Server está instalado (Rápido)

### En PowerShell:
```powershell
# Buscar servicios de SQL Server
Get-Service | Where-Object {$_.Name -like "*SQL*"}

# Resultado esperado:
# Status   Name                DisplayName
# ------   ----                -----------
# Running  MSSQLSERVER         SQL Server (SQLEXPRESS)
```

Si no ves ningún servicio SQL Server, **necesitas instalarlo**.

---

## Solución 2: Iniciar SQL Server Express (Si ya está instalado)

### Opción A: Desde PowerShell (Como Administrador)
```powershell
# Abre PowerShell como Administrador y ejecuta:
Start-Service -Name "MSSQL$SQLEXPRESS"

# Luego verifica:
Get-Service -Name "MSSQL$SQLEXPRESS"
```

### Opción B: Desde Services.msc
1. Presiona `Win + R`
2. Escribe: `services.msc`
3. Busca: `SQL Server (SQLEXPRESS)`
4. Haz clic derecho → **Start**
5. Verifica que el estado cambie a **Running**

### Opción C: Desde SQL Server Configuration Manager
1. Presiona `Win + R`
2. Escribe: `SQLServerManager15.msc` (o la versión que tengas)
3. Expande: **SQL Server Services**
4. Haz clic derecho en `SQL Server (SQLEXPRESS)` → **Start**

---

## Solución 3: Instalar SQL Server Express (Si no está instalado)

### Instalador disponible:
En tu carpeta hay estos scripts de instalación:
- `install_sql_express.bat`
- `install_sql_express_silent.bat`
- `install_sql_simple.bat`

### Ejecutar instalación:
```bash
# Abre PowerShell como Administrador y ejecuta:
cd "c:\Users\kgonzalezt\Downloads\crud.prueba IA"
.\install_sql_simple.bat
```

O simplemente haz doble clic en el archivo `.bat`

---

## Solución 4: Verificar Conexión Después

Una vez que SQL Server esté ejecutándose:

```powershell
# Abre SQL Server Management Studio (SSMS)
# O verifica la conexión con:
python test_newtablecrud.py
```

---

## Verificar Paso a Paso

### 1️⃣ ¿SQL Server Express está instalado?
```powershell
Get-Service | Where-Object {$_.Name -like "*SQL*"} | Select-Object Name, Status
```

**Si ves `MSSQL$SQLEXPRESS` → Está instalado**
**Si NO ves nada → Necesitas instalarlo**

### 2️⃣ ¿El servicio está corriendo?
```powershell
Get-Service -Name "MSSQL$SQLEXPRESS" | Select-Object Status
```

**Si ves `Running` → ✅ Todo bien**
**Si ves `Stopped` → Inicia el servicio**

### 3️⃣ ¿Puedo conectar?
```powershell
python diagnostic.py
```

---

## Comandos Rápidos

```powershell
# Abrir PowerShell como Administrador
# Luego ejecuta uno de estos:

# Ver estado
Get-Service -Name "MSSQL$SQLEXPRESS"

# Iniciar
Start-Service -Name "MSSQL$SQLEXPRESS"

# Detener
Stop-Service -Name "MSSQL$SQLEXPRESS"

# Reiniciar
Restart-Service -Name "MSSQL$SQLEXPRESS"
```

---

## Alternativa: Usar SQLite

Si no quieres lidiar con SQL Server, puedo ayudarte a migrar a **SQLite** (más simple):

```env
DATABASE_TYPE=sqlite
DATABASE_FILE=database.db
```

Mucho más fácil de instalar y usar para desarrollo.

---

## Próximos Pasos

1. ✅ Verifica si SQL Server está instalado
2. ✅ Si no está instalado, corre `install_sql_simple.bat`
3. ✅ Inicia el servicio si está parado
4. ✅ Ejecuta: `python diagnostic.py`
5. ✅ Si todo está bien, ejecuta: `python test_newtablecrud.py`

¿Necesitas ayuda con alguno de estos pasos?
