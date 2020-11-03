import csv
import copy
import pandas as pd


class Participante():
    contador_id = 1

    def __init__(self, nomYape, edad, sexo):
        self.idParticipante = Participante.contador_id
        self.nomYape = nomYape
        self.edad = edad
        self.sexo = sexo
        Participante.contador_id += 1

    def __str__(self):
        return "\n Nro unico del Participante: {} \n, Nombre y Apellido: {}, Edad: {}, Sexo: {}\n".format(self.idParticipante, self.nomYape, self.edad, self.sexo)


class Disparo(Participante):
    def __init__(self, nomYape, edad, sexo, disparo1, disparo2, disparo3, mejor_disparo, prom_disparo):
        Participante.__init__(self,  nomYape, edad, sexo)
        self.disparo1 = disparo1
        self.disparo2 = disparo2
        self.disparo3 = disparo3
        self.mejor_disparo = mejor_disparo
        self.prom_disparo = prom_disparo

    def __str__(self):
        return "{}, {}, {}, {}, {}, {}, {}, {}, {}".format(self.idParticipante, self.nomYape, self.edad, self.sexo, self.disparo1, self.disparo2, self.disparo3, self.mejor_disparo, self.prom_disparo)


class Concurso():
    concursantes = []

    def __init__(self, concursantes=[]):
        self.concursantes = concursantes

    def agregar(self, c):
        self.concursantes.append(c)

    # visualiza todos lor registros ordenados segun Mejor Disparo
    def mostrar(self, accion):
        self.concursantes.sort(
            key=lambda participante: participante.idParticipante)
        self.guardarEnArchivo("consulta")

        try:
            if accion == "guardar":
                registros = pd.read_csv('archivos/consulta.csv', index_col=0)
                registros.to_csv('archivos/mostar.csv')
            else:
                print("\n")
                print(37*' ' + "Listado de participantes")
                print("\n")
                registros = pd.read_csv('archivos/consulta.csv', index_col=0)
                print(registros)
                print("\n")
        except FileNotFoundError:
            print("No se puede procesar el archivo")

    # los 3 primeros concursantes con tiros mas cercano, si hay dos iguales desempatar por promedio
    def podio(self, accion):
        self.concursantes.sort(
            key=lambda participante: (participante.mejor_disparo, participante.prom_disparo))
        self.guardarEnArchivo("consulta")  # guardo consulta.csv
        try:
            if accion == "guardar":
                registros = pd.read_csv('archivos/consulta.csv', index_col=0)
                 ##Para devolver las primeras n filas, use DataFrame.head([n])
                registros.head(3).to_csv(
                    'archivos/podio.csv')
            else:
                print("\n")
                print(40*' ' + "Podio de Ganadores")
                print("\n")
                # leo el archivo y lo represento en consola
                registros = pd.read_csv('archivos/consulta.csv', index_col=0)
                print(registros.head(3))
                print("\n")
        except FileNotFoundError:
            print("No se puede procesar el archivo")

    # mostrar quien fue el último.
    def ultimo(self, accion):
        self.concursantes.sort(
            key=lambda participante: participante.mejor_disparo, reverse=True)
        self.guardarEnArchivo("consulta")

        try:
            if accion == "guardar":
                registros = pd.read_csv('archivos/consulta.csv', index_col=0)
                ##Para devolver las primeras n filas, use DataFrame.head([n])
                registros.head(1).to_csv('archivos/ultimo.csv')
            else:
                print("\n")
                print(43*' ' + "Ultimo lugar")
                print("\n")
                registros = pd.read_csv('archivos/consulta.csv', index_col=0)
                print(registros.head(1))
                print("\n")
        except FileNotFoundError:
            print("No se puede procesar el archivo")

    # informar cuantos participantes formaron parte del concurso.
    def cantidaParticipantes(self, accion):
        if accion == "guardar":
            with open('archivos/cantidadParticipantes.csv', "w") as escribo:
                escribo.write("Cantidad de participantes: \n")
                escribo.write(str(len(self.concursantes)))
        else:
            print("\n")
            print("Cantidad de Participantes:", len(self.concursantes))
            print("\n")

     # listado de los participantes ordenados por edad.
    def listadoPorEdad(self, accion):
        self.concursantes.sort(
            key=lambda participante: participante.edad)
        self.guardarEnArchivo("consulta")

        try:
            if accion == "guardar":
                registros = pd.read_csv('archivos/consulta.csv', index_col=0)
                registros.to_csv('archivos/listadoPorEdad.csv')
            else:
                print("\n")
                print(32*' ' + "Listado por edad del participante")
                print("\n")
                registros = pd.read_csv('archivos/consulta.csv', index_col=0)
                print(registros)
                print("\n")
        except FileNotFoundError:
            print("No se puede procesar el archivo")

     # promedio de todos los disparos.
    def promedioDeDisparos(self, accion):
        self.concursantes.sort(
            key=lambda participante: participante.prom_disparo)
        self.guardarEnArchivo("consulta")

        try:
            if accion == "guardar":
                registros = pd.read_csv('archivos/consulta.csv', index_col=0,
                                        usecols=[0, 1, 8])
                registros.to_csv('archivos/promedios.csv')
            else:
                print("\n")
                print(5*' ' + "Listado por promedio de participantes")
                print("\n")
                registros = pd.read_csv('archivos/consulta.csv', index_col=0,
                                        usecols=[0, 1, 8])
                print(registros)
                print("\n")
        except FileNotFoundError:
            print("No se puede procesar el archivo")

 # guardar toda la información del torneo en un archivo csv.
    def guardarEnArchivo(self, tipo):
        if tipo == "consulta":
            with open('archivos/consulta.csv', "w") as escribo:
                escribo.write(
                    "Nro Participante, Nombre , Edad, Sexo, Disp 1, Disp 2, Disp 3, Mejor Disp, Promedio de Disp\n")
                for row in self.concursantes:
                    escribo.write(str(row) + "\n")
        else:
            print("guardando las consultas....")
            self.mostrar("guardar")
            self.cantidaParticipantes("guardar")
            self.podio("guardar")
            self.ultimo("guardar")
            self.listadoPorEdad("guardar")
            self.promedioDeDisparos("guardar")
