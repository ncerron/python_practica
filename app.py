from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from bd.consultas import session
from bd.bd_setup import Participantes
from sqlalchemy import asc
import datetime

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///participantes.db'
db=SQLAlchemy(app)

@app.route('/flask/api/v2/<nombre_del_ganador>/<mejor_disparo>', methods=['GET'])
def premios(nombre_del_ganador, mejor_disparo):
     
     ##falta token
    dia = datetime.datetime.now()
    bd= session.query(Participantes).order_by(asc(Participantes.mejor_disparo)).limit(3)

    if bd[0].nombre.strip() == nombre_del_ganador and bd[0].mejor_disparo== float(mejor_disparo):
        res = mensaje(dia,bd[0].nombre.strip() , "1000", "Primer Premio", "dsdfsdfsf" )
    elif bd[1].nombre.strip() == nombre_del_ganador and bd[1].mejor_disparo== float(mejor_disparo):
        res = mensaje(dia,bd[1].nombre.strip() , "600", "Segundo Premio", "dsdfsdfsf" )
    elif bd[2].nombre.strip() == nombre_del_ganador and bd[2].mejor_disparo== float(mejor_disparo):
        res = mensaje(dia,bd[1].nombre.strip() , "400", "Tercer Premio", "dsdfsdfsf" )
    else:
        res={'mensaje': 'no tiene premio'} 
    return res


def mensaje(fecha, nombre, premio, premio_cat,token):
    return {'fecha': fecha, 'mensaje': f'Hola {nombre}, obtuviste el {premio_cat}!! ganaste $ {premio}', 'nombre': nombre , 'premio': premio, 'token':token}


if __name__== '__main__':
    app.run(debug=True)
