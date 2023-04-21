# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 20:00:36 2022

@author: David Betancourt
"""

from tkinter import *

window=Tk()
window.title("Menu de la Escuela")
window.geometry("800x800")



panel=Frame()
panel.config(width="650", heigh="650")
panel.config(bg="white")
panel.pack()




titulo=Label(text="Registro de la Escuela")
titulo.pack()
titulo.place(x=182,y=50)

def boton1():
  window.destroy()
  try:
    from VMaestro import VAlumno
    alumno.alumno()
  except:
    print("Error")



def boton2():
  window.destroy()
 
  try:
    
    from VAlumno import VMaestro
    maestro.maestro()
  except:
    print("Error en la consulta")


opcion1=Button(command=boton1,text="RegistroAlumno")
opcion1.pack()


opcion1.place(x=160,y=150)

opcion2=Button(command=boton2,text="RegistroMaestro")
opcion2.pack()


opcion2.place(x=330,y=150)


mainloop()