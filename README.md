# PRUEBA MASSMOVIL

###Primera Parte: GitHub

1)	Tienes que crear una cuenta de GitHub si no la tienes. Es gratuito, así que no debería de haber problema
2)	Crea un repositorio nuevo. Tiene que ser público para que lo podamos revisar (nos tendrás que pasar el enlace al repo).
3)	A partir de ahora deberás hacer los ejercicios a continuación. Cada apartado numerado debería de ser un único commit 
      (el mensaje que pongas en cada uno es libre, pero como sugerencia puedes poner el nombre del ejercicio y el número del apartado), 
      pero puedes hacer tantos commits como necesites.

###Segunda parte: Python

1)	Define un nuevo objeto Trabajador, que herede de la clase Persona, añadiendo las propiedades departamento y puesto. La clase persona contiene:

    class Persona:

    def init (self, nombre, edad):
        self.nombre = nombre 
        self.edad = edad
    def presentation(self):
        print(f"Hola! Soy {self.nombre} y tengo {self.edad} años")

    nombre = 'Alberto'
    persona_1 = Persona(nombre, 20) 
    person.presentation()

2)	Cambia el método de presentation en la clase de Trabajador, manteniendo la función original pero añadiendo un nuevo print con los campos de departamento y puesto. Crea una instancia trabajador_1 (pon los valores que quieras) y llama a su función presentation.
3)	¿Qué diferencia hay entre self.nombre y la variable llamada nombre? Puedes incluirlo como comentario en el código.
4)	Haz que por defecto el departamento sea Data y el puesto sea Analyst.
5)	Dada la lista my_var_list = [ ‘Andrea’, ‘42’, ‘Ventas’, ‘Manager’], pasa sus valores (puedes reordenar la lista si lo necesitas) a una nueva instancia de Trabajador llamada trabajador_2 y llama a su función presentation.
6)	Dado el diccionario my_var_dict = { ‘nombre’: ‘Andrea’, ‘edad’: ‘42’, ‘departamento’: ‘Ventas’ , ‘puesto’: ‘Manager’}, pasa sus valores a una nueva instancia de Trabajador llamada trabajador_3 y llama a su función presentation.


###Tercera Parte: Airflow

Para esta prueba vas a necesitar tener el módulo Airflow instalado en local o en una máquina de docker para poder lanzarlo.
1)	Define un DAG llamado test que se ejecuta cada día a las 3:00 UTC, con los siguientes argumentos por defecto:
        
    from datetime import datetime, timedelta

    default_args = {
        'owner': 'airflow', 
        'depends_on_past': False, 
        'start_date': datetime(1900, 1, 1),
        'retries': 1,
        'retry_delay': timedelta(seconds=5)
    }

2)	Incluye las tareas start y end como DummyOperator y que end vaya detrás de start en el DAG.
3)	Define una lista de tareas dummy task_n con N tareas, donde cada tarea con n par dependa de todas las tareas impares.
4)	Define un nuevo operador TimeDiff que parta del BaseOperator, que reciba una fecha (diff_date) como entrada y muestre la diferencia con la actual. Crea una tarea nueva con el operador.
5)	¿Qué es un Hook? ¿En qué se diferencia de una conexión? Puedes responder en un comentario dentro del código.