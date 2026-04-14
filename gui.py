"""
Interfaz gráfica CRUD de Empleados con Tkinter
"""
import tkinter as tk
from tkinter import ttk, messagebox
from crud_operations import CRUDEmpleado
from datetime import datetime, date
import re

class CRUDEmpleadosGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CRUD DE EMPLEADOS")
        self.root.geometry("900x600")
        self.root.resizable(True, True)
        
        # Configurar estilos
        self.configurar_estilos()
        
        # Crear UI
        self.crear_interfaz()
        
        # Cargar datos iniciales
        self.actualizar_tabla()
    
    def configurar_estilos(self):
        """Configura los estilos de la aplicación"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Colores
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'), foreground='#2c3e50')
        style.configure('Header.TLabel', font=('Arial', 11, 'bold'), foreground='#34495e')
        style.configure('Normal.TLabel', font=('Arial', 10))
        style.configure('Button.TButton', font=('Arial', 10))
        
        # Botones de color
        style.map('Success.TButton',
                  foreground=[('!active', 'white'), ('pressed', 'white')],
                  background=[('!active', '#27ae60'), ('active', '#229954'), ('pressed', '#1e8449')])
        
        style.map('Danger.TButton',
                  foreground=[('!active', 'white'), ('pressed', 'white')],
                  background=[('!active', '#e74c3c'), ('active', '#c0392b'), ('pressed', '#a93226')])
        
        style.map('Info.TButton',
                  foreground=[('!active', 'white'), ('pressed', 'white')],
                  background=[('!active', '#3498db'), ('active', '#2980b9'), ('pressed', '#1f618d')])
    
    def crear_interfaz(self):
        """Crea la interfaz principal"""
        # Frame principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Título
        titulo = ttk.Label(main_frame, text="📋 GESTIÓN DE EMPLEADOS", style='Title.TLabel')
        titulo.pack(pady=10)
        
        # Frame para búsqueda
        search_frame = ttk.LabelFrame(main_frame, text="🔍 Búsqueda y Filtros", padding=10)
        search_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(search_frame, text="Buscar por nombre:", style='Normal.TLabel').pack(side=tk.LEFT, padx=5)
        self.search_var = tk.StringVar()
        self.search_var.trace('w', lambda *args: self.filtrar_tabla())
        ttk.Entry(search_frame, textvariable=self.search_var, width=30).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(search_frame, text="🔄 Actualizar", command=self.actualizar_tabla, style='Info.TButton').pack(side=tk.LEFT, padx=5)
        
        # Frame para la tabla
        table_frame = ttk.LabelFrame(main_frame, text="📊 Lista de Empleados", padding=10)
        table_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Crear Treeview
        columns = ('ID', 'Nombre', 'Apellido', 'Email', 'Teléfono', 'Salario', 'Estado')
        self.tree = ttk.Treeview(table_frame, columns=columns, height=15, show='headings')
        
        # Definir encabezados
        self.tree.column('ID', width=40, anchor=tk.CENTER)
        self.tree.column('Nombre', width=100)
        self.tree.column('Apellido', width=100)
        self.tree.column('Email', width=150)
        self.tree.column('Teléfono', width=100)
        self.tree.column('Salario', width=80)
        self.tree.column('Estado', width=60)
        
        for col in columns:
            self.tree.heading(col, text=col)
        
        # Scrollbars
        vsb = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        hsb = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        self.tree.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0, sticky='ns')
        hsb.grid(column=0, row=1, sticky='ew')
        
        table_frame.grid_columnconfigure(0, weight=1)
        table_frame.grid_rowconfigure(0, weight=1)
        
        # Frame para botones
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(button_frame, text="➕ Nuevo Empleado", command=self.abrir_formulario_crear, style='Success.TButton').pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="✏️  Editar", command=self.abrir_formulario_editar, style='Info.TButton').pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="❌ Eliminar", command=self.eliminar_empleado, style='Danger.TButton').pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="👁️  Ver Detalles", command=self.ver_detalles, style='Info.TButton').pack(side=tk.LEFT, padx=5)
    
    def actualizar_tabla(self):
        """Actualiza la tabla con todos los empleados"""
        # Limpiar tabla
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Obtener empleados
        empleados = CRUDEmpleado.leer_todos()
        
        # Llenar tabla
        for emp in empleados:
            id_emp, nombre, apellido, email, telefono, fecha_ingreso, salario, estado = emp
            estado_txt = estado or 'N/A'
            salario_txt = f"${salario:,.2f}" if salario else "N/A"
            
            self.tree.insert('', tk.END, values=(
                id_emp,
                nombre,
                apellido,
                email or '',
                telefono or '',
                salario_txt,
                estado_txt
            ))
    
    def filtrar_tabla(self):
        """Filtra la tabla según el término de búsqueda"""
        termino = self.search_var.get().lower()
        empleados = CRUDEmpleado.leer_todos()
        
        # Limpiar tabla
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Llenar con resultados filtrados
        for emp in empleados:
            id_emp, nombre, apellido, email, telefono, fecha_ingreso, salario, estado = emp
            
            if (termino in nombre.lower() or 
                termino in apellido.lower() or 
                termino in (email or '').lower()):
                
                estado_txt = estado or 'N/A'
                salario_txt = f"${salario:,.2f}" if salario else "N/A"
                
                self.tree.insert('', tk.END, values=(
                    id_emp,
                    nombre,
                    apellido,
                    email or '',
                    telefono or '',
                    salario_txt,
                    estado_txt
                ))
    
    def obtener_empleado_seleccionado(self):
        """Obtiene el empleado seleccionado en la tabla"""
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona un empleado")
            return None
        
        item = self.tree.item(seleccion[0])
        id_emp = item['values'][0]
        return id_emp
    
    def abrir_formulario_crear(self):
        """Abre el formulario para crear un nuevo empleado"""
        self.ventana_formulario = tk.Toplevel(self.root)
        self.ventana_formulario.title("Nuevo Empleado")
        self.ventana_formulario.geometry("400x350")
        self.ventana_formulario.resizable(False, False)
        
        self.crear_formulario(self.ventana_formulario, es_crear=True)
    
    def abrir_formulario_editar(self):
        """Abre el formulario para editar un empleado"""
        id_emp = self.obtener_empleado_seleccionado()
        if id_emp is None:
            return
        
        empleado = CRUDEmpleado.leer_por_id(id_emp)
        if not empleado:
            messagebox.showerror("Error", "No se pudo cargar el empleado")
            return
        
        self.ventana_formulario = tk.Toplevel(self.root)
        self.ventana_formulario.title("Editar Empleado")
        self.ventana_formulario.geometry("400x350")
        self.ventana_formulario.resizable(False, False)
        
        self.crear_formulario(self.ventana_formulario, es_crear=False, empleado=empleado)
    
    def crear_formulario(self, ventana, es_crear=True, empleado=None):
        """Crea el formulario de empleado"""
        frame = ttk.Frame(ventana, padding=15)
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Nombre
        ttk.Label(frame, text="Nombre:", style='Header.TLabel').pack(anchor=tk.W, pady=(10, 5))
        nombre_var = tk.StringVar()
        if empleado:
            nombre_var.set(empleado[1])
        ttk.Entry(frame, textvariable=nombre_var, width=35).pack(anchor=tk.W, pady=(0, 10))
        
        # Apellido
        ttk.Label(frame, text="Apellido:", style='Header.TLabel').pack(anchor=tk.W, pady=(10, 5))
        apellido_var = tk.StringVar()
        if empleado:
            apellido_var.set(empleado[2])
        ttk.Entry(frame, textvariable=apellido_var, width=35).pack(anchor=tk.W, pady=(0, 10))
        
        # Email
        ttk.Label(frame, text="Email:", style='Header.TLabel').pack(anchor=tk.W, pady=(10, 5))
        email_var = tk.StringVar()
        if empleado:
            email_var.set(empleado[3] or '')
        ttk.Entry(frame, textvariable=email_var, width=35).pack(anchor=tk.W, pady=(0, 10))
        
        # Teléfono
        ttk.Label(frame, text="Teléfono:", style='Header.TLabel').pack(anchor=tk.W, pady=(10, 5))
        telefono_var = tk.StringVar()
        if empleado:
            telefono_var.set(empleado[4] or '')
        ttk.Entry(frame, textvariable=telefono_var, width=35).pack(anchor=tk.W, pady=(0, 10))
        
        # Fecha de Ingreso
        ttk.Label(frame, text="Fecha de Ingreso (YYYY-MM-DD):", style='Header.TLabel').pack(anchor=tk.W, pady=(10, 5))
        fecha_ingreso_var = tk.StringVar()
        if empleado:
            fecha_ingreso_var.set(str(empleado[5]))
        ttk.Entry(frame, textvariable=fecha_ingreso_var, width=35).pack(anchor=tk.W, pady=(0, 10))
        
        # Estado
        ttk.Label(frame, text="Estado:", style='Header.TLabel').pack(anchor=tk.W, pady=(10, 5))
        estado_var = tk.StringVar()
        if empleado:
            estado_var.set(empleado[7] or 'Activo')
        else:
            estado_var.set('Activo')
        ttk.OptionMenu(frame, estado_var, estado_var.get(), 'Activo', 'Incapacitado', 'Vacaciones').pack(anchor=tk.W, pady=(0, 10), fill=tk.X)
        
        # Salario
        ttk.Label(frame, text="Salario:", style='Header.TLabel').pack(anchor=tk.W, pady=(10, 5))
        salario_var = tk.StringVar()
        if empleado and empleado[6]:
            salario_var.set(str(empleado[6]))
        ttk.Entry(frame, textvariable=salario_var, width=35).pack(anchor=tk.W, pady=(0, 10))
        
        # Frame para botones
        button_frame = ttk.Frame(frame)
        button_frame.pack(fill=tk.X, pady=20)
        
        def guardar():
            nombre = nombre_var.get().strip()
            apellido = apellido_var.get().strip()
            email = email_var.get().strip()
            telefono = telefono_var.get().strip()
            fecha_ingreso = fecha_ingreso_var.get().strip()
            estado = estado_var.get().strip()
            
            if not nombre or not apellido or ' ' in nombre or ' ' in apellido:
                messagebox.showerror("Error", "Nombre y Apellido deben ser de una sola palabra")
                return
            
            if not fecha_ingreso:
                messagebox.showerror("Error", "La fecha de ingreso es obligatoria")
                return
            
            try:
                fecha = datetime.strptime(fecha_ingreso, '%Y-%m-%d').date()
            except ValueError:
                messagebox.showerror("Error", "Formato de fecha inválido")
                return
            
            if fecha < date(2025, 1, 1):
                messagebox.showerror("Error", "La fecha de ingreso debe ser a partir de 2025")
                return
            
            if estado not in ('Activo', 'Incapacitado', 'Vacaciones'):
                messagebox.showerror("Error", "Selecciona un estado válido")
                return
            
            if not telefono or not telefono.isdigit() or len(telefono) != 10:
                messagebox.showerror("Error", "El teléfono debe tener exactamente 10 dígitos")
                return
            
            try:
                salario = float(salario_var.get())
            except ValueError:
                messagebox.showerror("Error", "Salario debe ser un número")
                return
            
            if salario < 2000000 or salario >= 6000000:
                messagebox.showerror("Error", "El salario debe estar entre 2.000.000 y menos de 6.000.000")
                return
            
            if not email:
                email = f"{nombre.lower()}.{apellido.lower()}@gmail.com"
            
            if not self.validar_email(email) or not email.lower().endswith('@gmail.com'):
                messagebox.showerror("Error", "Email inválido. Debe ser un gmail relacionado con nombre y apellido")
                return
            
            if es_crear:
                CRUDEmpleado.crear_empleado(nombre, apellido, email, telefono, fecha, salario, estado)
                messagebox.showinfo("Éxito", f"Empleado '{nombre} {apellido}' creado")
            else:
                id_emp = empleado[0]
                CRUDEmpleado.actualizar_empleado(id_emp, nombre, apellido, email, telefono, fecha, salario, estado)
                messagebox.showinfo("Éxito", f"Empleado '{nombre} {apellido}' actualizado")
            
            self.actualizar_tabla()
            ventana.destroy()
        
        ttk.Button(button_frame, text="💾 Guardar", command=guardar, style='Success.TButton').pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="❌ Cancelar", command=ventana.destroy).pack(side=tk.LEFT, padx=5)
    
    def eliminar_empleado(self):
        """Elimina un empleado"""
        id_emp = self.obtener_empleado_seleccionado()
        if id_emp is None:
            return
        
        if messagebox.askyesno("Confirmar", f"¿Eliminar empleado ID {id_emp}?"):
            if CRUDEmpleado.eliminar_empleado(id_emp):
                self.actualizar_tabla()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el empleado")
    
    def ver_detalles(self):
        """Muestra los detalles completos de un empleado"""
        id_emp = self.obtener_empleado_seleccionado()
        if id_emp is None:
            return
        
        empleado = CRUDEmpleado.leer_por_id(id_emp)
        if not empleado:
            messagebox.showerror("Error", "No se pudo cargar el empleado")
            return
        
        id_emp, nombre, apellido, email, telefono, fecha_ingreso, salario, estado = empleado
        estado_txt = estado or 'N/A'
        
        salario_txt = f"${salario:,.2f}" if salario else 'N/A'
        detalles = f"""
DETALLES DEL EMPLEADO
{'='*40}
ID: {id_emp}
Nombre: {nombre} {apellido}
Email: {email or 'N/A'}
Teléfono: {telefono or 'N/A'}
Fecha Ingreso: {fecha_ingreso}
Salario: {salario_txt}
Estado: {estado_txt}
"""
        messagebox.showinfo("Detalles del Empleado", detalles)
    
    @staticmethod
    def validar_email(email):
        """Valida el formato de email"""
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron, email) is not None


def main():
    """Ejecuta la aplicación"""
    root = tk.Tk()
    app = CRUDEmpleadosGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
