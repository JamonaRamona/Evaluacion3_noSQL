def solicitar_hotel():

    nombre = input("Nombre del hotel: ")
    print("=============================================")
    print("      A g r e g a r  D i r e c c i ó n       ")
    print("=============================================")
    print("\nSe solicitará Calle, Número, Comuna, Ciudad y Región por separado")
    print("Ingrese los datos según se solicite\n")
    calle = input("Calle: ")
    numero = input("Número: ")
    comuna = input("Comuna: ")
    ciudad = input("Ciudad: ")
    region = input("Región: ")

    direccion = {
        "calle": calle,
        "numero": numero,
        "comuna": comuna,
        "ciudad": ciudad,
        "region": region
    }

    return {
        "nombre": nombre,
        "direccion": direccion,
        "habitaciones": []  # inicialmente vacío
    }

def solicitar_agregar_habitacion():

    while True:
        print("=============================================")
        print("     A g r e g a r  H a b i t a c i ó n      ")
        print("=============================================")
        print("\nSe solicitará Número, Tipo, Precio y Disponibilidad por separado\n")

        numero = input("Número de habitación: ")
        tipo = input("Tipo de habitación: ")
        while True: #bucle para manejar que el precio sea un número entero
            try:
                precio = int(input("Precio: "))
                break
            except ValueError:
                input("El precio debe ser un número entero. Presione una tecla para intentarlo nuevamente.")
        
        disponible = input("¿Está disponible? (s/n): ").lower() == "s"

        return {
            "numero": numero,
            "tipo": tipo,
            "precio": precio,
            "disponible": disponible
        }

def solicitar_nueva_direccion():
    print("\nSe solicitará Calle, Número, Comuna, Ciudad y Región por separado")
    print("Ingrese los datos según se solicite\n")
    calle = input("Calle: ")
    numero = input("Número: ")
    comuna = input("Comuna: ")
    ciudad = input("Ciudad: ")
    region = input("Región: ")

    return {
        "calle": calle,
        "numero": numero,
        "comuna": comuna,
        "ciudad": ciudad,
        "region": region
    }


def solicitar_edicion_habitacion():
    print("\n¿Qué desea editar de la habitación?")
    print("1. Tipo")
    print("2. Precio")
    print("3. Disponibilidad")
    print("4. Eliminar habitación")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        campo = "tipo"
        nuevo_valor = input("Nuevo tipo: ")
    elif opcion == "2":
        campo = "precio"
        nuevo_valor = int(input("Nuevo precio: "))
    elif opcion == "3":
        campo = "disponible"
        respuesta = input("¿Está disponible? (s/n): ").lower()
        nuevo_valor = True if respuesta == "s" else False
    elif opcion == "4":
        return "eliminar", None
    else:
        print("Opción inválida.")
        return None, None

    return campo, nuevo_valor


