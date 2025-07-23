def mostrar_hotel(hotel):
    print(f"\n{hotel['nombre']} - (ID: {hotel['_id']})")
    d = hotel['direccion']
    print(f"{d['calle']} {d['numero']}, {d['comuna']}, {d['ciudad']} ({d['region']})")
    print("Habitaciones:")
    for h in hotel['habitaciones']:
        estado = "Sí" if h['disponible'] else "No"
        precio = f"{h['precio']:,}".replace(",", ".")
        print(f"         - Nº {h['numero']} | Tipo: {h['tipo']} | Precio: ${precio} | Disponible: {estado}")


def mostrar_nombre_id_direccion(hoteles):
    for hotel in hoteles:
        print(f"\n{hotel['nombre']} - (ID: {hotel['_id']})")
        d = hotel['direccion']
        print(f"{d['calle']} {d['numero']}, {d['comuna']}, {d['ciudad']} ({d['region']})")

def mostrar_habitaciones(habitaciones):
    for h in habitaciones:
        estado = "Sí" if h["disponible"] else "No"
        precio = f"{h['precio']:,}".replace(",", ".")
        print(f" - Nº {h['numero']} | Tipo: {h['tipo']} | Precio: ${precio} | Disponible: {estado}")