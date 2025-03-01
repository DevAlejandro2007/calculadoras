# Importar la libreria que usaremos 
import tkinter as tk

#Inicializacion de la ventana 
ventana = tk.Tk()
ventana.title("CALCULADORA")
ventana.geometry("600x200")
ventana.config(background="red")

#Entrada de datos x,y que seran los valores con lo que operar
a = tk.Entry(master = ventana,font="ARIAL 15", width = 10)
b = tk.Entry(master = ventana,font= "ARIAL 15", width = 10)

texto_1 = tk.Label(master = ventana, text = "Ingrese el primer número: ", font="ARIAL 15",bg ="red") 
texto_1.place(x = 40, y= 0)

texto_2 = tk.Label(master = ventana, text = "Ingrese el segundo número: ", font="ARIAL 15",bg ="red")
texto_2.place(x = 40, y = 60)
a.place(x = 40, y = 30)
b.place(x=40, y =90)

salida = tk.Label(master=ventana, text = "", font="ARIAL 15", bg = "red")
salida.place(x = 480, y =20)

# Botones y funciones que realizan dichos botones
boton_suma = tk.Button(master = ventana, text= "SUMA",bg ="steel blue", border = 3, command= lambda: suma(a.get(), b.get()))
boton_suma.place(x = 40, y = 140)
def suma(x,y):
    x = int (x)
    y = int(y)
    resultado = x+y
    limpiar_celda()
    resultados(resultado)



boton_resta = tk.Button(master= ventana,text = "RESTA", bg = "steel blue", border = 3, command = lambda: resta(a.get(),b.get()))
boton_resta.place(x = 100, y = 140)
def resta(x,y):
    x = int(x)
    y = int(y)
    resultado = x-y
    limpiar_celda()
    resultados(resultado)


boton_mult = tk.Button(master = ventana, text = "MULTIPLICACIÓN", bg = "steel blue", border = 3, command= lambda: multiplicacion(a.get(),b.get()))
boton_mult.place(x= 160, y = 140)   
def multiplicacion(x,y):
    x = int(x)
    y = int(y)
    resultado = x*y
    limpiar_celda()
    resultados(resultado)


boton_div = tk.Button(master=ventana, text="DIVICION", bg = "steel blue", border = 3, command = lambda: division(a.get(),b.get()))
boton_div.place(x=280, y = 140)
def division(x,y):
    x = int(x)
    y = int(y)
    if y != 0:
        resultado = x/y
    else:
        resultado = "No se puede dividir entre cero"
    limpiar_celda()
    resultados(resultado)


boton_mcm = tk.Button(master= ventana, text="MINIMO COMUN",bg = "steel blue", border = 3, command = lambda: mcm(a.get(),b.get()))
boton_mcm.place(x = 360, y = 140)
def mcm(x, y):
    x = int(x)
    y = int(y)    
    mcd = mcdiv(x, y)  
    mcm = abs(x * y) // mcd
    limpiar_celda()
    resultados(mcm)


def mcdiv(x, y):
    x = int(x)
    y = int(y)
    while y != 0:
        x, y = y, x % y 
    return x

boton_mcd = tk.Button(master = ventana, text="MINIMO DIVISOR", bg = "steel blue", border = 3, command= lambda: mcdivi(a.get(),b.get()))
boton_mcd.place(x = 480, y = 140)
def mcdivi(x, y):
    x = int(x)
    y = int(y)
    limpiar_celda()
    resultados(mcdiv(x,y))



def resultados(z):
    salida.config(text=str(z))

def limpiar_celda():
    a.delete(0,-1)
    b.delete(0,-1)

ventana.mainloop()

