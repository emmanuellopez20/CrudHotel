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
        self.notebook.pack (expand=1, fill="both")

        self.crearPestanas()

    def crearPestanas(self):
        #Creamos los frames de cada pestaña
        self.pestana_Clientes = pestanaClientes(self.notebook)
        self.pestana_Reservaciones = pestanaReservaciones(self.notebook)
        self.pestana_Habitaciones = PestanaHabitaciones(self.notebook)

        #Añadir las pestañas al notebook
        self.notebook.add(self.pestana_Clientes, text="Clientes")
        self.notebook.add(self.pestana_Reservaciones, text="Reservaciones")
        self.notebook.add(self.pestana_Habitaciones, text="Habitaciones")
    
class pestanaClientes(ttk.Frame):
    def __init__(self, notebook):
        super().__init__(notebook)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        #Frame para Id del cliente
        self.frameIngresarId = tk.Frame(self)
        self.frameIngresarId.grid(row=0, column=1, padx=10, pady=20)

        #Etiquetas y Entradas para Clientes
        self.lbIngresarId = tk.Label(self.frameIngresarId, text="Ingrese ID del Cliente: ")
        self.lbIngresarId.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.txIngresarId = tk.Entry(self.frameIngresarId, width=30)
        self.txIngresarId.grid(row=0, column=1, padx=10, pady=5)

        #Boton de buscar
        self.btBuscar = tk.Button(self.frameIngresarId, text="Buscar", font=("Arial",10, "bold"))
        self.btBuscar.grid(row=0, column=2, padx=15)

        #Frame para entrys de datos
        self.frameEntradaDeDatos = tk.Frame(self)
        self.frameEntradaDeDatos.grid(row=1, column=1, padx=10)

        #Entrada de datos del cliente
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

        self.lbTelefono = tk.Label(self.frameEntradaDeDatos, text="Telefono: ")
        self.lbTelefono.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.txTelefono = tk.Entry(self.frameEntradaDeDatos)
        self.txTelefono.grid(row=4, column=1, padx=10, pady=10)

        self.lbEmail = tk.Label(self.frameEntradaDeDatos, text="Email: ")
        self.lbEmail.grid(row=2, column=3, padx=10, pady=10, sticky="w")
        self.txEmail = tk.Entry(self.frameEntradaDeDatos)
        self.txEmail.grid(row=2, column=4, padx=10, pady=10)

        #Frame para botones
        self.frameBotones = tk.Frame(self)
        self.frameBotones.grid(row=5, column=1)

        self.btNuevo = tk.Button(self.frameBotones, text="Nuevo", font=("Arial", 10))
        self.btNuevo.grid(row=1, column=1, padx=10, pady=10)

        self.btSalvar = tk.Button(self.frameBotones, text="Salvar", font=("Arial", 10))
        self.btSalvar.grid(row=1, column=2, padx=10, pady=10)

        self.btCancelar = tk.Button(self.frameBotones, text="Cancelar", font=("Arial", 10))
        self.btCancelar.grid(row=1, column=3, padx=10, pady=10)

        self.btEditar = tk.Button(self.frameBotones, text="Editar", font=("Arial", 10))
        self.btEditar.grid(row=1, column=4, padx=10, pady=10)

        self.btEliminar = tk.Button(self.frameBotones, text="Eliminar", font=("Arial", 10))
        self.btEliminar.grid(row=1, column=5, padx=10, pady=10)


class pestanaReservaciones(ttk.Frame):
    def __init__(self, notebook):
        super().__init__(notebook)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.frameIngresarId = tk.Frame(self)
        self.frameIngresarId.grid(row=0, column=1, padx=10, pady=20)

        #Etiquetas y Entradas para Clientes
        self.lbIngresarId = tk.Label(self.frameIngresarId, text="Ingrese Reservacion: ")
        self.lbIngresarId.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.txIngresarId = tk.Entry(self.frameIngresarId)
        self.txIngresarId.grid(row=0, column=1, padx=10, pady=5)

        #Boton de buscar
        self.btBuscar = tk.Button(self.frameIngresarId, text="Buscar Reservacion", font=("Arial",10, "bold"))
        self.btBuscar.grid(row=0, column=2, padx=15)

        #Frame para entrada de datos
        self.frameEntradaDeDatos = tk.Frame(self)
        self.frameEntradaDeDatos.grid(row=1, column=1, padx=10)

        #Entrada de datos del cliente
        self.lbId = tk.Label(self.frameEntradaDeDatos, text="Reservacion ID: ")
        self.lbId.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.txId = tk.Entry(self.frameEntradaDeDatos)
        self.txId.grid(row=1, column=1, padx=10, pady=10)

        self.lbClienteID = tk.Label(self.frameEntradaDeDatos, text="Cliente ID: ")
        self.lbClienteID.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.cbClienteId = ttk.Combobox(self.frameEntradaDeDatos, values="")
        self.cbClienteId.grid(row=2, column=1, padx=10, pady=10)

        self.lbHatacionID = tk.Label(self.frameEntradaDeDatos, text="Habitacion ID: ")
        self.lbHatacionID.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.cbHabitacionID = ttk.Combobox(self.frameEntradaDeDatos, values="")
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

        #Frame para botones
        self.frameBotones = tk.Frame(self)
        self.frameBotones.grid(row=5, column=1)

        self.btNuevo = tk.Button(self.frameBotones, text="Nueva Reservacion", font=("Arial", 10))
        self.btNuevo.grid(row=5, column=1, padx=10, pady=10)

        self.btSalvar = tk.Button(self.frameBotones, text="Reservar", font=("Arial", 10))
        self.btSalvar.grid(row=5, column=2, padx=10, pady=10)

        self.btCancelar = tk.Button(self.frameBotones, text="Cancelar Reservacion", font=("Arial", 10))
        self.btCancelar.grid(row=5, column=3, padx=10, pady=10)

        self.btEditar = tk.Button(self.frameBotones, text="Editar", font=("Arial", 10))
        self.btEditar.grid(row=5, column=4, padx=10, pady=10)

class PestanaHabitaciones(ttk.Frame):
    def __init__(self, notebook):
        super().__init__(notebook)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.frameIngresarId = tk.Frame(self)
        self.frameIngresarId.grid(row=0, column=1, padx=10, pady=20)
        
        self.lbIngresarId = tk.Label(self.frameIngresarId, text="Ingrese Numero de Habitacion: ")
        self.lbIngresarId.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.txIngresarId = tk.Entry(self.frameIngresarId)
        self.txIngresarId.grid(row=0, column=1, padx=10, pady=5)

        #Boton de buscar
        self.btBuscar = tk.Button(self.frameIngresarId, text="Buscar", font=("Arial",10, "bold"))
        self.btBuscar.grid(row=0, column=2, padx=15)

        #Frame de entrada de datos
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
        self.cbClienteId = ttk.Combobox(self.frameEntradaDeDatos, values="")
        self.cbClienteId.grid(row=2, column=3, padx=10, pady=10)

        #Frame de Botones
        self.frameBotones = tk.Frame(self)
        self.frameBotones.grid(row=5, column=1)

        self.btNuevo = tk.Button(self.frameBotones, text="Nueva Habitación", font=("Arial", 10))
        self.btNuevo.grid(row=3, column=2, padx=10, pady=10)

        self.btEditar = tk.Button(self.frameBotones, text="Editar", font=("Arial", 10))
        self.btEditar.grid(row=3, column=3, padx=10, pady=10)


if __name__=="__main__":
    app=App()
    app.mainloop()
