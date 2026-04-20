"""
Script para verificar drivers ODBC disponibles en el sistema.
"""
import pyodbc

print("=" * 60)
print("Drivers ODBC disponibles en tu sistema:")
print("=" * 60)

drivers = pyodbc.drivers()
for driver in drivers:
    print(f"✅ {driver}")

print("\n" + "=" * 60)
print("Recomendaciones:")
print("=" * 60)

# Detecta qué drivers hay disponibles
has_driver_18 = any("ODBC Driver 18" in d for d in drivers)
has_driver_17 = any("ODBC Driver 17" in d for d in drivers)
has_native_client = any("SQL Server Native Client" in d for d in drivers)

if has_driver_18 or has_driver_17:
    print("✅ Tienes drivers ODBC modernos instalados - usa uno de ellos")
elif has_native_client:
    print("✅ Tienes SQL Server Native Client - puede funcionar")
else:
    print("❌ No se encontraron drivers SQL Server")
    print("\n   SOLUCIÓN: Instala 'ODBC Driver 18 for SQL Server'")
    print("   Descárgalo desde: https://learn.microsoft.com/es-es/sql/connect/odbc/download-odbc-driver-for-sql-server")
