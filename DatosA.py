# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 20:00:32 2022

@author: David Betancourt
"""

class DatosA:
  def __init__(self, nombre, apepa, apema, grupo, email, boleta):
    self.nombre=nombre
    self.apepa=apepa
    self.apema=apema
    self.email=email
    self.boleta=boleta
    self.grupo=grupo

  def getNombre(self):
    return self.nombre

  def setNombre(self,nombre):
    self.nombre=nombre


  def getApellidopa(self):
    return self.apater

  def setApellidopa(self,apepa):
    self.apepa=apepa


  def getApellidoma(self):
    return self.apema

  def setApellidoma(self,apema):
    self.apema=apema
  
    
  def getGrupo(self):
      return self.grupo

  def setGrupo(self,grupo):
      self.grupo=grupo

  
  def getBoleta(self):
    return self.boleta

  def setBoleta(self,boleta):
    self.boleta=boleta

 

  def getEmail(self):
    return self.email

  def setEmail(self,email):
    self.email=email



  def imprime(self):
    archivo=open("aliregistro.csv","a")
    
    archivo.write("Nombre: ")
    archivo.write(self.nombre)
    archivo.write("\n")
    
    archivo.write("Apellido Paterno: ")
    archivo.write(self.apema)
    archivo.write("\n")
    
    archivo.write("Apellido Materno: ")
    archivo.write(self.apema)
    archivo.write("\n")
    
    archivo.write("Correo electronico: ")
    archivo.write(self.email)
    archivo.write("\n")
    
    archivo.write("Grupo: ")
    archivo.write(self.grupo)
    archivo.write("\n")
    
    archivo.write("Boleta: ")
    archivo.write(self.boleta)
    archivo.write("\n")
    
    
    
    
    
    
    
    
    archivo.close()
    
    print("El nombre del alumno es: ",self.nombre)
    print("Su apellido paterno es: ", self.apepa)
    print("Su apellido materno es: ", self.apema)
    print("Su email es: ", self.email)
    print("Su grupo es: ", self.grupo)
    print("Su boleta es: ", self.amater)
    
