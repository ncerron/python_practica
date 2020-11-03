from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Participantes(Base):
    __tablename__= 'usuarios'
    id=Column(Integer, primary_key= True)
    nombre= Column(String(30), nullable=True)
    edad= Column(Integer, nullable = True)
    sexo = Column(String(1), nullable = True)
    disparo1 = Column(Float, nullable=True)
    disparo2 = Column(Float, nullable=True)
    disparo3 = Column(Float, nullable=True)
    mejor_disparo = Column(Float, nullable=True)
    prom_disparo =  Column(Float, nullable=True)


engine = create_engine('sqlite:///participantes.db')
Base.metadata.create_all(engine)
