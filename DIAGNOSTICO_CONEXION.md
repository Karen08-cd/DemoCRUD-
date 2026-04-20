# 🔧 Diagnóstico y Solución de Conexión a SQL Server

## Problema Identificado
```
❌ El servidor TEST\CLBSTEST01 no es accesible
   Error: getaddrinfo failed (No se puede resolver el nombre del servidor)
```

## Posibles Causas y Soluciones

### 1️⃣ El servidor no es accesible en la red
**Síntomas:**
- Error "getaddrinfo failed"
- No se puede contactar al servidor

**Soluciones:**
```bash
# Verifica si el servidor es alcanzable
ping TEST
ping CLBSTEST01

# Verifica si el puerto 1433 está abierto
telnet TEST 1433
```

**Si no funciona:**
- Verifica la conectividad de red
- Comprueba si el firewall bloquea la conexión
- Pregunta al administrador de TI si el servidor está disponible

### 2️⃣ Usar dirección IP en lugar de nombre
Si el servidor tiene una dirección IP estática, actualiza `.env`:

```env
SQL_SERVER=192.168.X.X\CLBSTEST01
SQL_DATABASE=LC-PRU-NephroCalc
SQL_USER=
SQL_PASSWORD=
```

### 3️⃣ Si usas SQL Server LOCAL

Si tienes SQL Server Express instalado localmente, usa:

```env
SQL_SERVER=localhost\SQLEXPRESS
SQL_DATABASE=LC-PRU-NephroCalc
SQL_USER=  
SQL_PASSWORD=  
```

**Nota:** Deja USER y PASSWORD vacíos para usar autenticación integrada de Windows.

### 4️⃣ Alternativa: Usar Azure o SQL Server en la nube

Si necesitas una base de datos remota, puedes usar:
- **Azure SQL Database**: Más confiable para conexiones remotas
- **SQL Server en EC2/VM**: Más control sobre la instancia

## Cómo Verificar la Conexión

### Opción A: Desde PowerShell
```powershell
# Verificar acceso al servidor
ping TEST
ping CLBSTEST01

# Probar puerto
Test-NetConnection -ComputerName TEST -Port 1433
```

### Opción C: Ejecutar diagnóstico mejorado
```bash
python diagnostic_server.py
```

## Próximos Pasos

1. **Verificar servidor:** 
   - ¿El servidor está encendido?
   - ¿Es accesible desde tu red?
   - ¿Son correctas las credenciales?

2. **Actualizar .env** con la información correcta:
   ```env
   SQL_SERVER=
   SQL_DATABASE=
   SQL_USER=<usuario>
   SQL_PASSWORD=<contraseña>
   ```

3. **Reintentar la conexión:**
   ```bash
   python test_newtablecrud.py
   ```

## Opciones de Configuración

### Para SQL Server Express (Local)
```env
SQL_SERVER=localhost\SQLEXPRESS
SQL_DATABASE=LC-PRU-NephroCalc
SQL_USER=
SQL_PASSWORD=
```

### Para SQL Server en Red
```env
SQL_SERVER=SERVIDOR_IP\INSTANCIA
SQL_DATABASE=LC-PRU-NephroCalc
SQL_USER=usuario
SQL_PASSWORD=contraseña
```

### Para SQL Server con Autenticación Windows
```env
SQL_SERVER=SERVIDOR\INSTANCIA
SQL_DATABASE=LC-PRU-NephroCalc
SQL_USER=
SQL_PASSWORD=
```

## Contacta al Administrador

Si ninguna solución funciona, proporciona al administrador de TI esta información:

```
Servidor intentado: TEST\CLBSTEST01
Base de datos: LC-PRU-NephroCalc
Usuario: subd-pru-NephroCalc
Error: A network-related or instance-specific error has occurred
```

