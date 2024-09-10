import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("900x600")
        self.title("Control Hotel")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=1, fill="both")

        # Listas para la base de datos
        self.clientes = []
        self.habitaciones = []
        self.reservaciones = []

        self.crearPestanas()

    def crearPestanas(self):
        # Creamos los frames de cada pestaña
        self.pestana_Clientes = pestanaClientes(self.notebook, self.clientes)
        self.pestana_Reservaciones = pestanaReservaciones(self.notebook, self.reservaciones, self.clientes, self.habitaciones)
        self.pestana_Habitaciones = PestanaHabitaciones(self.notebook, self.habitaciones)

        # Añadir las pestañas al notebook
        self.notebook.add(self.pestana_Clientes, text="Clientes")
        self.notebook.add(self.pestana_Reservaciones, text="Reservaciones")
        self.notebook.add(self.pestana_Habitaciones, text="Habitaciones")
    
class pestanaClientes(ttk.Frame):
    def __init__(self, notebook, clientes):
        super().__init__(notebook)
        self.clientes = clientes

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Frame para Id del cliente
        self.frameIngresarId = tk.Frame(self)
        self.frameIngresarId.grid(row=0, column=1, padx=10, pady=20)

        # Etiquetas y Entradas para Clientes
        self.lbIngresarId = tk.Label(self.frameIngresarId, text="Ingrese ID del Cliente: ")
        self.lbIngresarId.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.txIngresarId = tk.Entry(self.frameIngresarId, width=30)
        self.txIngresarId.grid(row=0, column=1, padx=10, pady=5)

        # Botón de buscar
        self.btBuscar = tk.Button(self.frameIngresarId, text="Buscar", font=("Arial", 10, "bold"), command=self.buscar_cliente)
        self.btBuscar.grid(row=0, column=2, padx=15)

        # Frame para entrys de datos
        self.frameEntradaDeDatos = tk.Frame(self)
        self.frameEntradaDeDatos.grid(row=1, column=1, padx=10)

        # Entrada de datos del cliente
        self.lbId = tk.Label(self.frameEntradaDeDatos, text="ID: ")
        self.lbId.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.txId = tk.Entry(self.frameEntradaDeDatos)
        self.txId.grid(row=1, column=1, padx=10, pady=10)

        self.lbNombre = tk.Label(self.frameEntradaDeDatos, text="Nombre: ")
        self.lbNombre.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.txNombre = tk.Entry(self.frameEntradaDeDatos)
        self.txNombre.grid(row=2, column=1, padx=10, pady=10)

        self.lbDireccion = tk.Label(self.frameEntradaDeDatos, text="Dirección: ")
        self.lbDireccion.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.txDireccion = tk.Entry(self.frameEntradaDeDatos)
        self.txDireccion.grid(row=3, column=1, padx=10, pady=10)

        self.lbTelefono = tk.Label(self.frameEntradaDeDatos, text="Teléfono: ")
        self.lbTelefono.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.txTelefono = tk.Entry(self.frameEntradaDeDatos)
        self.txTelefono.grid(row=4, column=1, padx=10, pady=10)

        self.lbEmail = tk.Label(self.frameEntradaDeDatos, text="Email: ")
        self.lbEmail.grid(row=2, column=3, padx=10, pady=10, sticky="w")
        self.txEmail = tk.Entry(self.frameEntradaDeDatos)
        self.txEmail.grid(row=2, column=4, padx=10, pady=10)

        # Frame para botones
        self.frameBotones = tk.Frame(self)
        self.frameBotones.grid(row=5, column=1)

        self.btNuevo = tk.Button(self.frameBotones, text="Nuevo", font=("Arial", 10), command=self.nuevo_cliente)
        self.btNuevo.grid(row=1, column=1, padx=10, pady=10)

        self.btSalvar = tk.Button(self.frameBotones, text="Salvar", font=("Arial", 10), command=self.salvar_cliente, state=tk.DISABLED)
        self.btSalvar.grid(row=1, column=2, padx=10, pady=10)

        self.btCancelar = tk.Button(self.frameBotones, text="Cancelar", font=("Arial", 10), command=self.cancelar, state=tk.DISABLED)
        self.btCancelar.grid(row=1, column=3, padx=10, pady=10)

        self.btEditar = tk.Button(self.frameBotones, text="Editar", font=("Arial", 10), command=self.editar_cliente, state=tk.DISABLED)
        self.btEditar.grid(row=1, column=4, padx=10, pady=10)

        self.btEliminar = tk.Button(self.frameBotones, text="Eliminar", font=("Arial", 10), command=self.eliminar_cliente, state=tk.DISABLED)
        self.btEliminar.grid(row=1, column=5, padx=10, pady=10)

    def nuevo_cliente(self):
        self.txId.delete(0, tk.END)
        self.txNombre.delete(0, tk.END)
        self.txDireccion.delete(0, tk.END)
        self.txTelefono.delete(0, tk.END)
        self.txEmail.delete(0, tk.END)

        # Generar automáticamente el ID del cliente
        nuevo_id = len(self.clientes) + 1
        self.txId.insert(0, nuevo_id)

        # Habilitar botones
        self.btSalvar.config(state=tk.NORMAL)
        self.btCancelar.config(state=tk.NORMAL)
        self.btEditar.config(state=tk.NORMAL)
        self.btEliminar.config(state=tk.NORMAL)

    def buscar_cliente(self):
        id_cliente = self.txIngresarId.get()
        for cliente in self.clientes:
            if cliente["ID"] == id_cliente:
                self.txId.delete(0, tk.END)
                self.txId.insert(0, cliente["ID"])
                self.txNombre.delete(0, tk.END)
                self.txNombre.insert(0, cliente["Nombre"])
                self.txDireccion.delete(0, tk.END)
                self.txDireccion.insert(0, cliente["Direccion"])
                self.txTelefono.delete(0, tk.END)
                self.txTelefono.insert(0, cliente["Telefono"])
                self.txEmail.delete(0, tk.END)
                self.txEmail.insert(0, cliente["Email"])

                # Habilitar botones de Editar y Cancelar
                self.btEditar.config(state=tk.NORMAL)
                self.btCancelar.config(state=tk.NORMAL)
                return
        messagebox.showerror("Error", "Cliente no encontrado")


    def salvar_cliente(self):
        cliente = {
            "ID": self.txId.get(),
            "Nombre": self.txNombre.get(),
            "Direccion": self.txDireccion.get(),
            "Telefono": self.txTelefono.get(),
            "Email": self.txEmail.get()
        }
        self.clientes.append(cliente)
        messagebox.showinfo("Información", "Cliente guardado exitosamente")

        # Limpiar campos de entrada
        self.txId.delete(0, tk.END)
        self.txNombre.delete(0, tk.END)
        self.txDireccion.delete(0, tk.END)
        self.txTelefono.delete(0, tk.END)
        self.txEmail.delete(0, tk.END)

        # Deshabilitar botones
        self.btSalvar.config(state=tk.DISABLED)
        self.btCancelar.config(state=tk.DISABLED)
        self.btEditar.config(state=tk.DISABLED)
        self.btEliminar.config(state=tk.DISABLED)

    def editar_cliente(self):
        id_cliente = self.txId.get()
        for cliente in self.clientes:
            if cliente["ID"] == id_cliente:
                cliente["Nombre"] = self.txNombre.get()
                cliente["Direccion"] = self.txDireccion.get()
                cliente["Telefono"] = self.txTelefono.get()
                cliente["Email"] = self.txEmail.get()
                messagebox.showinfo("Información", "Cliente editado exitosamente")

                # Limpiar campos de entrada
                self.txId.delete(0, tk.END)
                self.txNombre.delete(0, tk.END)
                self.txDireccion.delete(0, tk.END)
                self.txTelefono.delete(0, tk.END)
                self.txEmail.delete(0, tk.END)

                # Deshabilitar botones
                self.btEditar.config(state=tk.DISABLED)
                self.btCancelar.config(state=tk.DISABLED)
                return
        messagebox.showerror("Error", "Cliente no encontrado")

    def eliminar_cliente(self):
        id_cliente = self.txId.get()
        for cliente in self.clientes:
            if cliente["ID"] == id_cliente:
                self.clientes.remove(cliente)
                messagebox.showinfo("Información", "Cliente eliminado exitosamente")
                return
        messagebox.showerror("Error", "Cliente no encontrado")

    def cancelar(self):
        # Limpiar campos de entrada
        self.txId.delete(0, tk.END)
        self.txNombre.delete(0, tk.END)
        self.txDireccion.delete(0, tk.END)
        self.txTelefono.delete(0, tk.END)
        self.txEmail.delete(0, tk.END)

        # Deshabilitar botones
        self.btSalvar.config(state=tk.DISABLED)
        self.btCancelar.config(state=tk.DISABLED)
        self.btEditar.config(state=tk.DISABLED)
        self.btEliminar.config(state=tk.DISABLED)





class PestanaHabitaciones(ttk.Frame):
    def __init__(self, notebook, habitaciones):
        super().__init__(notebook)
        self.habitaciones = habitaciones

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.frameIngresarId = tk.Frame(self)
        self.frameIngresarId.grid(row=0, column=1, padx=10, pady=20)
        
        self.lbIngresarId = tk.Label(self.frameIngresarId, text="Ingrese Numero de Habitacion: ")
        self.lbIngresarId.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.txIngresarId = tk.Entry(self.frameIngresarId)
        self.txIngresarId.grid(row=0, column=1, padx=10, pady=5)

        # Botón de buscar
        self.btBuscar = tk.Button(self.frameIngresarId, text="Buscar", font=("Arial", 10, "bold"), command=self.buscar_habitacion)
        self.btBuscar.grid(row=0, column=2, padx=15)

        # Frame de entrada de datos
        self.frameEntradaDeDatos = tk.Frame(self)
        self.frameEntradaDeDatos.grid(row=1, column=1, padx=10)

        self.lbHabitacionId = tk.Label(self.frameEntradaDeDatos, text="Habitacion ID: ")
        self.lbHabitacionId.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.txHabitacionId = tk.Entry(self.frameEntradaDeDatos)
        self.txHabitacionId.grid(row=1, column=1, padx=10, pady=5)

        self.lbNumero = tk.Label(self.frameEntradaDeDatos, text="Numero: ")
        self.lbNumero.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.txNumero = tk.Entry(self.frameEntradaDeDatos)
        self.txNumero.grid(row=3, column=1, padx=10, pady=5)

        self.lbEstadoHabit = tk.Label(self.frameEntradaDeDatos, text="Seleccione Estado Habitación: ")
        self.lbEstadoHabit.grid(row=1, column=3, padx=10, sticky="e")
        self.cbEstadoHabit = ttk.Combobox(self.frameEntradaDeDatos, values=["Libre", "Reservado", "Cancelado"])
        self.cbEstadoHabit.grid(row=2, column=3, padx=10, pady=10)

        # Frame de Botones
        self.frameBotones = tk.Frame(self)
        self.frameBotones.grid(row=5, column=1)

        self.btNuevo = tk.Button(self.frameBotones, text="Nueva Habitación", font=("Arial", 10), command=self.nueva_habitacion)
        self.btNuevo.grid(row=3, column=2, padx=10, pady=10)

        self.btSalvar = tk.Button(self.frameBotones, text="Salvar", font=("Arial", 10), command=self.salvar_habitacion, state=tk.DISABLED)
        self.btSalvar.grid(row=3, column=3, padx=10, pady=10)

        self.btCancelar = tk.Button(self.frameBotones, text="Cancelar", font=("Arial", 10), command=self.cancelar, state=tk.DISABLED)
        self.btCancelar.grid(row=3, column=4, padx=10, pady=10)

        self.btEditar = tk.Button(self.frameBotones, text="Editar", font=("Arial", 10), command=self.editar_habitacion, state=tk.DISABLED)
        self.btEditar.grid(row=3, column=5, padx=10, pady=10)

    def nueva_habitacion(self):
        self.txHabitacionId.delete(0, tk.END)
        self.txNumero.delete(0, tk.END)
        self.cbEstadoHabit.set('')

        # Generar automáticamente el ID de la habitación
        nuevo_id = len(self.habitaciones) + 1
        self.txHabitacionId.insert(0, nuevo_id)

        # Habilitar botones
        self.btSalvar.config(state=tk.NORMAL)
        self.btCancelar.config(state=tk.NORMAL)
        self.btEditar.config(state=tk.NORMAL)

    def buscar_habitacion(self):
        id_habitacion = self.txIngresarId.get()
        for habitacion in self.habitaciones:
            if habitacion["ID"] == id_habitacion:
                self.txHabitacionId.delete(0, tk.END)
                self.txHabitacionId.insert(0, habitacion["ID"])
                self.txNumero.delete(0, tk.END)
                self.txNumero.insert(0, habitacion["Numero_Habitacion"])
                self.cbEstadoHabit.set(habitacion["Estado"])

                # Habilitar botones de Editar y Cancelar
                self.btEditar.config(state=tk.NORMAL)
                self.btCancelar.config(state=tk.NORMAL)
                return
        messagebox.showerror("Error", "Habitación no encontrada")


    def salvar_habitacion(self):
        habitacion = {
            "ID": self.txHabitacionId.get(),
            "Numero_Habitacion": self.txNumero.get(),
            "Estado": "Libre"
        }
        self.habitaciones.append(habitacion)
        messagebox.showinfo("Información", "Habitación guardada exitosamente")

        # Limpiar campos de entrada
        self.txHabitacionId.delete(0, tk.END)
        self.txNumero.delete(0, tk.END)
        self.cbEstadoHabit.set('')

        # Deshabilitar botones
        self.btSalvar.config(state=tk.DISABLED)
        self.btCancelar.config(state=tk.DISABLED)
        self.btEditar.config(state=tk.DISABLED)

    def editar_habitacion(self):
        id_habitacion = self.txHabitacionId.get()
        for habitacion in self.habitaciones:
            if habitacion["ID"] == id_habitacion:
                habitacion["Numero_Habitacion"] = self.txNumero.get()
                habitacion["Estado"] = self.cbEstadoHabit.get()
                messagebox.showinfo("Información", "Habitación editada exitosamente")

                # Limpiar campos de entrada
                self.txHabitacionId.delete(0, tk.END)
                self.txNumero.delete(0, tk.END)
                self.cbEstadoHabit.set('')

                # Deshabilitar botones
                self.btEditar.config(state=tk.DISABLED)
                self.btCancelar.config(state=tk.DISABLED)
                return
        messagebox.showerror("Error", "Habitación no encontrada")

    def cancelar(self):
        # Limpiar campos de entrada
        self.txHabitacionId.delete(0, tk.END)
        self.txNumero.delete(0, tk.END)
        self.cbEstadoHabit.set('')

        # Deshabilitar botones
        self.btSalvar.config(state=tk.DISABLED)
        self.btCancelar.config(state=tk.DISABLED)
        self.btEditar.config(state=tk.DISABLED)

class pestanaReservaciones(ttk.Frame):
    def __init__(self, notebook, reservaciones, clientes, habitaciones):
        super().__init__(notebook)
        self.reservaciones = reservaciones
        self.clientes = clientes
        self.habitaciones = habitaciones

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.frameIngresarId = tk.Frame(self)
        self.frameIngresarId.grid(row=0, column=1, padx=10, pady=20)

        # Etiquetas y Entradas para Reservaciones
        self.lbIngresarId = tk.Label(self.frameIngresarId, text="Ingrese Reservacion: ")
        self.lbIngresarId.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.txIngresarId = tk.Entry(self.frameIngresarId)
        self.txIngresarId.grid(row=0, column=1, padx=10, pady=5)

        # Botón de buscar
        self.btBuscar = tk.Button(self.frameIngresarId, text="Buscar Reservacion", font=("Arial", 10, "bold"), command=self.buscar_reservacion)
        self.btBuscar.grid(row=0, column=2, padx=15)

        # Frame para entrada de datos
        self.frameEntradaDeDatos = tk.Frame(self)
        self.frameEntradaDeDatos.grid(row=1, column=1, padx=10)

        # Entrada de datos de la reservación
        self.lbId = tk.Label(self.frameEntradaDeDatos, text="Reservacion ID: ")
        self.lbId.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.txId = tk.Entry(self.frameEntradaDeDatos)
        self.txId.grid(row=1, column=1, padx=10, pady=10)

        self.lbClienteID = tk.Label(self.frameEntradaDeDatos, text="Cliente ID: ")
        self.lbClienteID.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.cbClienteId = ttk.Combobox(self.frameEntradaDeDatos, values=[cliente["ID"] for cliente in self.clientes])
        self.cbClienteId.grid(row=2, column=1, padx=10, pady=10)

        self.lbHabitacionID = tk.Label(self.frameEntradaDeDatos, text="Habitacion ID: ")
        self.lbHabitacionID.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.cbHabitacionID = ttk.Combobox(self.frameEntradaDeDatos, values=[habitacion["ID"] for habitacion in self.habitaciones if habitacion["Estado"] == "Libre"])
        self.cbHabitacionID.grid(row=3, column=1, padx=10, pady=10)

        self.lbCosto = tk.Label(self.frameEntradaDeDatos, text="Costo: ")
        self.lbCosto.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.txCosto = tk.Entry(self.frameEntradaDeDatos)
        self.txCosto.grid(row=4, column=1, padx=10, pady=10)

        self.lbFechaReser = tk.Label(self.frameEntradaDeDatos, text="Fecha Reservacion: ")
        self.lbFechaReser.grid(row=1, column=3, padx=10, pady=10, sticky="e")
        self.txFechaReser = tk.Entry(self.frameEntradaDeDatos)
        self.txFechaReser.grid(row=1, column=4, padx=10, pady=10)

        self.lbFechaSalida = tk.Label(self.frameEntradaDeDatos, text="Fecha salida: ")
        self.lbFechaSalida.grid(row=2, column=3, padx=10, pady=10, sticky="e")
        self.txFechaSalida = tk.Entry(self.frameEntradaDeDatos)
        self.txFechaSalida.grid(row=2, column=4, padx=10, pady=10)

        self.lbHoraReser = tk.Label(self.frameEntradaDeDatos, text="Hora Reservación: ")
        self.lbHoraReser.grid(row=3, column=3, padx=10, pady=10, sticky="e")
        self.txHoraReser = tk.Entry(self.frameEntradaDeDatos)
        self.txHoraReser.grid(row=3, column=4, padx=10, pady=10)

        # Frame para botones
        self.frameBotones = tk.Frame(self)
        self.frameBotones.grid(row=5, column=1)

        self.btNuevo = tk.Button(self.frameBotones, text="Nueva Reservacion", font=("Arial", 10), command=self.nueva_reservacion)
        self.btNuevo.grid(row=5, column=1, padx=10, pady=10)

        self.btSalvar = tk.Button(self.frameBotones, text="Reservar", font=("Arial", 10), command=self.salvar_reservacion, state=tk.DISABLED)
        self.btSalvar.grid(row=5, column=2, padx=10, pady=10)

        self.btCancelar = tk.Button(self.frameBotones, text="Cancelar Reservacion", font=("Arial", 10), command=self.cancelar_reservacion, state=tk.DISABLED)
        self.btCancelar.grid(row=5, column=3, padx=10, pady=10)

        self.btEditar = tk.Button(self.frameBotones, text="Editar", font=("Arial", 10), command=self.editar_reservacion, state=tk.DISABLED)
        self.btEditar.grid(row=5, column=4, padx=10, pady=10)

    def nueva_reservacion(self):
        self.txId.delete(0, tk.END)
        self.cbClienteId.set('')
        self.cbHabitacionID.set('')
        self.txCosto.delete(0, tk.END)
        self.txFechaReser.delete(0, tk.END)
        self.txFechaSalida.delete(0, tk.END)
        self.txHoraReser.delete(0, tk.END)

        # Generar automáticamente el ID de la reservación
        nuevo_id = len(self.reservaciones) + 1
        self.txId.insert(0, nuevo_id)

        # Popular los menús desplegables
        self.cbClienteId['values'] = [cliente["ID"] for cliente in self.clientes]
        self.cbHabitacionID['values'] = [habitacion["ID"] for habitacion in self.habitaciones if habitacion["Estado"] == "Libre"]

        # Habilitar botones
        self.btSalvar.config(state=tk.NORMAL)
        self.btCancelar.config(state=tk.NORMAL)
        self.btEditar.config(state=tk.NORMAL)

    def buscar_reservacion(self):
        id_reservacion = self.txIngresarId.get()
        for reservacion in self.reservaciones:
            if reservacion["ReservacionID"] == id_reservacion:
                self.txId.delete(0, tk.END)
                self.txId.insert(0, reservacion["ReservacionID"])
                self.cbClienteId.set(reservacion["ClienteID"])
                self.cbHabitacionID.set(reservacion["HabitacionID"])
                self.txCosto.delete(0, tk.END)
                self.txCosto.insert(0, reservacion["Costo"])
                self.txFechaReser.delete(0, tk.END)
                self.txFechaReser.insert(0, reservacion["Fecha_Reservacion"])
                self.txFechaSalida.delete(0, tk.END)
                self.txFechaSalida.insert(0, reservacion["Fecha_Salida"])
                self.txHoraReser.delete(0, tk.END)
                self.txHoraReser.insert(0, reservacion["Hora_Reservacion"])

                # Habilitar botones de Editar y Cancelar
                self.btEditar.config(state=tk.NORMAL)
                self.btCancelar.config(state=tk.NORMAL)
                return
        messagebox.showerror("Error", "Reservación no encontrada")

    def salvar_reservacion(self):
        reservacion = {
            "ReservacionID": self.txId.get(),
            "ClienteID": self.cbClienteId.get(),
            "HabitacionID": self.cbHabitacionID.get(),
            "Fecha_Reservacion": self.txFechaReser.get(),
            "Hora_Reservacion": self.txHoraReser.get(),
            "Fecha_Salida": self.txFechaSalida.get(),
            "Costo": self.txCosto.get()
        }
        self.reservaciones.append(reservacion)
        for habitacion in self.habitaciones:
            if habitacion["ID"] == reservacion["HabitacionID"]:
                habitacion["Estado"] = "Reservado"
                break
        messagebox.showinfo("Información", "Reservación guardada exitosamente")

        # Limpiar campos de entrada
        self.txId.delete(0, tk.END)
        self.cbClienteId.set('')
        self.cbHabitacionID.set('')
        self.txCosto.delete(0, tk.END)
        self.txFechaReser.delete(0, tk.END)
        self.txFechaSalida.delete(0, tk.END)
        self.txHoraReser.delete(0, tk.END)

        # Deshabilitar botones
        self.btSalvar.config(state=tk.DISABLED)
        self.btCancelar.config(state=tk.DISABLED)
        self.btEditar.config(state=tk.DISABLED)

    def editar_reservacion(self):
        id_reservacion = self.txId.get()
        for reservacion in self.reservaciones:
            if reservacion["ReservacionID"] == id_reservacion:
                reservacion["ClienteID"] = self.cbClienteId.get()
                reservacion["HabitacionID"] = self.cbHabitacionID.get()
                reservacion["Fecha_Reservacion"] = self.txFechaReser.get()
                reservacion["Hora_Reservacion"] = self.txHoraReser.get()
                reservacion["Fecha_Salida"] = self.txFechaSalida.get()
                reservacion["Costo"] = self.txCosto.get()
                messagebox.showinfo("Información", "Reservación editada exitosamente")

                # Limpiar campos de entrada
                self.txId.delete(0, tk.END)
                self.cbClienteId.set('')
                self.cbHabitacionID.set('')
                self.txCosto.delete(0, tk.END)
                self.txFechaReser.delete(0, tk.END)
                self.txFechaSalida.delete(0, tk.END)
                self.txHoraReser.delete(0, tk.END)

                # Deshabilitar botones
                self.btEditar.config(state=tk.DISABLED)
                self.btCancelar.config(state=tk.DISABLED)
                return
        messagebox.showerror("Error", "Reservación no encontrada")

    def cancelar_reservacion(self):
        id_reservacion = self.tx

if __name__=="__main__":
    app=App()
    app.mainloop()
