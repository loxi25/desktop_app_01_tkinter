# se importala libreria tkinter con todas sus funciones 
from tkinter import *

# _________________________________
# funciones de la app 
#__________________________________



#_____________________________
#  ventana principal de la aplicacion
#_____________________________


# se declara una variable llamada ventana-principal , que adquiere las caracteristicas en un objeto de tipo TK()


ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("oscar eduardo sanchez payares") 





# tamaño de la ventana 
ventana_principal.geometry("800x500")

# deshabilitar el boton de maximizar
ventana_principal.resizable(0,0)

# color de fondo de la ventana 
ventana_principal.config(bg="green")

#------
# frame 1
#------

frame_1 = Frame(ventana_principal)
frame_1.config(bg="yellow", width=780 , height=240)
frame_1.place(x=10, y=18 )


#---------
# frame 2 
#---------
frame_2 = Frame(ventana_principal)
frame_2.config(bg="blue", width=780 , height=128)
frame_2.place(x =10  , y = 250)

frame_3 = Frame(ventana_principal)
frame_3.config(bg="red", width=788 , height=128)
frame_3.place(x = 10 , y = 370)




# metodo principal que despliega la ventana en pantalla
ventana_principal.mainloop()


# 

