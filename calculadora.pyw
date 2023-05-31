from tkinter import *

raiz=Tk()

miFrame=Frame(raiz)
miFrame.pack()

titulo=Label(miFrame, text="Calculadora",fg="blue")
titulo.grid(row=0, column=1)

# ---------- Pantalla ---------- #

cuadroResultado=Entry(miFrame, justify="center", fg="green")
cuadroResultado.grid(row=1, column=1)

# ------------------------------ #

# ---------- Primera Linea ---------- #

cajaBotones=Frame(miFrame)
cajaBotones.grid(row=2, column=1)

boton7=Button(cajaBotones, text="7")
boton7.grid(row=0, column=0)
boton7.config(padx=5, pady=5)

boton8=Button(cajaBotones, text="8")
boton8.grid(row=0, column=1)
boton8.config(padx=5, pady=5)

boton9=Button(cajaBotones, text="9")
boton9.grid(row=0, column=2)
boton9.config(padx=5, pady=5)

botonDivision=Button(cajaBotones, text="/")
botonDivision.grid(row=0, column=3)
botonDivision.config(padx=5, pady=5)

# ------------------------------ #

# ---------- Segunda Linea ---------- #

boton4=Button(cajaBotones, text="4")
boton4.grid(row=1, column=0)
boton4.config(padx=5, pady=5)

boton5=Button(cajaBotones, text="5")
boton5.grid(row=1, column=1)
boton5.config(padx=5, pady=5)

boton6=Button(cajaBotones, text="6")
boton6.grid(row=1, column=2)
boton6.config(padx=5, pady=5)

botonMulti=Button(cajaBotones, text="x")
botonMulti.grid(row=1, column=3)
botonMulti.config(padx=5, pady=5)

# ------------------------------ #

# ---------- Tercera Linea ---------- #

boton1=Button(cajaBotones, text="1")
boton1.grid(row=2, column=0)
boton1.config(padx=5, pady=5)

boton2=Button(cajaBotones, text="2")
boton2.grid(row=2, column=1)
boton2.config(padx=5, pady=5)

boton3=Button(cajaBotones, text="3")
boton3.grid(row=2, column=2)
boton3.config(padx=5, pady=5)

botonPlus=Button(cajaBotones, text="+")
botonPlus.grid(row=2, column=3)
botonPlus.config(padx=5, pady=5)

# ------------------------------ #

# ---------- Cuarta Linea ---------- #

boton0=Button(cajaBotones, text="0")
boton0.grid(row=3, column=1)
boton0.config(padx=5, pady=5)

botonDecimal=Button(cajaBotones, text=",")
botonDecimal.grid(row=3, column=2)
botonDecimal.config(padx=5, pady=5)

botonResta=Button(cajaBotones, text="-")
botonResta.grid(row=3, column=3)
botonResta.config(padx=5, pady=5)

botonIgual=Button(cajaBotones, text="=")
botonIgual.grid(row=4, column=0, columnspan=2)
botonIgual.config(padx=20, pady=5)

raiz.mainloop()