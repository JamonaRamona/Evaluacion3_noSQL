#pip install pymongo

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ConfigurationError, PyMongoError

class ConexionMongo:
    def __init__(self):
        self.cliente = None
        self.db = None
        self.conectar()

    def conectar(self):
        try:
            self.cliente = MongoClient("mongodb+srv://usuario:contraseña@clase01.zloxnzq.mongodb.net/")
            self.db = self.cliente["Prueba3"]  # nombre de la base de datos, así se llama en la mía xd
            #test conexión:
            self.cliente.admin.command('ping')
            print("Conexión a MongoDB exitosa.")
        except (ConnectionFailure, ConfigurationError, PyMongoError) as e:
            print(f"Error al conectar con MongoDB: {e}")

    def obtener_coleccion(self):
        if self.cliente is None or self.db is None:
            print("Reintentando conexión a MongoDB...")
            self.conectar()
        return self.db["hoteles"]  # nombre de la colección, así se llama la mía xd

    def cerrar_conexion(self):
        if self.cliente:
            self.cliente.close()
            print("Conexión a MongoDB cerrada.")
