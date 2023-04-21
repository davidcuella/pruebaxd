# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 20:00:39 2022

@author: David Betancourt
"""

from tkinter import *

window=Tk()

window.resizable(False,False)
window.title("Registro para el Maestro")
window.geometry("600x600")

panel=Frame()
panel.pack()
panel.config(width="600",height="600")
panel.config(bg="red")

titulo=Label(text="Registro de Maestro")
titulo.pack()
titulo.place(x=190,y=50)

nombre=Label(text="Nombre")
nombre.pack()
nombre.place(x=90, y=150)

txtNombre=Entry()
txtNombre.pack()
txtNombre.place(x=182,y=100)

apellido1=Label(text="Apellido Paterno")
apellido1.pack()
apellido1.place(x=75, y=150)

txtApellido1=Entry()
txtApellido1.pack()
txtApellido1.place(x=182, y=150)

apellido2=Label(text="Apellido Materno")
apellido2.pack()
apellido2.place(x=75, y=200)

txtApellido2=Entry()
txtApellido2.pack()
txtApellido2.place(x=182, y=200)

curp=Label(text="CURP")
curp.pack()
curp.place(x=75, y=250)

txtCurp=Entry()
txtCurp.pack()
txtCurp.place(x=182, y=250)

grupo=Label(text="Grupo")
grupo.pack()
grupo.place(x=75, y=300)

txtGrupo=Entry()
txtGrupo.pack()
txtGrupo.place(x=182,y=300)

materia=Label(text="Materia")
materia.pack()
materia.place(x=75, y=350)

txtMateria=Entry()
txtMateria.pack()
txtMateria.place(x=182,y=350)

email=Label(text="Email")
email.pack()
email.place(x=75, y=400)

txtEmail=Entry()
txtEmail.pack()
txtEmail.place(x=182,y=400)


def boton1():

  from tkinter import messagebox
  nombre=txtNombre.get()
  apepa=txtApellido1.get()
  apema=txtApellido2.get()
  curp=txtCurp.get()
  grupo=txtGrupo.get()
  materia=txtMateria.get()
  email=txtEmail.get()
  
  if(nombre=="" or materia=="" or curp=="" or apema=="" or apepa=="" or grupo=="" or email==""):
    messagebox("Información","Ingresa toda la información")

  else:

    from DatosM import DatosM
    DatosM=DatosM(nombre,apepa,apema,grupo,materia,curp,email)
    DatosM.imprime()


def boton2():

  from tkinter import messagebox
  archivo=open("maestro.csv")
  registro=archivo.read()
  messagebox.showInfo("Registros",registros)
  archivo.close  


btnRegistrar=Button(command=boton1,text="Registrar")
btnRegistrar.pack()
btnRegistrar.place(x=400,y=100)

btnConsultar=Button(command=boton1,text="Consultar")
btnConsultar.pack()
btnConsultar.place(x=400,y=400)


mainloop()