import tkinter as ventana
from tkinter import messagebox
from usuario import Usuario
from carro import Carro
from parqueadero import Parqueadero

registros = []  

def actualizar_lista():
    lb_registros.delete(0, ventana.END)
    for idx, reg in enumerate(registros):
        p = reg["parqueadero"]  
        estado = p.estado
        resumen = f"{idx+1}. {p.puesto} - {reg['carro'].placa} ({estado})"
        lb_registros.insert(ventana.END, resumen)


def mostrar_detalle(event=None):
    sel = lb_registros.curselection()
    if not sel:
        return
    idx = sel[0]
    reg = registros[idx]
    u = reg["usuario"]
    c = reg["carro"]
    p = reg["parqueadero"]
    detalle = (
        f"Usuario:\n  Nombre: {u.nombre}\n  Cédula: {u.cedula}\n  Tipo: {u.tipo_usuario}\n\n"
        f"Carro:\n  Placa: {c.placa}\n  Marca: {c.marca}\n  Color: {c.color}\n\n"
        f"Parqueadero:\n  Puesto: {p.puesto}\n  Fecha entrada: {p.fecha_entrada}\n  Hora entrada: {p.hora_entrada}\n  Hora salida: {p.hora_salida if p.hora_salida else 'Pendiente'}\n  Estado: {p.estado}"
    )
    txt_detalle.config(state=ventana.NORMAL)
    txt_detalle.delete(1.0, ventana.END)
    txt_detalle.insert(ventana.END, detalle)
    txt_detalle.config(state=ventana.DISABLED)


def agregar_registro():
    nombre = ent_nombre.get().strip()
    cedula = ent_cedula.get().strip()
    tipo = ent_tipo.get().strip()
    placa = ent_placa.get().strip()
    marca = ent_marca.get().strip()
    color = ent_color.get().strip()
    puesto = ent_puesto.get().strip()
    fecha = ent_fecha.get().strip()
    hora = ent_hora.get().strip()

    if not (nombre and cedula and tipo and placa and marca and color and puesto and fecha and hora):
        messagebox.showwarning("Campos incompletos", "Por favor completa todos los campos antes de agregar.")
        return

    usuario = Usuario(cedula, nombre, tipo)
    carro = Carro(placa, marca, color)
    parqueadero = Parqueadero(puesto, fecha, hora)

    registros.append({"usuario": usuario, "carro": carro, "parqueadero": parqueadero})
    actualizar_lista()
    limpiar_campos()


def limpiar_campos():
    ent_nombre.delete(0, ventana.END)
    ent_cedula.delete(0, ventana.END)
    ent_tipo.delete(0, ventana.END)
    ent_placa.delete(0, ventana.END)
    ent_marca.delete(0, ventana.END)
    ent_color.delete(0, ventana.END)
    ent_puesto.delete(0, ventana.END)
    ent_fecha.delete(0, ventana.END)
    ent_hora.delete(0, ventana.END)


def registrar_salida():
    """Registra la hora de salida del registro seleccionado"""
    sel = lb_registros.curselection()
    if not sel:
        messagebox.showinfo("Seleccionar", "Selecciona un registro en la lista.")
        return
    idx = sel[0]
    hora_s = ent_hora_salida.get().strip()
    if not hora_s:
        messagebox.showwarning("Hora salida", "Ingresa  hora de salida.")
        return
    registros[idx]["parqueadero"].registrar_salida(hora_s)
    actualizar_lista()
    mostrar_detalle()



root = ventana.Tk()
root.title("Parqueadero")

frm_entrada = ventana.Frame(root, padx=10, pady=10)
frm_entrada.pack(side=ventana.TOP, fill=ventana.X)

lbl_nombre = ventana.Label(frm_entrada, text="Nombre:")
lbl_nombre.grid(row=0, column=0, sticky=ventana.W)
ent_nombre = ventana.Entry(frm_entrada)
ent_nombre.grid(row=0, column=1)

lbl_cedula = ventana.Label(frm_entrada, text="Cédula:")
_lbl_cedula = lbl_cedula
lbl_cedula.grid(row=1, column=0, sticky=ventana.W)
ent_cedula = ventana.Entry(frm_entrada)
ent_cedula.grid(row=1, column=1)

lbl_tipo = ventana.Label(frm_entrada, text="Tipo usuario:")
_lbl_tipo = lbl_tipo
lbl_tipo.grid(row=2, column=0, sticky=ventana.W)
ent_tipo = ventana.Entry(frm_entrada)
ent_tipo.grid(row=2, column=1)

lbl_placa = ventana.Label(frm_entrada, text="Placa:")
lbl_placa.grid(row=0, column=2, sticky=ventana.W)
ent_placa = ventana.Entry(frm_entrada)
ent_placa.grid(row=0, column=3)

lbl_marca = ventana.Label(frm_entrada, text="Marca:")
lbl_marca.grid(row=1, column=2, sticky=ventana.W)
ent_marca = ventana.Entry(frm_entrada)
ent_marca.grid(row=1, column=3)

lbl_color = ventana.Label(frm_entrada, text="Color:")
lbl_color.grid(row=2, column=2, sticky=ventana.W)
ent_color = ventana.Entry(frm_entrada)
ent_color.grid(row=2, column=3)

lbl_puesto = ventana.Label(frm_entrada, text="Puesto:")
lbl_puesto.grid(row=3, column=0, sticky=ventana.W)
ent_puesto = ventana.Entry(frm_entrada)
ent_puesto.grid(row=3, column=1)

lbl_fecha = ventana.Label(frm_entrada, text="Fecha entrada:")
lbl_fecha.grid(row=3, column=2, sticky=ventana.W)
ent_fecha = ventana.Entry(frm_entrada)
ent_fecha.grid(row=3, column=3)

lbl_hora = ventana.Label(frm_entrada, text="Hora entrada:")
lbl_hora.grid(row=4, column=0, sticky=ventana.W)
ent_hora = ventana.Entry(frm_entrada)
ent_hora.grid(row=4, column=1)

btn_agregar = ventana.Button(frm_entrada, text="Agregar registro", command=agregar_registro)
btn_agregar.grid(row=4, column=3, pady=5)

frm_lista = ventana.Frame(root, padx=10, pady=10)
frm_lista.pack(side=ventana.LEFT, fill=ventana.BOTH, expand=True)

lb_registros = ventana.Listbox(frm_lista, width=40, height=15)
lb_registros.pack(side=ventana.TOP, fill=ventana.BOTH, expand=True)
lb_registros.bind("<<ListboxSelect>>", mostrar_detalle)


frm_detalle = ventana.Frame(root, padx=10, pady=10)
frm_detalle.pack(side=ventana.RIGHT, fill=ventana.BOTH, expand=True)

txt_detalle = ventana.Text(frm_detalle, width=50, height=15, state=ventana.DISABLED)
txt_detalle.pack()

lbl_hora_salida = ventana.Label(frm_detalle, text="Hora salida:")
lbl_hora_salida.pack(anchor=ventana.W)
ent_hora_salida = ventana.Entry(frm_detalle)
ent_hora_salida.pack(anchor=ventana.W)

btn_salida = ventana.Button(frm_detalle, text="Registrar salida", command=registrar_salida)
btn_salida.pack(pady=5)


root.mainloop()
