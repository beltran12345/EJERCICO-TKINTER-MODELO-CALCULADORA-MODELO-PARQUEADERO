from modelo_usuario import Usuario
from modelo_numero import Numero
from modelo_calculadora import Calculadora
import tkinter as ventana

object_ventana = ventana.Tk()
object_ventana.title("REGISTRO DE USUARIO")
object_ventana.geometry("900x800")
object_ventana.config(bg="black")
object_ventana.resizable(False, True) 

titulo_label = ventana.Label(object_ventana, text="REGISTRO DE USUARIO")
titulo_label.config(bg="PINK", font=("Arial", 20), fg="white")
titulo_label.pack()

seccio1 = ventana.Frame(object_ventana)
seccio1.pack(pady=10)

titulo_seccio1 = ventana.Label(seccio1, text="Datos del usuario")
seccio1.config(bg="white")
titulo_seccio1.pack()

label_nombre = ventana.Label(seccio1, text="Digite el nombre:", font=("Arial", 14))
label_nombre.pack(pady=5)

entry_nombre = ventana.Entry(seccio1, width=20, font=("Arial", 12))
entry_nombre.pack(pady=5)

label_id = ventana.Label(seccio1, text="Digite el ID:", font=("Arial", 14))
label_id.pack(pady=5)

entry_id = ventana.Entry(seccio1, width=20, font=("Arial", 12))
entry_id.pack(pady=5)

button_borrar_user = ventana.Button(seccio1, text="Borrar", command=lambda: [entry_nombre.delete(0, ventana.END), entry_id.delete(0, ventana.END)], bg="red", fg="white", font=("Arial", 12))
button_borrar_user.pack(pady=5)

# ===== SECCION 2: CALCULADORA =====

titulo_label2 = ventana.Label(object_ventana, text="REGISTRO DE OPERACION")
titulo_label2.config(bg="black", font=("Arial", 20), fg="white")
titulo_label2.pack(pady=10)

seccion2 = ventana.Frame(object_ventana)
seccion2.pack(pady=10)

titulo_seccio2 = ventana.Label(seccion2, text="Calculadora")
seccion2.config(bg="white")
titulo_seccio2.pack()

label_calc = ventana.Label(seccion2, text="Ingrese operacion:", font=("Arial", 14))
label_calc.pack(pady=5)

entry_operacion = ventana.Entry(seccion2, width=30, font=("Arial", 12))
entry_operacion.pack(pady=5)

button_resultado = ventana.Button(seccion2, text="Imprimir resultado", command=lambda: [entry_resultados.delete(0, ventana.END), entry_resultados.insert(0, str(eval(entry_operacion.get())))], bg="blue", fg="white", font=("Arial", 12))
button_resultado.pack(pady=5)


button_borrar_calc = ventana.Button(seccion2, text="Borrar resultado", command=lambda: entry_operacion.delete(0, ventana.END), bg="red", fg="white", font=("Arial", 12))
button_borrar_calc.pack(pady=5)

butto_numero1=  ventana.Button(seccion2, text="1",command=lambda: entry_operacion.insert(ventana.END, "1"))
butto_numero1.pack()

butto_numero2  = ventana.Button(seccion2, text="2", command=lambda: entry_operacion.insert(ventana.END, "2"))
butto_numero2.pack()

button_suma = ventana.Button(seccion2, text="+", command=lambda: entry_operacion.insert(ventana.END, "+"), bg="orange", fg="white", font=("Arial", 12))

button_suma.pack(pady=5)

button_resta = ventana.Button(seccion2, text="-", command=lambda: entry_operacion.insert(ventana.END, "-"), bg="orange", fg="white", font=("Arial", 12))
button_resta.pack(pady=5)

button_multiplicacion = ventana.Button(seccion2, text="*", command=lambda: entry_operacion.insert(ventana.END, "*"), bg="orange", fg="white", font=("Arial", 12))
button_multiplicacion.pack(pady=5)

butto_divicion = ventana.Button(seccion2, text="/", command=lambda: entry_operacion.insert(ventana.END, "/"), bg="orange", fg="white", font=("Arial", 12))
butto_divicion.pack(pady=5)


# ===== SECCION 3: DATOS DE RESULTADOS =====


titulo_label3 = ventana.Label(object_ventana, text="DATOS DE RESULTADOS")
titulo_label3.config(bg="black", font=("Arial", 20), fg="white")
titulo_label3.pack(pady=10)

seccion3 = ventana.Frame(object_ventana)
seccion3.pack(pady=10)

titulo_seccio3 = ventana.Label(seccion3, text="Resultados")
seccion3.config(bg="white")
titulo_seccio3.pack()

label_resultados = ventana.Label(seccion3, text="Datos de resultados:", font=("Arial", 14))
label_resultados.pack(pady=5)

entry_resultados = ventana.Entry(seccion3, width=30, font=("Arial", 12))
entry_resultados.pack(pady=5)
button_guardar = ventana.Button(seccio1, text="Guardar", command=lambda: Usuario(entry_nombre.get(), entry_id.get()), bg="green", fg="white", font=("Arial", 12))
button_guardar.pack(pady=5)

button_borrar_user = ventana.Button(seccio1, text="Borrar", command=lambda: [entry_nombre.delete(0, ventana.END), entry_id.delete(0, ventana.END)], bg="red", fg="white", font=("Arial", 12))
button_borrar_user.pack(pady=5)



object_ventana.mainloop()
    
    