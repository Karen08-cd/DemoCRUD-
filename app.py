"""
Launcher - Elige entre interfaz gráfica o línea de comandos
"""
import os
import sys
from config import verificar_conexion

def limpiar_pantalla():
    """Limpia la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """Menú principal de selección"""
    limpiar_pantalla()
    
    print("\n" + "="*50)
    print("    CRUD DE EMPLEADOS - SELECCIONA INTERFAZ")
    print("="*50)
    
    print("\n🔍 Verificando conexion a SQL Server...")
    if not verificar_conexion():
        print("\n⚠️  Actualiza los datos de conexion en el archivo '.env'")
        input("Presiona Enter para salir...")
        sys.exit(1)
    
    print("\n¿Qué interfaz deseas utilizar?\n")
    print("1. 🖥️  Interfaz Gráfica (Tkinter)")
    print("2. 💻 Línea de Comandos (CLI)")
    print("3. 🚪 Salir")
    print("\n" + "="*50)
    
    opcion = input("\nSelecciona una opción (1-3): ").strip()
    
    if opcion == '1':
        print("\n⏳ Abriendo interfaz gráfica...")
        from gui import main as gui_main
        gui_main()
    elif opcion == '2':
        print("\n⏳ Abriendo línea de comandos...")
        from main import main as cli_main
        cli_main()
    elif opcion == '3':
        print("\n👋 ¡Hasta luego!")
        sys.exit(0)
    else:
        print("\n❌ Opción inválida")
        input("Presiona Enter para intentar de nuevo...")
        main()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Aplicación interrumpida por el usuario")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        input("Presiona Enter para salir...")
        sys.exit(1)
