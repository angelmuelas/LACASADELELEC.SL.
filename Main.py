# main.py
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime
import random

# Importar todas las clases del sistema
from Administrador import Administrador
from Administradores import Administradores
from Cliente import Cliente
from Clientes import Clientes
from Carrito import Carrito
from Carritos import Carritos
from Envio import Envio
from Envios import Envios
from Telefono import Telefono
from Telefonos import Telefonos
from Television import Television
from Televisiones import Televisiones
from Ordenador import Ordenador
from Ordenadores import Ordenadores
from EquipoSonido import EquipoSonido
from EquiposSonido import EquiposSonido
from Electrodomestico import Electrodomestico

class TiendaElectronica:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🛒 TechStore - Tienda Electrónica")
        self.root.geometry("1200x800")
        self.root.configure(bg='#f0f0f0')
        
        # Variables de sesión
        self.usuario_actual = None
        self.tipo_usuario = None  # 'cliente' o 'administrador'
        self.carrito_actual = None
        
        # Inicializar datos del sistema
        self.inicializar_datos()
        
        # Configurar estilos
        self.configurar_estilos()
        
        # Crear interfaz principal
        self.crear_interfaz_principal()
        
        # Cargar datos de ejemplo
        self.cargar_datos_ejemplo()
    
    def configurar_estilos(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar colores
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'), background='#f0f0f0')
        style.configure('Subtitle.TLabel', font=('Arial', 12, 'bold'), background='#f0f0f0')
        style.configure('Header.TFrame', background='#2c3e50')
        style.configure('Main.TFrame', background='#ecf0f1')
        style.configure('Card.TFrame', background='white', relief='raised', borderwidth=2)
    
    def inicializar_datos(self):
        """Inicializar todas las colecciones de datos"""
        self.administradores = Administradores()
        self.clientes = Clientes()
        self.carritos = Carritos()
        self.envios = Envios()
        self.telefonos = Telefonos()
        self.televisiones = Televisiones()
        self.ordenadores = Ordenadores()
        self.equipos_sonido = EquiposSonido()
        # Note: Electrodomesticos class is referenced but not fully implemented in the original code
        self.electrodomesticos = []
    
    def crear_interfaz_principal(self):
        """Crear la interfaz principal de la aplicación"""
        # Header
        header_frame = ttk.Frame(self.root, style='Header.TFrame')
        header_frame.pack(fill='x', pady=(0, 10))
        
        # Título principal
        title_label = tk.Label(header_frame, text="🛒 TechStore", 
                              font=('Arial', 24, 'bold'), 
                              fg='white', bg='#2c3e50')
        title_label.pack(side='left', padx=20, pady=10)
        
        # Panel de usuario
        self.user_frame = tk.Frame(header_frame, bg='#2c3e50')
        self.user_frame.pack(side='right', padx=20, pady=10)
        
        self.user_label = tk.Label(self.user_frame, text="Invitado", 
                                  font=('Arial', 12), fg='white', bg='#2c3e50')
        self.user_label.pack(side='left', padx=(0, 10))
        
        # Botones de sesión
        login_btn = tk.Button(self.user_frame, text="Iniciar Sesión", 
                             command=self.mostrar_login, bg='#3498db', fg='white')
        login_btn.pack(side='left', padx=2)
        
        register_btn = tk.Button(self.user_frame, text="Registrarse", 
                               command=self.mostrar_registro, bg='#2ecc71', fg='white')
        register_btn.pack(side='left', padx=2)
        
        admin_btn = tk.Button(self.user_frame, text="Admin", 
                            command=self.mostrar_admin_login, bg='#e74c3c', fg='white')
        admin_btn.pack(side='left', padx=2)
        
        # Container principal
        main_container = ttk.Frame(self.root, style='Main.TFrame')
        main_container.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Panel izquierdo - Categorías
        left_panel = ttk.Frame(main_container, style='Card.TFrame')
        left_panel.pack(side='left', fill='y', padx=(0, 5))
        
        categories_label = ttk.Label(left_panel, text="📱 Categorías", style='Title.TLabel')
        categories_label.pack(pady=10)
        
        # Lista de categorías
        self.categories_listbox = tk.Listbox(left_panel, font=('Arial', 12), width=20)
        self.categories_listbox.pack(fill='both', expand=True, padx=10, pady=5)
        self.categories_listbox.bind('<<ListboxSelect>>', self.on_category_select)
        
        # Agregar categorías
        categorias = ["📱 Teléfonos", "📺 Televisiones", "💻 Ordenadores", 
                     "🔊 Equipos de Sonido", "🏠 Electrodomésticos"]
        for categoria in categorias:
            self.categories_listbox.insert(tk.END, categoria)
        
        # Panel central - Productos
        center_panel = ttk.Frame(main_container, style='Card.TFrame')
        center_panel.pack(side='left', fill='both', expand=True, padx=5)
        
        products_label = ttk.Label(center_panel, text="🛍️ Productos", style='Title.TLabel')
        products_label.pack(pady=10)
        
        # Treeview para productos
        columns = ('ID', 'Nombre', 'Marca', 'Precio', 'Detalles')
        self.products_tree = ttk.Treeview(center_panel, columns=columns, show='headings', height=15)
        
        for col in columns:
            self.products_tree.heading(col, text=col)
            self.products_tree.column(col, width=120)
        
        # Scrollbar para productos
        products_scrollbar = ttk.Scrollbar(center_panel, orient='vertical', command=self.products_tree.yview)
        self.products_tree.configure(yscrollcommand=products_scrollbar.set)
        
        self.products_tree.pack(side='left', fill='both', expand=True, padx=(10, 0), pady=5)
        products_scrollbar.pack(side='right', fill='y', pady=5, padx=(0, 10))
        
        # Panel derecho - Carrito y acciones
        right_panel = ttk.Frame(main_container, style='Card.TFrame')
        right_panel.pack(side='right', fill='y', padx=(5, 0))
        
        cart_label = ttk.Label(right_panel, text="🛒 Carrito", style='Title.TLabel')
        cart_label.pack(pady=10)
        
        # Lista del carrito
        self.cart_listbox = tk.Listbox(right_panel, font=('Arial', 10), width=30, height=10)
        self.cart_listbox.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Botones de acción
        btn_frame = ttk.Frame(right_panel)
        btn_frame.pack(fill='x', padx=10, pady=5)
        
        add_to_cart_btn = tk.Button(btn_frame, text="➕ Añadir al Carrito", 
                                   command=self.agregar_al_carrito, bg='#3498db', fg='white')
        add_to_cart_btn.pack(fill='x', pady=2)
        
        remove_from_cart_btn = tk.Button(btn_frame, text="➖ Quitar del Carrito", 
                                        command=self.quitar_del_carrito, bg='#e67e22', fg='white')
        remove_from_cart_btn.pack(fill='x', pady=2)
        
        checkout_btn = tk.Button(btn_frame, text="💳 Comprar", 
                               command=self.realizar_compra, bg='#27ae60', fg='white')
        checkout_btn.pack(fill='x', pady=2)
        
        # Panel de administración (inicialmente oculto)
        self.admin_panel = ttk.Frame(right_panel)
        
        admin_label = ttk.Label(self.admin_panel, text="⚙️ Panel Admin", style='Subtitle.TLabel')
        admin_label.pack(pady=5)
        
        admin_products_btn = tk.Button(self.admin_panel, text="Gestionar Productos", 
                                     command=self.gestionar_productos, bg='#8e44ad', fg='white')
        admin_products_btn.pack(fill='x', pady=2)
        
        admin_users_btn = tk.Button(self.admin_panel, text="Gestionar Usuarios", 
                                  command=self.gestionar_usuarios, bg='#8e44ad', fg='white')
        admin_users_btn.pack(fill='x', pady=2)
        
        admin_orders_btn = tk.Button(self.admin_panel, text="Gestionar Pedidos", 
                                   command=self.gestionar_pedidos, bg='#8e44ad', fg='white')
        admin_orders_btn.pack(fill='x', pady=2)
    
    def cargar_datos_ejemplo(self):
        """Cargar datos de ejemplo para la demostración"""
        # Administrador de ejemplo
        admin = Administrador(1, "Admin", "admin@techstore.com", "admin123")
        self.administradores.agregar(admin)
        
        # Clientes de ejemplo
        cliente1 = Cliente(1, "Juan Pérez", "juan@email.com", "123456", 
                          "Calle Principal 123", "600123456", "12345678A", 
                          "Masculino", "1990-01-01", "2024-01-01", "Premium", "Compras frecuentes")
        self.clientes.agregar(cliente1)
        
        # Productos de ejemplo
        # Teléfonos
        tel1 = Telefono(1, "Smartphone", "Apple", 999.99, "Negro", 6.1, "iOS")
        tel2 = Telefono(2, "Smartphone", "Samsung", 799.99, "Azul", 6.2, "Android")
        tel3 = Telefono(3, "Smartphone", "Xiaomi", 399.99, "Blanco", 6.0, "Android")
        self.telefonos.agregar(tel1)
        self.telefonos.agregar(tel2)
        self.telefonos.agregar(tel3)
        
        # Televisiones
        tv1 = Television(1, "Smart TV", "LG", 599.99, "Negro", 55.0, "WiFi, Bluetooth")
        tv2 = Television(2, "Smart TV", "Samsung", 799.99, "Gris", 65.0, "WiFi, Bluetooth, USB")
        tv3 = Television(3, "TV LED", "Sony", 449.99, "Negro", 43.0, "WiFi")
        self.televisiones.agregar(tv1)
        self.televisiones.agregar(tv2)
        self.televisiones.agregar(tv3)
        
        # Ordenadores
        ord1 = Ordenador(1, "Portátil", "Apple", 1299.99, "Plata", "macOS", "M2", 16)
        ord2 = Ordenador(2, "Portátil", "Dell", 899.99, "Negro", "Windows 11", "Intel i7", 16)
        ord3 = Ordenador(3, "Desktop", "HP", 699.99, "Negro", "Windows 11", "Intel i5", 8)
        self.ordenadores.agregar(ord1)
        self.ordenadores.agregar(ord2)
        self.ordenadores.agregar(ord3)
        
        # Equipos de sonido
        audio1 = EquipoSonido(1, "Altavoz", "JBL", 199.99, "Negro", 40)
        audio2 = EquipoSonido(2, "Auriculares", "Sony", 299.99, "Azul", 0)
        audio3 = EquipoSonido(3, "Barra de sonido", "Samsung", 399.99, "Negro", 120)
        self.equipos_sonido.agregar(audio1)
        self.equipos_sonido.agregar(audio2)
        self.equipos_sonido.agregar(audio3)
    
    def on_category_select(self, event):
        """Manejar selección de categoría"""
        selection = self.categories_listbox.curselection()
        if selection:
            categoria_index = selection[0]
            self.mostrar_productos_categoria(categoria_index)
    
    def mostrar_productos_categoria(self, categoria_index):
        """Mostrar productos de la categoría seleccionada"""
        # Limpiar lista actual
        for item in self.products_tree.get_children():
            self.products_tree.delete(item)
        
        if categoria_index == 0:  # Teléfonos
            productos = self.telefonos.mostrarTodos()
            for tel in productos:
                detalles = f"{tel.get_pulgadas()}\" - {tel.get_sistemaOperativo()}"
                self.products_tree.insert('', 'end', values=(
                    tel.get_id(), tel.get_tipo(), tel.get_marca(), 
                    f"{tel.get_precio()}€", detalles))
        
        elif categoria_index == 1:  # Televisiones
            productos = self.televisiones.mostrarTodos()
            for tv in productos:
                detalles = f"{tv.get_pulgadas()}\" - {tv.get_conectividad()}"
                self.products_tree.insert('', 'end', values=(
                    tv.get_id(), tv.get_tipo(), tv.get_marca(), 
                    f"{tv.get_precio()}€", detalles))
        
        elif categoria_index == 2:  # Ordenadores
            productos = self.ordenadores.mostrarTodos()
            for ord in productos:
                detalles = f"{ord.get_procesador()} - {ord.get_memoriaRam()}GB RAM"
                self.products_tree.insert('', 'end', values=(
                    ord.get_id(), ord.get_tipo(), ord.get_marca(), 
                    f"{ord.get_precio()}€", detalles))
        
        elif categoria_index == 3:  # Equipos de Sonido
            productos = self.equipos_sonido.mostrarTodos()
            for audio in productos:
                detalles = f"{audio.get_potencia()}W" if audio.get_potencia() > 0 else "Auriculares"
                self.products_tree.insert('', 'end', values=(
                    audio.get_id(), audio.get_tipo(), audio.get_marca(), 
                    f"{audio.get_precio()}€", detalles))
    
    def mostrar_login(self):
        """Mostrar ventana de login para clientes"""
        login_window = tk.Toplevel(self.root)
        login_window.title("Iniciar Sesión - Cliente")
        login_window.geometry("400x300")
        login_window.configure(bg='#ecf0f1')
        login_window.transient(self.root)
        login_window.grab_set()
        
        # Centrar ventana
        login_window.geometry("+%d+%d" % (self.root.winfo_rootx() + 50, self.root.winfo_rooty() + 50))
        
        # Contenido
        tk.Label(login_window, text="🔐 Iniciar Sesión", font=('Arial', 18, 'bold'), 
                bg='#ecf0f1').pack(pady=20)
        
        # Email
        tk.Label(login_window, text="Email:", font=('Arial', 12), bg='#ecf0f1').pack()
        email_entry = tk.Entry(login_window, font=('Arial', 12), width=30)
        email_entry.pack(pady=5)
        
        # Contraseña
        tk.Label(login_window, text="Contraseña:", font=('Arial', 12), bg='#ecf0f1').pack()
        password_entry = tk.Entry(login_window, font=('Arial', 12), width=30, show='*')
        password_entry.pack(pady=5)
        
        def login():
            email = email_entry.get().strip()
            password = password_entry.get().strip()
            
            if not email or not password:
                messagebox.showerror("Error", "Por favor, complete todos los campos")
                return
            
            # Buscar cliente
            for cliente in self.clientes.mostrarTodos():
                if cliente.get_email() == email and cliente.get_contrasena() == password:
                    self.usuario_actual = cliente
                    self.tipo_usuario = 'cliente'
                    self.user_label.config(text=f"Cliente: {cliente.get_nombre()}")
                    self.crear_carrito_usuario()
                    login_window.destroy()
                    messagebox.showinfo("Éxito", f"Bienvenido, {cliente.get_nombre()}!")
                    return
            
            messagebox.showerror("Error", "Credenciales incorrectas")
        
        # Botones
        btn_frame = tk.Frame(login_window, bg='#ecf0f1')
        btn_frame.pack(pady=20)
        
        tk.Button(btn_frame, text="Iniciar Sesión", command=login, 
                 bg='#3498db', fg='white', font=('Arial', 12)).pack(side='left', padx=5)
        tk.Button(btn_frame, text="Cancelar", command=login_window.destroy, 
                 bg='#95a5a6', fg='white', font=('Arial', 12)).pack(side='left', padx=5)
    
    def mostrar_registro(self):
        """Mostrar ventana de registro para nuevos clientes"""
        register_window = tk.Toplevel(self.root)
        register_window.title("Registro de Cliente")
        register_window.geometry("500x600")
        register_window.configure(bg='#ecf0f1')
        register_window.transient(self.root)
        register_window.grab_set()
        
        # Centrar ventana
        register_window.geometry("+%d+%d" % (self.root.winfo_rootx() + 50, self.root.winfo_rooty() + 50))
        
        # Título
        tk.Label(register_window, text="📝 Registro de Cliente", font=('Arial', 18, 'bold'), 
                bg='#ecf0f1').pack(pady=10)
        
        # Frame para el formulario
        form_frame = tk.Frame(register_window, bg='#ecf0f1')
        form_frame.pack(pady=10, padx=20)
        
        # Campos del formulario
        fields = [
            ("Nombre:", "nombre"),
            ("Email:", "email"),
            ("Contraseña:", "contrasena"),
            ("Dirección:", "direccion"),
            ("Teléfono:", "telefono"),
            ("DNI:", "dni"),
            ("Género:", "genero"),
            ("Fecha Nacimiento (YYYY-MM-DD):", "fecha_nacimiento")
        ]
        
        entries = {}
        
        for i, (label, field) in enumerate(fields):
            tk.Label(form_frame, text=label, font=('Arial', 10), bg='#ecf0f1').grid(
                row=i, column=0, sticky='w', pady=2)
            
            if field == "contrasena":
                entry = tk.Entry(form_frame, font=('Arial', 10), width=30, show='*')
            else:
                entry = tk.Entry(form_frame, font=('Arial', 10), width=30)
            
            entry.grid(row=i, column=1, pady=2, padx=(10, 0))
            entries[field] = entry
        
        def registrar():
            try:
                # Validar campos
                for field, entry in entries.items():
                    if not entry.get().strip():
                        messagebox.showerror("Error", f"El campo {field} es obligatorio")
                        return
                
                # Generar nuevo ID
                nuevo_id = len(self.clientes.mostrarTodos()) + 1
                
                # Crear cliente
                cliente = Cliente(
                    nuevo_id,
                    entries["nombre"].get().strip(),
                    entries["email"].get().strip(),
                    entries["contrasena"].get().strip(),
                    entries["direccion"].get().strip(),
                    entries["telefono"].get().strip(),
                    entries["dni"].get().strip(),
                    entries["genero"].get().strip(),
                    entries["fecha_nacimiento"].get().strip(),
                    datetime.now().strftime("%Y-%m-%d"),
                    "Regular",
                    "Nuevo cliente"
                )
                
                # Verificar email único
                for c in self.clientes.mostrarTodos():
                    if c.get_email() == cliente.get_email():
                        messagebox.showerror("Error", "El email ya está registrado")
                        return
                
                # Agregar cliente
                if self.clientes.agregar(cliente):
                    messagebox.showinfo("Éxito", "Cliente registrado correctamente")
                    register_window.destroy()
                else:
                    messagebox.showerror("Error", "Error al registrar cliente")
                
            except Exception as e:
                messagebox.showerror("Error", f"Error en el registro: {str(e)}")
        
        # Botones
        btn_frame = tk.Frame(register_window, bg='#ecf0f1')
        btn_frame.pack(pady=20)
        
        tk.Button(btn_frame, text="Registrarse", command=registrar, 
                 bg='#2ecc71', fg='white', font=('Arial', 12)).pack(side='left', padx=5)
        tk.Button(btn_frame, text="Cancelar", command=register_window.destroy, 
                 bg='#95a5a6', fg='white', font=('Arial', 12)).pack(side='left', padx=5)
    
    def mostrar_admin_login(self):
        """Mostrar ventana de login para administradores"""
        admin_window = tk.Toplevel(self.root)
        admin_window.title("Login Administrador")
        admin_window.geometry("400x300")
        admin_window.configure(bg='#ecf0f1')
        admin_window.transient(self.root)
        admin_window.grab_set()
        
        # Centrar ventana
        admin_window.geometry("+%d+%d" % (self.root.winfo_rootx() + 50, self.root.winfo_rooty() + 50))
        
        tk.Label(admin_window, text="🔐 Login Administrador", font=('Arial', 18, 'bold'), 
                bg='#ecf0f1').pack(pady=20)
        
        # Email
        tk.Label(admin_window, text="Email:", font=('Arial', 12), bg='#ecf0f1').pack()
        email_entry = tk.Entry(admin_window, font=('Arial', 12), width=30)
        email_entry.pack(pady=5)
        
        # Contraseña
        tk.Label(admin_window, text="Contraseña:", font=('Arial', 12), bg='#ecf0f1').pack()
        password_entry = tk.Entry(admin_window, font=('Arial', 12), width=30, show='*')
        password_entry.pack(pady=5)
        
        def admin_login():
            email = email_entry.get().strip()
            password = password_entry.get().strip()
            
            if not email or not password:
                messagebox.showerror("Error", "Complete todos los campos")
                return
            
            # Buscar administrador
            for admin in self.administradores.mostrarTodos():
                if admin.get_email() == email and admin.get_contrasena() == password:
                    self.usuario_actual = admin
                    self.tipo_usuario = 'administrador'
                    self.user_label.config(text=f"Admin: {admin.get_nombre()}")
                    self.admin_panel.pack(fill='x', pady=10)
                    admin_window.destroy()
                    messagebox.showinfo("Éxito", f"Bienvenido, {admin.get_nombre()}!")
                    return
            
            messagebox.showerror("Error", "Credenciales incorrectas")
        
        # Botones
        btn_frame = tk.Frame(admin_window, bg='#ecf0f1')
        btn_frame.pack(pady=20)
        
        tk.Button(btn_frame, text="Iniciar Sesión", command=admin_login, 
                 bg='#e74c3c', fg='white', font=('Arial', 12)).pack(side='left', padx=5)
        tk.Button(btn_frame, text="Cancelar", command=admin_window.destroy, 
                 bg='#95a5a6', fg='white', font=('Arial', 12)).pack(side='left', padx=5)
    
    def crear_carrito_usuario(self):
        """Crear carrito para el usuario actual"""
        if self.usuario_actual and self.tipo_usuario == 'cliente':
            nuevo_id = len(self.carritos.mostrarTodos()) + 1
            self.carrito_actual = Carrito(
                nuevo_id, 0, datetime.now().strftime("%Y-%m-%d"), 
                "Activo", 0.0, 0.0, 0.0
            )
            self.carritos.agregar(self.carrito_actual)
    
    def agregar_al_carrito(self):
        """Agregar producto seleccionado al carrito"""
        if not self.usuario_actual or self.tipo_usuario != 'cliente':
            messagebox.showwarning("Acceso Requerido", "Debe iniciar sesión como cliente para añadir productos")
            return
        
        selection = self.products_tree.selection()
        if not selection:
            messagebox.showwarning("Selección", "Por favor, seleccione un producto")
            return
        
        item = self.products_tree.item(selection[0])
        producto_info = item['values']
        
        # Agregar al carrito visual
        producto_text = f"{producto_info[1]} {producto_info[2]} - {producto_info[3]}"
        self.cart_listbox.insert(tk.END, producto_text)
        
        # Actualizar carrito actual
        if self.carrito_actual:
            precio = float(producto_info[3].replace('€', ''))
            self.carrito_actual.set_productoTotal(self.carrito_actual.get_productoTotal() + 1)
            self.carrito_actual.set_precioTotal(self.carrito_actual.get_precioTotal() + precio)
            self.carrito_actual.set_precioFinal(self.carrito_actual.get_precioTotal())
        
        messagebox.showinfo("Éxito", "Producto añadido al carrito")
    
    def quitar_del_carrito(self):
        """Quitar producto seleccionado del carrito"""
        selection = self.cart_listbox.curselection()
        if not selection:
            messagebox.showwarning("Selección", "Seleccione un producto del carrito")
            return
        
        self.cart_listbox.delete(selection[0])
        
        # Actualizar carrito actual
        if self.carrito_actual and self.carrito_actual.get_productoTotal() > 0:
            self.carrito_actual.set_productoTotal(self.carrito_actual.get_productoTotal() - 1)
            # Nota: Para simplicidad, no calculamos el precio exacto a restar
        
        messagebox.showinfo("Éxito", "Producto eliminado del carrito")
    
    def realizar_compra(self):
        """Procesar la compra del carrito"""
        if not self.usuario_actual or self.tipo_usuario != 'cliente':
            messagebox.showwarning("Acceso Requerido", "Debe iniciar sesión como cliente")
            return
        
        if self.cart_listbox.size() == 0:
            messagebox.showwarning("Carrito Vacío", "No hay productos en el carrito")
            return
        
        # Confirmar compra
        total = self.carrito_actual.get_precioTotal() if self.carrito_actual else 0
        confirmar = messagebox.askyesno("Confirmar Compra", 
                                       f"¿Confirmar compra por {total:.2f}€?")
        
        if confirmar:
            # Cambiar estado del carrito
            if self.carrito_actual:
                self.carrito_actual.set_estado("Completado")
            
            # Crear envío
            nuevo_envio_id = len(self.envios.mostrarTodos()) + 1
            envio = Envio(
                nuevo_envio_id,
                f"Pedido #{nuevo_envio_id}",
                datetime.now().strftime("%Y-%m-%d"),
                "Por determinar",
                "Preparando",
                "Correos",
                random.uniform(0.5, 5.0),
                random.uniform(0.01, 0.1)
            )
            self.envios.agregar(envio)
            
            # Limpiar carrito visual
            self.cart_listbox.delete(0, tk.END)
            
            # Crear nuevo carrito para futuras compras
            self.crear_carrito_usuario()
            
            messagebox.showinfo("Compra Realizada", 
                              f"Compra realizada con éxito!\nTotal: {total:.2f}€\nNúmero de seguimiento: ENV-{nuevo_envio_id}")
    
    def gestionar_productos(self):
        """Abrir ventana de gestión de productos para administradores"""
        if self.tipo_usuario != 'administrador':
            messagebox.showwarning("Acceso Denegado", "Solo administradores pueden acceder")
            return
        
        products_window = tk.Toplevel(self.root)
        products_window.title("⚙️ Gestión de Productos")
        products_window.geometry("800x600")
        products_window.configure(bg='#ecf0f1')
        
        # Notebook para diferentes categorías
        notebook = ttk.Notebook(products_window)
        notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Pestaña Teléfonos
        tel_frame = ttk.Frame(notebook)
        notebook.add(tel_frame, text="📱 Teléfonos")
        self.crear_gestion_categoria(tel_frame, self.telefonos, "telefono")
        
        # Pestaña Televisiones
        tv_frame = ttk.Frame(notebook)
        notebook.add(tv_frame, text="📺 Televisiones")
        self.crear_gestion_categoria(tv_frame, self.televisiones, "television")
        
        # Pestaña Ordenadores
        ord_frame = ttk.Frame(notebook)
        notebook.add(ord_frame, text="💻 Ordenadores")
        self.crear_gestion_categoria(ord_frame, self.ordenadores, "ordenador")
        
        # Pestaña Equipos de Sonido
        audio_frame = ttk.Frame(notebook)
        notebook.add(audio_frame, text="🔊 Audio")
        self.crear_gestion_categoria(audio_frame, self.equipos_sonido, "audio")
    
    def crear_gestion_categoria(self, parent, coleccion, tipo):
        """Crear interfaz de gestión para una categoría específica"""
        # Lista de productos
        listbox = tk.Listbox(parent, font=('Arial', 10))
        listbox.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Actualizar lista
        def actualizar_lista():
            listbox.delete(0, tk.END)
            for producto in coleccion.mostrarTodos():
                info = f"ID: {producto.get_id()} - {producto.get_marca()} {producto.get_tipo()} - {producto.get_precio()}€"
                listbox.insert(tk.END, info)
        
        actualizar_lista()
        
        # Botones de gestión
        btn_frame = tk.Frame(parent, bg='#ecf0f1')
        btn_frame.pack(fill='x', padx=10, pady=5)
        
        def agregar_producto():
            self.mostrar_formulario_producto(tipo, coleccion, actualizar_lista)
        
        def eliminar_producto():
            selection = listbox.curselection()
            if not selection:
                messagebox.showwarning("Selección", "Seleccione un producto")
                return
            
            # Extraer ID del texto seleccionado
            texto = listbox.get(selection[0])
            id_producto = int(texto.split()[1])
            
            if coleccion.eliminar(id_producto):
                messagebox.showinfo("Éxito", "Producto eliminado")
                actualizar_lista()
                # Actualizar vista principal si es necesario
                categoria_actual = self.categories_listbox.curselection()
                if categoria_actual:
                    self.mostrar_productos_categoria(categoria_actual[0])
            else:
                messagebox.showerror("Error", "No se pudo eliminar el producto")
        
        tk.Button(btn_frame, text="➕ Agregar", command=agregar_producto, 
                 bg='#27ae60', fg='white').pack(side='left', padx=5)
        tk.Button(btn_frame, text="🗑️ Eliminar", command=eliminar_producto, 
                 bg='#e74c3c', fg='white').pack(side='left', padx=5)
    
    def mostrar_formulario_producto(self, tipo, coleccion, callback_actualizar):
        """Mostrar formulario para agregar/editar producto"""
        form_window = tk.Toplevel(self.root)
        form_window.title(f"Agregar {tipo.title()}")
        form_window.geometry("400x500")
        form_window.configure(bg='#ecf0f1')
        form_window.transient(self.root)
        form_window.grab_set()
        
        tk.Label(form_window, text=f"Nuevo {tipo.title()}", 
                font=('Arial', 16, 'bold'), bg='#ecf0f1').pack(pady=10)
        
        # Campos comunes
        campos_comunes = ["Tipo", "Marca", "Precio", "Color"]
        entries = {}
        
        for campo in campos_comunes:
            tk.Label(form_window, text=f"{campo}:", bg='#ecf0f1').pack()
            entry = tk.Entry(form_window, width=30)
            entry.pack(pady=5)
            entries[campo.lower()] = entry
        
        # Campos específicos según el tipo
        if tipo == "telefono":
            tk.Label(form_window, text="Pulgadas:", bg='#ecf0f1').pack()
            entries['pulgadas'] = tk.Entry(form_window, width=30)
            entries['pulgadas'].pack(pady=5)
            
            tk.Label(form_window, text="Sistema Operativo:", bg='#ecf0f1').pack()
            entries['sistema_operativo'] = tk.Entry(form_window, width=30)
            entries['sistema_operativo'].pack(pady=5)
        
        elif tipo == "television":
            tk.Label(form_window, text="Pulgadas:", bg='#ecf0f1').pack()
            entries['pulgadas'] = tk.Entry(form_window, width=30)
            entries['pulgadas'].pack(pady=5)
            
            tk.Label(form_window, text="Conectividad:", bg='#ecf0f1').pack()
            entries['conectividad'] = tk.Entry(form_window, width=30)
            entries['conectividad'].pack(pady=5)
        
        elif tipo == "ordenador":
            tk.Label(form_window, text="Sistema Operativo:", bg='#ecf0f1').pack()
            entries['sistema_operativo'] = tk.Entry(form_window, width=30)
            entries['sistema_operativo'].pack(pady=5)
            
            tk.Label(form_window, text="Procesador:", bg='#ecf0f1').pack()
            entries['procesador'] = tk.Entry(form_window, width=30)
            entries['procesador'].pack(pady=5)
            
            tk.Label(form_window, text="Memoria RAM (GB):", bg='#ecf0f1').pack()
            entries['memoria_ram'] = tk.Entry(form_window, width=30)
            entries['memoria_ram'].pack(pady=5)
        
        elif tipo == "audio":
            tk.Label(form_window, text="Potencia (W):", bg='#ecf0f1').pack()
            entries['potencia'] = tk.Entry(form_window, width=30)
            entries['potencia'].pack(pady=5)
        
        def guardar_producto():
            try:
                # Generar nuevo ID
                nuevo_id = len(coleccion.mostrarTodos()) + 1
                
                # Validar campos básicos
                tipo_val = entries['tipo'].get().strip()
                marca_val = entries['marca'].get().strip()
                precio_val = float(entries['precio'].get().strip())
                color_val = entries['color'].get().strip()
                
                if not all([tipo_val, marca_val, color_val]) or precio_val <= 0:
                    messagebox.showerror("Error", "Complete todos los campos correctamente")
                    return
                
                # Crear producto según el tipo
                if tipo == "telefono":
                    producto = Telefono(
                        nuevo_id, tipo_val, marca_val, precio_val, color_val,
                        float(entries['pulgadas'].get()),
                        entries['sistema_operativo'].get().strip()
                    )
                elif tipo == "television":
                    producto = Television(
                        nuevo_id, tipo_val, marca_val, precio_val, color_val,
                        float(entries['pulgadas'].get()),
                        entries['conectividad'].get().strip()
                    )
                elif tipo == "ordenador":
                    producto = Ordenador(
                        nuevo_id, tipo_val, marca_val, precio_val, color_val,
                        entries['sistema_operativo'].get().strip(),
                        entries['procesador'].get().strip(),
                        int(entries['memoria_ram'].get())
                    )
                elif tipo == "audio":
                    producto = EquipoSonido(
                        nuevo_id, tipo_val, marca_val, precio_val, color_val,
                        int(entries['potencia'].get())
                    )
                
                # Agregar a la colección
                if coleccion.agregar(producto):
                    messagebox.showinfo("Éxito", "Producto agregado correctamente")
                    callback_actualizar()
                    form_window.destroy()
                    
                    # Actualizar vista principal si es necesario
                    categoria_actual = self.categories_listbox.curselection()
                    if categoria_actual:
                        self.mostrar_productos_categoria(categoria_actual[0])
                else:
                    messagebox.showerror("Error", "No se pudo agregar el producto")
            
            except ValueError as e:
                messagebox.showerror("Error", "Verifique que los valores numéricos sean correctos")
            except Exception as e:
                messagebox.showerror("Error", f"Error al guardar: {str(e)}")
        
        # Botones
        btn_frame = tk.Frame(form_window, bg='#ecf0f1')
        btn_frame.pack(pady=20)
        
        tk.Button(btn_frame, text="💾 Guardar", command=guardar_producto, 
                 bg='#27ae60', fg='white').pack(side='left', padx=5)
        tk.Button(btn_frame, text="❌ Cancelar", command=form_window.destroy, 
                 bg='#95a5a6', fg='white').pack(side='left', padx=5)
    
    def gestionar_usuarios(self):
        """Abrir ventana de gestión de usuarios"""
        if self.tipo_usuario != 'administrador':
            messagebox.showwarning("Acceso Denegado", "Solo administradores pueden acceder")
            return
        
        users_window = tk.Toplevel(self.root)
        users_window.title("👥 Gestión de Usuarios")
        users_window.geometry("800x600")
        users_window.configure(bg='#ecf0f1')
        
        # Notebook para clientes y administradores
        notebook = ttk.Notebook(users_window)
        notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Pestaña Clientes
        clientes_frame = ttk.Frame(notebook)
        notebook.add(clientes_frame, text="👤 Clientes")
        
        # Lista de clientes
        clientes_tree = ttk.Treeview(clientes_frame, columns=('ID', 'Nombre', 'Email', 'Categoría'), show='headings')
        clientes_tree.pack(fill='both', expand=True, padx=10, pady=10)
        
        for col in ['ID', 'Nombre', 'Email', 'Categoría']:
            clientes_tree.heading(col, text=col)
            clientes_tree.column(col, width=150)
        
        # Cargar clientes
        def actualizar_clientes():
            clientes_tree.delete(*clientes_tree.get_children())
            for cliente in self.clientes.mostrarTodos():
                clientes_tree.insert('', 'end', values=(
                    cliente.get_id(), cliente.get_nombre(), 
                    cliente.get_email(), cliente.get_categoria()
                ))
        
        actualizar_clientes()
        
        # Pestaña Administradores
        admin_frame = ttk.Frame(notebook)
        notebook.add(admin_frame, text="🔧 Administradores")
        
        # Lista de administradores
        admin_tree = ttk.Treeview(admin_frame, columns=('ID', 'Nombre', 'Email'), show='headings')
        admin_tree.pack(fill='both', expand=True, padx=10, pady=10)
        
        for col in ['ID', 'Nombre', 'Email']:
            admin_tree.heading(col, text=col)
            admin_tree.column(col, width=200)
        
        def actualizar_admins():
            admin_tree.delete(*admin_tree.get_children())
            for admin in self.administradores.mostrarTodos():
                admin_tree.insert('', 'end', values=(
                    admin.get_id(), admin.get_nombre(), admin.get_email()
                ))
        
        actualizar_admins()
    
    def gestionar_pedidos(self):
        """Abrir ventana de gestión de pedidos y envíos"""
        if self.tipo_usuario != 'administrador':
            messagebox.showwarning("Acceso Denegado", "Solo administradores pueden acceder")
            return
        
        orders_window = tk.Toplevel(self.root)
        orders_window.title("📦 Gestión de Pedidos")
        orders_window.geometry("900x600")
        orders_window.configure(bg='#ecf0f1')
        
        # Notebook para carritos y envíos
        notebook = ttk.Notebook(orders_window)
        notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Pestaña Carritos
        carritos_frame = ttk.Frame(notebook)
        notebook.add(carritos_frame, text="🛒 Carritos")
        
        carritos_tree = ttk.Treeview(carritos_frame, columns=('ID', 'Productos', 'Precio Total', 'Estado'), show='headings')
        carritos_tree.pack(fill='both', expand=True, padx=10, pady=10)
        
        for col in ['ID', 'Productos', 'Precio Total', 'Estado']:
            carritos_tree.heading(col, text=col)
            carritos_tree.column(col, width=150)
        
        def actualizar_carritos():
            carritos_tree.delete(*carritos_tree.get_children())
            for carrito in self.carritos.mostrarTodos():
                carritos_tree.insert('', 'end', values=(
                    carrito.get_id(), carrito.get_productoTotal(),
                    f"{carrito.get_precioTotal()}€", carrito.get_estado()
                ))
        
        actualizar_carritos()
        
        # Pestaña Envíos
        envios_frame = ttk.Frame(notebook)
        notebook.add(envios_frame, text="🚚 Envíos")
        
        envios_tree = ttk.Treeview(envios_frame, columns=('ID', 'Pedido', 'Estado', 'Transportista'), show='headings')
        envios_tree.pack(fill='both', expand=True, padx=10, pady=10)
        
        for col in ['ID', 'Pedido', 'Estado', 'Transportista']:
            envios_tree.heading(col, text=col)
            envios_tree.column(col, width=180)
        
        def actualizar_envios():
            envios_tree.delete(*envios_tree.get_children())
            for envio in self.envios.mostrarTodos():
                envios_tree.insert('', 'end', values=(
                    envio.get_id(), envio.get_pedido(),
                    envio.get_estado(), envio.get_transportista()
                ))
        
        actualizar_envios()
        
        # Botones de gestión para envíos
        envios_btn_frame = tk.Frame(envios_frame, bg='#ecf0f1')
        envios_btn_frame.pack(fill='x', padx=10, pady=5)
        
        def cambiar_estado_envio():
            selection = envios_tree.selection()
            if not selection:
                messagebox.showwarning("Selección", "Seleccione un envío")
                return
            
            estados = ["Preparando", "En tránsito", "Entregado", "Devuelto"]
            nuevo_estado = simpledialog.askstring("Cambiar Estado", 
                                                 f"Estados disponibles: {', '.join(estados)}\nIngrese nuevo estado:")
            
            if nuevo_estado and nuevo_estado in estados:
                item = envios_tree.item(selection[0])
                envio_id = int(item['values'][0])
                
                envio = self.envios.buscar(envio_id)
                if envio:
                    envio.set_estado(nuevo_estado)
                    actualizar_envios()
                    messagebox.showinfo("Éxito", "Estado actualizado")
        
        tk.Button(envios_btn_frame, text="📝 Cambiar Estado", command=cambiar_estado_envio, 
                 bg='#f39c12', fg='white').pack(side='left', padx=5)
    
    def run(self):
        """Ejecutar la aplicación"""
        self.root.mainloop()

# Punto de entrada de la aplicación
if __name__ == "__main__":
    app = TiendaElectronica()
    app.run()