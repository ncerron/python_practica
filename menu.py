from clases import Disparo, Concurso
import math
import sys
import csv
from bd.consultas import guardar_en_base, borrar_bd, mostrar_bd


class Menu():
    def __init__(self):
        self.c = Concurso()
        self.opciones = {
            "1": self.ingresar_participante,
            "2": self.mostrar_participantes,
            "3": self.mostrar_podio,
            "4": self.mostrar_ultimo,
            "5": self.cantidad_paticipantes,
            "6": self.mostar_participantes_por_edad,
            "7": self.mostrar_promedio_disparos,
            "8": self.guardar_participantes,
            "9": self.guardar_bd,
            "10": self.ver_bd,
            "11": self.salir
        }

    def mostrar_menu(self):
        print( '\033[36m' +  """
    Menu

     1 Ingresar participantes
     2 Listado de participantes
     3 Listado de podio de ganadores
     4 Ver ultimo participante
     5 Ver cantidad de participantes
     6 Listado de participantes por edad
     7 Listado de promedio de disparos
     8 Guardar informacion del torneo
     9 Guardar en Base de Datos
    10 Ver registros de la Base de Datos 
    11 Salir
    """ + '\033[m')

    def run(self):
        '''Muestra el menú y responde a las elecciones.'''
        while True:
            self.mostrar_menu()
            eleccion = input("Escribe una opción: ")
            accion = self.opciones.get(eleccion)
            if accion:
                accion()
            else:
                print("{0} no es una elección válida".format(eleccion))

    def salir(self):
        print("Adios")
        sys.exit(0)

    def ingresar_participante(self):
        self.ingresar_part()

    def mostrar_participantes(self):
        self.uso_funcion(self.c.mostrar("none"))

    def mostrar_podio(self):
        self.uso_funcion(self.c.podio("none"))

    def mostrar_ultimo(self):
        self.uso_funcion(self.c.ultimo("none"))

    def cantidad_paticipantes(self):
        self.uso_funcion(self.c.cantidaParticipantes("none"))

    def mostar_participantes_por_edad(self):
        self.uso_funcion(self.c.listadoPorEdad("none"))

    def mostrar_promedio_disparos(self):
        self.uso_funcion(self.c.promedioDeDisparos("none"))

    def guardar_participantes(self):
        self.c.guardarEnArchivo("none")

    def guardar_bd(self):
        self.c.guardarEnArchivo("none")
        borrar_bd()

        with open('archivos/consulta.csv', newline='') as File:
            reader = csv.DictReader(File)
            for row in reader:
                guardar_en_base(row[' Nombre '], row[' Edad'], row[' Sexo'], row[' Disp 1'], row[' Disp 2'],row[' Disp 3'],row[' Mejor Disp'],row[' Promedio de Disp'])


    def ver_bd(self):
        self.uso_funcion(mostrar_bd())
        
    # fin menu     
    def uso_funcion(self, funcion):
        salida = 0
        while salida != 99:
            funcion
            salida = self.validacion_input(
                "Ingrese 99 para volver al menu: ", "int")      

    def calculo_tiros(self, x, y):
        return math.sqrt(x**2+y**2)

    def validacion_input(self, texto, tipo):
        while True:
            texto_ingresado = input(texto)
            try:
                if tipo == "float":
                    if -80 <= float(texto_ingresado) <= 80:
                        return float(texto_ingresado)
                    else:
                        raise ValueError("el numero debe ser menor a 80")
                elif tipo == "int":
                    return int(texto_ingresado)
                elif tipo == "string":
                    if not texto_ingresado:
                        raise ErrorNombre("Ingrese un Nombre")
                    else:
                        return texto_ingresado
                elif tipo == "char":
                    texto_char = texto_ingresado[0]
                    if texto_char.lower() == "f" or texto_char.lower() == "m":
                        return texto_char.lower()
                    else:
                        raise ErrorSexo("Ingrese f o m ")

            except ErrorNombre as error:
                print(error)
            except ErrorSexo as error:
                print(error)
            except ValueError:
                print('verifique los datos ingresados')

    def ingresar_part(self):
        ingreso = 0
        ListaParticipantes = Concurso()
        while ingreso != 99:

            nombre = self.validacion_input(
                "Ingrese Nombre del Participante \n", "string")
            edad = self.validacion_input(
                "Ingrese Edad del Participante \n", "int")
            sexo = self.validacion_input(
                "Ingrese Sexo de Participante, ingrese f o m \n", "char")

            for i in range(3):
                x = self.validacion_input(
                    "Ingrese Coordenada 'x' del disparo {} \n".format(i+1), "float")
                y = self.validacion_input(
                    "Ingrese Coordenada 'y' del disparo  {} \n".format(i+1), "float")

                globals()["coord" + str(i+1)] = self.calculo_tiros(x, y)

            coord1 = round(globals()["coord1"], 2)
            coord2 = round(globals()["coord2"], 2)
            coord3 = round(globals()["coord3"], 2)

            lista_coord = [coord1, coord2, coord3]
            mejor_disparo = min(lista_coord)
            promedio_disparo = round((sum(lista_coord)/3), 2)

            participante = Disparo(nombre, edad, sexo, coord1,
                                   coord2, coord3, mejor_disparo, promedio_disparo)
            ListaParticipantes.agregar(participante)

            ingreso = self.validacion_input(
                "Ingrese un numero para ingresar un nuevo Participantes,\nsino para salir ingrese 99: ", "int")


class ErrorNombre (Exception):
    """Se crea la excepcion MiError"""
    pass


class ErrorSexo (Exception):
    """Se crea la excepcion MiError"""
    pass
