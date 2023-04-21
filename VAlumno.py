# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 20:00:37 2022

@author: David Betancourt
"""

from tkinter import *

window=Tk()

window.resizable(False,False)
window.title("Registro para el alumno")
window.geometry("600x600")

panel=Frame()
panel.pack()
panel.config(width="600",height="600")
panel.config(bg="blue")

titulo=Label(text="Registro de Alumno")
titulo.pack()
titulo.place(x=190,y=50)



nombrea=Label(text="Nombre")
nombrea.pack()
nombrea.place(x=90, y=120)

txtNombrea=Entry()
txtNombrea.pack()
txtNombrea.place(x=182,y=100)


apellido1a=Label(text="Apellido Paterno")
apellido1a.pack()
apellido1a.place(x=90, y=170)

txtApellido1a=Entry()
txtApellido1a.pack()
txtApellido1a.place(x=182, y=150)



apellido2a=Label(text="Apellido Materno")
apellido2a.pack()
apellido2a.place(x=90, y=220)

txtApellido2a=Entry()
txtApellido2a.pack()
txtApellido2a.place(x=182, y=200)



emaila=Label(text="Email")
emaila.pack()
emaila.place(x=90, y=270)

txtEmaila=Entry()
txtEmaila.pack()
txtEmaila.place(x=182,y=270)

boleta=Label(text="Boleta")
boleta.pack()
boleta.place(x=90, y=300)

txtBoleta=Entry()
txtBoleta.pack()
txtBoleta.place(x=182, y=300)

grupoa=Label(text="Grupo")
grupoa.pack()
grupoa.place(x=90, y=350)

txtGrupoa=Entry()
txtGrupoa.pack()
txtGrupoa.place(x=182,y=350)



def boton1():

  from tkinter import messagebox
  
  
  nombrea=txtNombrea.get()
  apatera=txtApellido1a.get()
  amatera=txtApellido2a.get()
  boleta=txtBoleta.get()
  grupoa=txtGrupoa.get()
  emaila=txtEmaila.get()




  if(nombrea=="" or apatera=="" or amatera=="" or boleta=="" or grupoa=="" or emaila==""):
    messagebox("Información","Ingresa toda la información")

  else:

    from DatosA import DatosA
    
    
    DatosA=DatosA(nombrea,apatera,amatera,boleta,grupoa,emaila)
    DatosA.imprime()


btnRegistrar=Button(command=boton1,text="Registrar Maestro")
btnRegistrar.pack()
btnRegistrar.place(x=550,y=200)

btnConsultar=Button(command=boton1,text="Consultar")
btnConsultar.pack()
btnConsultar.place(x=550,y=450)

mainloop()