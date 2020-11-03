from clases import Participante, Concurso, Disparo
import csv


participante1 = Disparo("juan perez", 11, "m", 5, 6, 4, 4, 5)
# print(participante1)

participante2 = Disparo("pepe", 31, "f", 4, 4, 5, 4, 4.33)
# print(participante2)

participante3 = Disparo("coco", 9, "f", 6, 6, 5, 5, 5)
# print(participante2)

participante4 = Disparo("kelina", 21, "f", 4.5, 4, 5, 4, 4.5)
# print(participante2)


c = Concurso()
c.agregar(participante1)
c.agregar(participante2)
c.agregar(participante3)
c.agregar(participante4)

# c.ultimo("consulta")
c.mostrar("guardar")
#
#
# c.podio("none")
# c.guardarEnArchivo("guardar")
# c.listadoPorEdad("guardar")

# c.promedioDeDisparos()
# c.cantidaParticipantes("guardar")

""" 
with open('archivos/consulta.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        print(row[0])
 """
for x in c.concursantes:

    print(x)