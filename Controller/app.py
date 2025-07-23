#para poder limpiar la consola
from Database.mongo import ConexionMongo
from Model.hotel import agregar_habitacion, agregar_hotel, buscar_ciudad_con_habitaciones_disponibles, buscar_hoteles_con_habitaciones_disponibles, buscar_hoteles_por_ciudad, buscar_hoteles_por_comuna, buscar_hoteles_por_id, buscar_hoteles_por_nombre, buscar_hoteles_por_precio, buscar_nombre_con_habitaciones_disponibles, editar_direccion_hotel, editar_habitacion_hotel, editar_nombre_hotel, eliminar_habitacion_hotel, eliminar_hotel, obtener_hoteles
from View.funciones_mostrar import mostrar_habitaciones, mostrar_hotel, mostrar_nombre_id_direccion
from View.funciones_solicitar import solicitar_agregar_habitacion, solicitar_edicion_habitacion, solicitar_hotel, solicitar_nueva_direccion


#estructura del menu principal

def menu_principal():
    
    conexion = ConexionMongo()
    continuar = True
    opcion = 0
    
    while continuar:
        try:
            ejecutar_accion = True
            
            print("================================")
            print("   M E N Ú  P R I N C I P A L   ")
            print("================================")
            print("  1.- AGREGAR UN NUEVO HOTEL    ")
            print("  2.- BUSCAR UN HOTEL           ")
            print("  3.- EDITAR HOTELES            ")
            print("  4.- ELIMINAR HOTEL            ")
            print("  5.- SALIR                     ")
            print("================================")
            
            opcion = int(input("Seleccione una opción: "))
            
            if 1 <= opcion <= 5:
                                
                if opcion ==1:
                    print("=============================================")
                    print("     A G R E G A R  N U E V O  H O T E L     ")
                    print("=============================================")
                    
                    hotel_nuevo = solicitar_hotel()
                    id_insertado = agregar_hotel(hotel_nuevo, conexion)

                    if id_insertado:
                        print(f'\nHotel "{hotel_nuevo["nombre"]}" agregado correctamente con ID: {id_insertado}')

                        opcion_agregar_habitacion = input("\n¿Desea agregar una habitación ahora? (S/N): ").lower()
                        
                        if opcion_agregar_habitacion=="s":
                            
                            while True:
                                habitacion = solicitar_agregar_habitacion()
                                exito = agregar_habitacion(id_insertado, habitacion, conexion)
                            
                                if exito:
                                    print(f'Habitación {habitacion["numero"]} agregada correctamente.')
                                else:
                                    print(f'No se pudo agregar la habitación.')

                                otra = input("\n¿Desea agregar otra habitación? (S/N): ").lower()
                                if otra != "s":
                                    break
                        else:
                            print("\nPuede agregar habitaciones más tarde desde el menú de edición de hoteles.")
                    else:
                        print("\nNo se pudo agregar el hotel.")
 
                    
                elif opcion ==2:
                    print("=============================================")
                    print("           B U S C A R   H O T E L           ")
                    print("=============================================")
                    while True:
                        print("Seleccione alguna de las siguientes opciones de búsqueda:")
                        print("======================================")
                        print("1. Listar todos los hoteles")
                        print("2. Búsqueda por nombre")
                        print("3. Búsqueda por ID")
                        print("4. Búsqueda por ciudad")
                        print("5. Búsqueda por comuna")
                        print("6. Hoteles con habitaciones disponibles")
                        print("7. Búsqueda por nombre (solo con habitaciones disponibles)")
                        print("8. Búsqueda por ciudad (solo con habitaciones disponibles)")
                        print("9. Búsqueda de habitaciones por precio")                        
                        print("10. Volver al menú principal")
                        print("=======================================")
                        
                        opcion_busqueda = input("\nSeleccione una opción: ")

                        if opcion_busqueda == "1":
                            
                            hoteles = obtener_hoteles(conexion)
    
                            if not hoteles:
                                print("No hay hoteles registrados.")
                            else:
                                print(f"\nSe encontraron {len(hoteles)} hoteles registrados:\n")
                                for hotel in hoteles:
                                    mostrar_hotel(hotel) 
                        
                        elif opcion_busqueda == "2":
                            nombre = input("Ingrese el nombre del hotel a buscar: ")
                            resultados = buscar_hoteles_por_nombre(nombre, conexion)

                            if resultados:
                                print(f"\nResultados encontrados: {len(resultados)}")
                                for hotel in resultados:
                                    mostrar_hotel(hotel)
                            else:
                                print(f'\nNo se encontraron hoteles con el nombre: "{nombre}".')
                            
                        elif opcion_busqueda == "3":
                            id_hotel = input("Ingrese el ID del hotel a buscar: ")
                            hotel = buscar_hoteles_por_id(id_hotel, conexion)

                            if hotel:
                                print(f'\nHotel con ID: "{id_hotel}":')
                                mostrar_hotel(hotel)

                            else:
                                print(f'\nNo se encontró hotel con el ID: "{id_hotel}".')
                                
                        elif opcion_busqueda == "4":
                            ciudad = input("Ingrese la ciudad: ")
                            resultados = buscar_hoteles_por_ciudad(ciudad, conexion)
                            
                            if resultados:
                                print(f"\nResultados encontrados: {len(resultados)} hoteles en la ciudad {ciudad}")
                                for hotel in resultados:
                                    mostrar_hotel(hotel)
                                
                            
                        elif opcion_busqueda == "5":
                            comuna = input("Ingrese la comuna: ")
                            resultados = buscar_hoteles_por_comuna(comuna, conexion)
                            
                            if resultados:
                                print(f"\nResultados encontrados: {len(resultados)} hoteles en la comuna {comuna}")
                                for hotel in resultados:
                                    mostrar_hotel(hotel)
                            else:
                                print(f'\nNo se encontraron hoteles para la comuna: "{comuna}".')
                                
                                
                        elif opcion_busqueda == "6":
                            resultados = buscar_hoteles_con_habitaciones_disponibles(conexion)

                            if resultados:
                                print(f"\nHoteles con habitaciones disponibles: {len(resultados)}")
                                for hotel in resultados:
                                    mostrar_hotel(hotel)
                            else:
                                print("\nNo hay hoteles con habitaciones disponibles.")
                                
                        elif opcion_busqueda =="7":
                            nombre = input("Ingrese el nombre del hotel: ")
                            resultados = buscar_nombre_con_habitaciones_disponibles(nombre, conexion)

                            if resultados:
                                print(f"\nSe encontraron {len(resultados)} con habitaciones disponibles:")
                                for hotel in resultados:
                                    mostrar_hotel(hotel)
                            else:
                                print(f"\nNo se encontraron hoteles llamados '{nombre}' con habitaciones disponibles.")

                        elif opcion_busqueda=="8":
                            
                            ciudad = input("Ingrese la ciudad: ")
                            resultados = buscar_ciudad_con_habitaciones_disponibles(ciudad, conexion)

                            if resultados:
                                print(f"\nSe encontraron {len(resultados)} hoteles en '{ciudad}' con habitaciones disponibles:")
                                for hotel in resultados:
                                    mostrar_hotel(hotel)
                            else:
                                print(f"\nNo se encontraron hoteles en '{ciudad}' con habitaciones disponibles.")

                        elif opcion_busqueda == "9":
                            print("1. Precio menor o igual que")
                            print("2. Precio mayor o igual que")

                            subopcion = input("Seleccione una opción: ")
                            if subopcion == "1":
                                precio = int(input("Ingrese el precio límite: "))
                                condicion = "menor_igual"
                            elif subopcion == "2":
                                precio = int(input("Ingrese el precio límite: "))
                                condicion = "mayor_igual"
                            else:
                                print("Opción inválida.")
                                continue

                            resultados = buscar_hoteles_por_precio(precio, condicion, conexion)

                            if resultados:
                                for hotel in resultados:
                                    if condicion == "mayor_igual":
                                        hotel["habitaciones"] = [h for h in hotel["habitaciones"] if h["precio"] >= precio]
                                    else:
                                        hotel["habitaciones"] = [h for h in hotel["habitaciones"] if h["precio"] <= precio]

                                    mostrar_hotel(hotel)
                            else:
                                print("No se encontraron hoteles con habitaciones en ese rango de precio.")

                        elif opcion_busqueda == "10":
                            print("\nVolviendo al menú principal...")
                            ejecutar_accion = False
                            break
                        
                        else:
                            print("\nOpción no válida. Intente nuevamente.")

                           
                elif opcion ==3:
                    print("=============================================")
                    print("          E D I T A R  H O T E L E S         ")
                    print("=============================================")    
                    

                    print("\nSeleccione un hotel de la lista:")
                    
                    hoteles = obtener_hoteles(conexion)
    
                    if not hoteles:
                        print("\nNo hay hoteles registrados para editar.")
                    else:
                        mostrar_nombre_id_direccion(hoteles)

                        id_hotel = input("\nIngrese el ID del hotel que desea editar: ")
                        hotel = buscar_hoteles_por_id(id_hotel, conexion)
                        
                        if not hotel:
                            print("\nNo se encontró hotel con el ID proporcionado.")
                            continue
                        
                        while True:
                            print("\n=====================================================")
                            print(f'Usted va a modificar el hotel: "{hotel["nombre"]}"')      
                            print("======================================================")              
                            print("¿Qué desea modificar?")
                            print("\n1. Nombre del hotel")
                            print("2. Dirección del hotel")
                            print("3. Agregar habitación")
                            print("4. Editar habitaciones existentes")
                            print("5. Volver al menú principal")
                            print("======================================================")

                            opcion_edicion = input("\nSeleccione una opción: ")

                            if opcion_edicion == "1":
                                
                                nuevo_nombre = input("\nIngrese el nuevo nombre del hotel: ")
                                exito = editar_nombre_hotel(id_hotel, nuevo_nombre, conexion)
                                
                                if exito:
                                    print(f'\nNombre del hotel actualizado a: "{nuevo_nombre}"')
                                    hotel = buscar_hoteles_por_id(id_hotel, conexion) #actualizar con los cambios

                                else:
                                    print("\nNo se pudo actualizar el nombre del hotel.")

                            elif opcion_edicion == "2":
                                nueva_direccion = solicitar_nueva_direccion()
                                exito = editar_direccion_hotel(id_hotel, nueva_direccion, conexion)
                                
                                if exito:
                                    print("\nDirección actualizada correctamente.")
                                    hotel = buscar_hoteles_por_id(id_hotel, conexion) #actualizar con los cambios

                                else:
                                    print("\nNo se pudo actualizar la dirección.")
                            
                            elif opcion_edicion=="3":
                                print("\nAgregar nueva habitación al hotel:")
                                nueva_habitacion = solicitar_agregar_habitacion()  #funcion reutilizada

                                exito = agregar_habitacion(id_hotel, nueva_habitacion, conexion)
                                if exito:
                                    print("Habitación agregada correctamente.")
                                    hotel = buscar_hoteles_por_id(id_hotel, conexion) #actualizar con los cambios

                                else:
                                    print("No se pudo agregar la habitación.")

                            
                                    
                            elif opcion_edicion == "4":
                                
                                print("\nHabitaciones disponibles:")
                                mostrar_habitaciones(hotel["habitaciones"])

                                numero = input("\nIngrese el número de la habitación a editar: ")
                                
                                #comparar mediante string
                                habitacion_existe = any(str(h["numero"]) == str(numero) for h in hotel["habitaciones"])
                                
                                if not habitacion_existe:
                                    print("\nNo se encontró una habitación con ese número.")
                                    continue
                                
                                else:
                                    campo, nuevo_valor = solicitar_edicion_habitacion()
                                    if campo == "eliminar":
                                        exito = eliminar_habitacion_hotel(id_hotel, numero, conexion)
                                        if exito:
                                            print("Habitación eliminada correctamente.")
                                            hotel = buscar_hoteles_por_id(id_hotel, conexion) #actualizar con los cambios

                                        else:
                                            print("No se pudo eliminar la habitación.")
                                    elif campo:
                                        exito = editar_habitacion_hotel(id_hotel, numero, campo, nuevo_valor, conexion)
                                        if exito:
                                            print("Habitación actualizada correctamente.")
                                            hotel = buscar_hoteles_por_id(id_hotel, conexion) #actualizar con los cambios

                                        else:
                                            print("No se pudo actualizar la habitación.")

                                
                            elif opcion_edicion == "5":
                                    print("\nVolviendo al menú principal...")
                                    ejecutar_accion = False
                                    break
                            else:
                                    print("\nOpción inválida.")
                    
                        
                elif opcion ==4:
                    print("=============================================")
                    print("        E L I M I N A R  H O T E L           ")
                    print("=============================================")
                    print("\nSeleccione un hotel de la lista:")
                    
                    hoteles = obtener_hoteles(conexion)
    
                    if not hoteles:
                        print("\nNo hay hoteles registrados.")
                    else:
                        mostrar_nombre_id_direccion(hoteles)

                        id_hotel = input("\nIngrese el ID del hotel que desea ELIMINAR: ")
                        hotel = buscar_hoteles_por_id(id_hotel, conexion)
                        
                        if not hotel:
                            print("\nNo se encontró hotel con el ID proporcionado.")
                            continue                   
                    
                        print(f'\nUsted va a ELIMINAR el hotel: "{hotel["nombre"]}"')
                        eliminar = input(f'\n¿Desea eliminar el hotel "{hotel["nombre"]}"? (S/N): ').strip().lower()
                        
                        if eliminar =="s":
                            exito = eliminar_hotel(id_hotel, conexion)
                            
                            if exito:
                                print(f'\nHotel "{hotel["nombre"]}" eliminado correctamente.')
                                hotel = buscar_hoteles_por_id(id_hotel, conexion)

                            else:
                                print("No se pudo eliminar el hotel")
                        else:
                            print("\nOperación cancelada. Volviendo al menú principal....")
                            ejecutar_accion = False
                
                elif opcion == 5:
                    print("\n¡Hasta pronto!")
                    conexion.cerrar_conexion()
                    ejecutar_accion = False
                    continuar = False
                    

            else:
                print("\nOpción no válida.")
        
            # preguntar si desea continuar, de lo contrario cerrar aplicación y conexión
            if ejecutar_accion:
                while True:
                    respuesta = input("\n¿Desea realizar otra acción? (S/N): ").strip().lower()
                    
                    if respuesta in ["s", "n"]:
                        if respuesta == "n":
                            continuar = False
                            print("\n¡Hasta pronto!")
                            conexion.cerrar_conexion()
                        break  
                    
                    else:
                        print("\nEntrada no válida. Por favor, ingrese 'S' para Sí o 'N' para No.")
                
        except ValueError:
            input("\nDebe ingresar un número dentro de las opciones. Presione una tecla para continuar.")
            continue
        



