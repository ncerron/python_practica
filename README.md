# python_practica


Aplicación en donde se registra los datos de un competencia de tiro con arco y flecha,  realizada en Python.
Se muestran las distintas consultas como el mejer disparo, cantidad de participantes, etc. en la terminal 
usando Pandas, y guardándolas en archivos csv.

Se implementa un método para guardar toda la información del torneo en una base de datos utilizando sqlite
y SQLAlchemy, y un método para mostrar los datos de la base de datos en la terminal.

Se puede realizar una consulta del premio obtenido a través de la url:
flask/api/v2/<nombre_del_ganador>/<mejor _disparo>
