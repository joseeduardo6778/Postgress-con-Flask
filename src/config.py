from psycopg2 import connect

HOST = 'localhost'
PORT = '5432'
BD = 'bd_personas'
USUARIO = 'postgres'
PASSWORD = 'jeduar'

def EstablecerConexion():
    try:
        conexion = connect(host=HOST, port=PORT, dbname=BD, user=USUARIO, password= PASSWORD)
    except ConnectionError:
        print("Error de conexion")
    return conexion