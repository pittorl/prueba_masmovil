# -*- coding: utf8 -*-
"""
  Ejercicio 2 creacion clase persona y trabajador que hereda de esta clase persona
"""

import sys


class Persona(object):
    """Clase que representa una Persona"""

    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def presentacion(self):
        print(f"Hola! Soy {self.nombre} y tengo {self.edad} años")

class Trabajador(Persona):
    """Clase que representa a un Trabajador"""

    def __init__(self, nombre, edad,  departamento ="Data", puesto ="Analayst"):
        """Constructor de clase Trabajador"""

        # Invoca al constructor de clase Persona
        Persona.__init__(self, nombre, edad)

        # Nuevos atributos
        self.departamento = departamento
        self.puesto = puesto

    def presentacion(self):
            Persona.presentacion(self)
            print(f"Trabajo en el departamento: {self.departamento} y tengo el puesto {self.puesto}")

nombre = 'Alberto'
persona_1 = Persona(nombre, 20)
trabajador_1 = Trabajador(nombre,20,"BigData","Data Engeneering")
persona_1.presentacion()
trabajador_1.presentacion()

######################################################################################################################
# Ejercicio 2 apartado 3
#¿Qué diferencia hay entre self.nombre y la variable llamada nombre? Puedes incluirlo como comentario en el código.
#
#La diferencia es que self.nombre es el valor que tiene el contructor padre pàra esa variable
# y la variable nombre es el valor que se esta pasando a el contructor
# en este caso cuando se llama a el contructor Persona el nomber es Alberto
# y self.nombre tomara el valor Alberto ya que el objeto Persona tiene nombre y edad
#
######################################################################################################################

my_var_list = [ "Andrea", 42, "Ventas", "Manager"]
trabajador_2 = Trabajador(my_var_list[0],my_var_list[1],my_var_list[2],my_var_list[3])
trabajador_2.presentacion()

my_var_dict = { 'nombre': "Andrea", 'edad': 42, 'departamento': 'Ventas' , 'puesto': 'Manager'}
trabajador_3 = Trabajador(my_var_dict['nombre'],my_var_dict['edad'],my_var_dict['departamento'],my_var_dict['puesto'])
trabajador_3.presentacion()