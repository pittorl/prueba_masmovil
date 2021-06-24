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

nombre = 'Alberto'
persona_1 = Persona(nombre, 20)
persona_1.presentation()