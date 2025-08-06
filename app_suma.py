# se importa la libreria tkinter con todas sus funciones
# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox
#------------------------------
# Funciones de la app
#------------------------------

def sumar():
    messagebox.showinfo("suma 1.0", "se sumaran los dos numeros...")
    

def borrar():
    messagebox.showinfo("suma 1.0", "los datos seran borrados...")
    a.set("")
    b.set("")
    t_resultado.delete("1.0","end")

def salir():
    messagebox.showinfo("suma 1.0", "la app se cerrará...")
    Ventana_principal.destroy()
#------------------------------
# Ventana principal de la app
#------------------------------

# se declara una variable llamada ventana principal que adquiere las características de un objeto tipo Tk()

Ventana_principal = Tk()

#Titulo de la ventana

Ventana_principal.title("oscar eduardo sanchez payarez")

#tamaño de la ventana
Ventana_principal.geometry("800x500")

#Deshabilitar el botón de maximizar de la ventana
Ventana_principal.resizable(0,0)

#color de fondo de la ventana

Ventana_principal.config(bg="black")


#-------------------------------
#variables globales
#-------------------------------

a=StringVar()
b=StringVar()
c=IntVar()

#-------------------------------
#Frame_1 - entrada de datos
#-------------------------------
frame_1 = Frame(Ventana_principal)
frame_1.config(bg="ivory2",width=780, height=200)
frame_1.place(x=10,y=10)

#-------------------------------
#Titulo
#-------------------------------
titulo = Label(frame_1, text="Colegio San José de Guanentá")
titulo.config(bg="yellow", fg="blue", font=("Arial", 18))
titulo.place(x=390, y=10)

#-------------------------------
#imagen= logo de la app
#-------------------------------

logo=PhotoImage(file="img/btn-suma.png")
label_logo = Label(frame_1, image=logo)
label_logo.place(x=10,y=10)

#-------------------------------
#etiqueta para el titulo 
#-------------------------------

#titulo= Label(frame_1, text="Colegio San José de Guanentá")
#titulo.config(bg="yellow",fg="blue", font=("Arial", 16))
#titulo.place(x=390,y=10)

#-------------------------------
#etiqueta para subtitulo 1 de la app
#-------------------------------

subtitulo1= Label(frame_1, text= "Especialidad en sistemas")
subtitulo1.config(bg="yellow",fg="blue", font=("Arial",12))
subtitulo1.place(x=390,y=40)

#-------------------------------
#etiqueta para subtitulo 2 de la app
#-------------------------------

subtitulo2=Label(frame_1, text="SUMA DE DOS NUMEROS ENTEROS")
subtitulo2.config(bg="ivory2", fg="blue",font=("Arial", 15), anchor=CENTER)
subtitulo2.place(x=390,y=70)

#-------------------------------
#etiqueta para el primer valor
#-------------------------------

Label_a=Label(frame_1, text="a =")
Label_a.config(bg="ivory2", fg="blue",font=("Arial", 20), anchor=CENTER)
Label_a.place(x=390,y=120)

#-------------------------------
#Entry para el primer valor
#-------------------------------
entry_a=Entry(frame_1,width=4, textvariable=a)
entry_a.config(font=("Arial",20),justify=CENTER)
entry_a.focus_set()
entry_a.place(x=427,y=120)

#-------------------------------
#etiqueta para el segundo valor
#-------------------------------
Label_b=Label(frame_1, text="b =")
Label_b.config(bg="ivory2", fg="blue",font=("Arial", 20), anchor=CENTER)
Label_b.place(x=540,y=120)




#-------------------------------
#entry para el segundo valor
#-------------------------------
entry_b=Entry(frame_1,width=4, textvariable=b)
entry_b.config(font=("Arial",20),justify=CENTER)
entry_b.place(x=585,y=120)



#-------------------------------
#Frame 2 - operaciones
#-------------------------------
frame_2 = Frame(Ventana_principal)
frame_2.config(bg="ivory2",width=780, height=125)
frame_2.place(x=10,y=230)



img_bt_sumar = PhotoImage(file = "img/boton_sumar.png")
#-------------------------------
# boton para sumar bt_sumar = Button(frame_2, text = "sumar", width=10)

bt_sumar = Button(frame_2 , image = img_bt_sumar, width = 105, height = 105, command = sumar)
bt_sumar.place(x=116, y=7)

# boton para borrar
img_bt_borrar = PhotoImage(file="img/boton_borrar.png")
#-------------------------------
# boton para sumar bt_sumar = Button(frame_2, text = "sumar", width=10)

bt_borrar = Button(frame_2 , image = img_bt_borrar, width = 105, height = 105, command=borrar)
bt_borrar.place(x=337, y=7)

# boton para cerrar la app
img_bt_salir = PhotoImage(file="img/boton_salir.png")
#-------------------------------
# boton para sumar bt_sumar = Button(frame_2, text = "sumar", width=10)

bt_salir = Button(frame_2 , image = img_bt_salir, width = 105, height = 105, command=salir)
bt_salir.place(x=558, y=7)

#-------------------------------
#Frame 3 - resultado
#-------------------------------
frame_3 = Frame(Ventana_principal)
frame_3.config(bg="ivory2",width=780, height=125)
frame_3.place(x=10,y=370)

# area de texto
t_resultado = Text(frame_3, width = 50, height=3)
t_resultado.config(bg="green", fg = "white", font = ("courier",20))
t_resultado.pack()

#metodo principal que despliega la ventana en pantalla
Ventana_principal.mainloop()



