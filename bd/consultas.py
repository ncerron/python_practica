from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
import pandas as pd

import sys
sys.path.insert(1, 'bd/')

from bd_setup import Base, Participantes

engine = create_engine('sqlite:///participantes.db')
Base.metadata.bind = engine
Session = scoped_session(sessionmaker(bind=engine))
session = Session()


def borrar_bd():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def mostrar_bd():
   
    with open('archivos/archivo.csv', "w") as escribo:
        escribo.write(
            "Nro Participante, Nombre , Edad, Sexo, Disp 1, Disp 2, Disp 3, Mejor Disp, Promedio de Disp\n")

        for i in session.query(Participantes).all():
            line =",".join(
                [
                    str(i.id),    
                    i.nombre,    
                    str(i.edad),  
                    i.sexo,
                    str(i.disparo1),
                    str(i.disparo2),
                    str(i.disparo3),
                    str(i.mejor_disparo),
                    str(i.prom_disparo)
                ]
            )
            escribo.write(line + '\n')

    print("\n")
    print(37*' ' + "Registros en Base de Datos")
    print("\n")
    registros = pd.read_csv('archivos/archivo.csv', index_col=0)
    print(registros)
    print("\n")


def guardar_en_base(nombre, edad, sexo, disp1, disp2,disp3, mejor,prom):
    part=Participantes(
            nombre=nombre,
            edad=edad,
            sexo= sexo,
            disparo1=disp1,
            disparo2 = disp2,
            disparo3 = disp3,
            mejor_disparo = mejor,
            prom_disparo = prom
        )
        
    session.add(part)
    session.commit()

