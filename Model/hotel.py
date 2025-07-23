from Database.mongo import ConexionMongo
from bson import ObjectId

#FUNCIONES FIND

def obtener_hoteles(conexion):
    coleccion = conexion.obtener_coleccion()
    hoteles = list(coleccion.find())
    return hoteles


def buscar_hoteles_por_id(id_hotel, conexion):
    try:
        coleccion = conexion.obtener_coleccion()
        hotel = coleccion.find_one({"_id": ObjectId(id_hotel)})
        return hotel
    except Exception as e:
        print(f"Error al obtener el hotel: {e}")
        return None

def buscar_hoteles_por_nombre(nombre, conexion):
    coleccion = conexion.obtener_coleccion()
    
    resultados = list(coleccion.find({"nombre": {"$regex": nombre, "$options": "i"}}))
    return resultados


def buscar_hoteles_por_comuna(comuna, conexion):
    coleccion = conexion.obtener_coleccion()

    resultados = list(coleccion.find(
        {"direccion.comuna": {"$regex": comuna, "$options": "i"}}
    ))
    return resultados

def buscar_hoteles_por_ciudad(ciudad, conexion):
    coleccion = conexion.obtener_coleccion()

    resultados = list(coleccion.find(
        {"direccion.ciudad": {"$regex": ciudad, "$options": "i"}}
    ))
    return resultados


def buscar_hoteles_con_habitaciones_disponibles(conexion):
    coleccion = conexion.obtener_coleccion()

    resultados = list(coleccion.find({
        "habitaciones": {
            "$elemMatch": {"disponible": True}
        }
    }))
    return resultados

def buscar_nombre_con_habitaciones_disponibles(nombre,conexion):
    coleccion = conexion.obtener_coleccion()
    resultados = list(coleccion.find({
        "nombre": {"$regex": nombre, "$options": "i"},
        "habitaciones": {
            "$elemMatch": {"disponible": True}
        }
    }))
    return resultados

def buscar_ciudad_con_habitaciones_disponibles(ciudad, conexion):
    coleccion = conexion.obtener_coleccion()
    resultados = list(coleccion.find({
        "direccion.ciudad": {"$regex": ciudad, "$options": "i"},
        "habitaciones": {
            "$elemMatch": {"disponible": True}
        }
    }))
    return resultados


#FUNCIONES DE CREATE (INSERT ONE)

def agregar_hotel(hotel_nuevo, conexion):
    coleccion = conexion.obtener_coleccion()
    try:
        resultado = coleccion.insert_one(hotel_nuevo)
        return resultado.inserted_id  # ID del nuevo hotel insertado
    except Exception as e:
        print(f"Error al insertar el hotel: {e}")
        return None


#FUNCIONES DE UPDATE

def agregar_habitacion(id_hotel, nueva_habitacion, conexion):
    try:
        coleccion = conexion.obtener_coleccion()

        resultado = coleccion.update_one(
            {"_id": ObjectId(id_hotel)},
            {"$push": {"habitaciones": nueva_habitacion}}
        )

        return resultado.modified_count > 0
    except Exception as e:
        print(f"Error al agregar habitación: {e}")
        return False


def editar_nombre_hotel(id_hotel, nuevo_nombre, conexion):
    coleccion = conexion.obtener_coleccion()
    
    resultado = coleccion.update_one(
        {"_id": ObjectId(id_hotel)},
        {"$set": {"nombre": nuevo_nombre}}
    )
    return resultado.modified_count > 0


def editar_direccion_hotel(id_hotel, nueva_direccion, conexion):
    try:
        coleccion = conexion.obtener_coleccion()
        
        resultado = coleccion.update_one(
            {"_id": ObjectId(id_hotel)},
            {"$set": {"direccion": nueva_direccion}}
        )
        return resultado.modified_count > 0
    except Exception as e:
        print(f"Error al actualizar la dirección: {e}")
        return False


def editar_habitacion_hotel(id_hotel, numero_habitacion, campo, nuevo_valor, conexion):
    try:
        coleccion = conexion.obtener_coleccion()

        resultado = coleccion.update_one(
            {
                "_id": ObjectId(id_hotel),
                "habitaciones.numero": numero_habitacion
            },
            {
                "$set": {f"habitaciones.$.{campo}": nuevo_valor}
            }
        )

        return resultado.modified_count > 0

    except Exception as e:
        print(f"Error al actualizar habitación: {e}")
        return False


#FUNCIONES PARA ELIMINAR

def eliminar_habitacion_hotel(id_hotel, numero_habitacion, conexion):
    try:
        coleccion = conexion.obtener_coleccion()

        resultado = coleccion.update_one(
            {"_id": ObjectId(id_hotel)},
            {"$pull": {"habitaciones": {"numero": numero_habitacion}}}
        )

        return resultado.modified_count > 0
    except Exception as e:
        print(f"Error al eliminar habitación: {e}")
        return False


def eliminar_hotel(id_hotel, conexion):
    try:
        coleccion = conexion.obtener_coleccion()
        resultado = coleccion.delete_one({"_id": ObjectId(id_hotel)})

        return resultado.deleted_count > 0
    except Exception as e:
        print(f"Error al eliminar el hotel: {e}")
        return False