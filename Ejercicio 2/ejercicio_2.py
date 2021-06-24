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
    def presentation(self):
        print(f"Hola! Soy {self.nombre} y tengo {self.edad} años")

class Trabajador(Persona):
    """Clase que representa a un Supervisor"""

    def __init__(self, nombre, edad, departamento, puesto):
        """Constructor de clase Supervisor"""

        # Invoca al constructor de clase Persona
        Persona.__init__(self, nombre, edad)

        # Nuevos atributos
        self.departamento = departamento
        self.puesto = puesto

    def presentation(self):
            Persona.presentation(self)
            print(f"Trabajo en el departamento: {self.departamento} y tengo el puesto {self.puesto}")

nombre = 'Alberto'
persona_1 = Persona(nombre, 20)
trabajador_1 = Trabajador(nombre,20,"BigData","Data Engeneering")
persona_1.presentation()
trabajador_1.presentation()