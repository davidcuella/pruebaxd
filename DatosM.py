# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 20:00:34 2022

@author: David Betancourt
"""

class DatosM:
  def __init__(self,nombre,apepa,apema,grupo,materia,curp,email):
    
      
    self.nombre=nombre
    self.apema=apepa
    self.apema=apema
    self.materia=materia 
    self.grupo=grupo   
    self.curp=curp
    self.email=email

  def getNombre(self):
    return self.nombre

  def setNombre(self, nombre):
    self.nombre=nombre



  def getApellidopater(self):
    return self.apepa

  def setApellidopater(self,apepa):
    self.apepa=apepa



  def getApellidomater(self):
    return self.apema

  def setApellidomater(self,apema):
    self.apema=apema


  def getGrupo(self):
   return self.grupo

  def setGrupo(self,grupo):
    self.grupo=grupo
  
  def getCurp(self):
    return self.curp

  def setCurp(self,curp):
    self.curp=curp



  

  def getCorreo(self):
    return self.email

  def setCorreo(self,email):
    self.email=email

  def getMateria(self):
    return self.materia

  def setMateria(self,materia):
    self.materia=materia






  
  def imprimirdatos(self):
    archivo=open("maestregistro.csv","a")
    
    archivo.write("Nombre: ")
    archivo.write(self.nombre)
    archivo.write("\n")
    
    archivo.write("Su apellido Paterno: ")
    archivo.write(self.apepa)
    archivo.write("\n")
    
    archivo.write("Su apellido Materno: ")
    archivo.write(self.apema)
    archivo.write("\n")

    archivo.write("Grupo: ")
    archivo.write(self.grupo)
    archivo.write("\n")
    
    archivo.write("CURP: ")
    archivo.write(self.curp)
    archivo.write("\n")
    
    archivo.write("Email: ")
    archivo.write(self.email)
    archivo.write("\n")
    
    archivo.write("Materia: ")
    archivo.write(self.materia)
    archivo.write("\n")
   
    
    archivo.close()
    
    print("El nombre del maestro es: ", self.nombre)
    print("Su apellido paterno es: ", self.apepa)
    print("Su apellido materno es: ", self.apema)
    print("La materia que imparte es: ", self.materia)
    print("Su grupo es: ", self.grupo)
    print("Su CURP es: ", self.curp)
    print("Su Email es: ", self.email)