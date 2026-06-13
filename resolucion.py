#este es el segundo parcial de programacion de la UTN 


# Contexto del Problema:

# Una ferretería local necesita digitalizar el control de sus productos para evitar pérdidas de stock.
# Actualmente manejan sus datos de forma manual y requieren un programa que permita gestionar 
# las herramientas a la venta y sus unidades disponibles en tiempo real.


#MENU
def menu_principal():

    while True:
        try:

            eleccion = int(input("1) Carga de herramientas\n2) Visualizar inventario\n3) Consulta de stock\n4) Reporte de agotados\n5) Alta de nuevo producto\n6) Actualizacion de stock (compra / venta)\n7) Salir\n"))

            if eleccion not in range(1,8):
                raise IndexError

        except ValueError:
            print("Por favor solo use numeros\n")
        except IndexError:
            print("\nOpcion fuera de rango\n")

        else:
            return eleccion 


#CARGA INICIAL
def carga_inicial(inventario):

    if inventario == []:

        while True:
            try:
                cantidad = int(input("\nCuantas herramientas quiere cargar?\n"))

                if cantidad < 0:
                    raise ValueError("negativo")

            except ValueError as e:
                if str(e) == "negativo":
                    print("\nError, use numeros positivos\n")
                else:
                    print("\nError, solo use numeros por favor\n")

            
            else:
                #Carga de herramientas una vez tenemos la cantidad validada
                for i in range(cantidad):

                    while True:
                        try:
                            nombre_herramienta = input("\nHerramienta: ")

                            if nombre_herramienta.strip() == "":
                                raise ValueError("nombre vacio")

                            for item in inventario:
                                if item["herramienta"] == nombre_herramienta:
                                    raise ValueError("duplicado")

                            herramienta_stock_inicial = int(input("Cantidad: "))

                        
                        except ValueError as e:

                            if str(e) == "duplicado":
                                print("\nError, herramienta ya cargada\n")

                            elif str(e) == "nombre vacio":
                                print("\nNo se permiten nombres vacios\n")

                            else:
                                print("\nCantidad invalida, use numeros\n")
                        
                        else:

                            inventario.append({"herramienta": nombre_herramienta, "cantidad": herramienta_stock_inicial})
                            break #para salir de while que mantiene al usuario cargando cantidades
                return inventario #para salir del while de carga de herramientas y emepzar con el programa
    else:
        print("\nNo se puede volver a usar la carga inicial, para cargar nuevas herramientas use la opcion 5\n")





#VISUALIZAR INVENTARIO

def ver_inventario(inventario):
    
    if inventario != []:
        for item in inventario:
            print(f"{item["herramienta"]} : {item["cantidad"]}\n")
    else:
        print("\nNo se han cargado herramientas, use la opcion de carga inicial\n")





#CONSTULTA DE STOCK 

def consulta(inventario):
    
    while True:
        try:
            buscar_herramienta = input("\nBuscar: ")
            if not any(item["herramienta"] == buscar_herramienta for item in inventario):
                raise ValueError("no se encuentra")

        except ValueError as e:
            if str(e) == "no se encuentra":
                print(f"\nNo se encuentra la herramienta \"{buscar_herramienta}\"\n")
                break

            else:
                print("\nerror de entrada\n")
        else:
            for item in inventario:
                if item["herramienta"] == buscar_herramienta:
                    print(f"\n{buscar_herramienta} : {item["cantidad"]} en stock\n")
            break
                




#REPORTE DE AGOTADOS

def reporte_de_agotados(inventario):
    agotados = False
    for item in inventario:
        if item["cantidad"] == 0:
            print(f"\n{item["herramienta"]}\n")
            agotados = True
    if agotados == False:
        print("\nNo hay herramientas sin stock\n")




#ALTA DE NUEVO PRODUCTO

def nuevo_producto(inventario):
    try:
        nuevo_producto = input("Nueva herramienta: ")

        if nuevo_producto == "":
            raise ValueError("nombre vacio")

        for item in inventario:
            if item["herramienta"] == nuevo_producto:
                raise ValueError("duplicado")

        
        cantidad = int(input("Cantidad: "))
        if cantidad < 0:
            raise ValueError("negativo")

    except ValueError as e:
        if str(e) == "duplicado":
            print("\nError, herramienta ya en stock\n")

        elif str(e) == "nombre vacio":
            print("\nError, no se permiten nombres vacios\n")
        
        elif str(e) == "negativo":
            print("\nError, no se puede poner numeros negativos como stock\n")
            
        else:
            print("\nError, cantidad ingresada invalida, use numeros.\n")
    else:

        inventario.append({"herramienta": nuevo_producto, "cantidad": cantidad})
        




#ACTUALIZACION DE STOCK (COMPRA/VENTA)

def compra_venta(inventario):
    while True:
        try:
            eleccion = int(input("1) Venta\n2) Compra\n"))
            if eleccion not in (1, 2):

                raise IndexError

            
        except ValueError:
            print("\nError, use los numeros 1 o 2\n")

        except IndexError:
            print("\nOpcion fuera de rango\n")
        
        else:
            if eleccion == 1:
                print(inventario)

                try:
                    herramienta_vendida = input("herramienta vendida: ")
                    encontrado = False
                    for item in inventario:
                            if item["herramienta"] != herramienta_vendida:
                                encontrado =False
                            else:
                                cantidad_en_stock = item["cantidad"]
                                encontrado = True
                                break
                    if encontrado == False:
                        raise ValueError("herramienta no encontrada")
                    
                    cantidad_vendida = int(input("Cantidad vendida: "))

                    if cantidad_vendida < 0:
                        raise ValueError("valor negativo")

                    if cantidad_vendida > cantidad_en_stock:
                        raise ValueError("stock insuficiente")

                except ValueError as e:
                    if str(e) == "herramienta no encontrada":
                        print("\nError. No se encontró esa herramienta\n")

                    elif str(e) == "stock insuficiente":
                        print("\nNo hay suficiente stock\n")

                    elif str(e) == "valor negativo":
                        print("\nError, no se puede usar un valor negativo")

                    else:
                        print("error desconocido")
                else:
                    for item in inventario:
                        if item["herramienta"] == herramienta_vendida:
                            item["cantidad"] -= cantidad_vendida
                    break
            else:
                print(inventario)

                try:
                    herramienta_comprada = input("Herramienta comprada: ")
                    encontrado = False
                    for item in inventario:
                        if item["herramienta"] != herramienta_comprada:
                            encontrado = False
                        else:
                            encontrado = True
                            break

                            
                    if encontrado == False:
                        raise ValueError("herramienta no encontrada")
                    
                    cantidad_comprada = int(input("Cantidad: "))
                    if cantidad_comprada < 0:
                        raise ValueError("valor negativo")
                        

                except ValueError as e:
                    
                    if str(e) == "herramienta no encontrada":
                        print("\nError. herramienta no registrada en stock, cargala en \"Alta de nuevo producto\"\n")

                    elif str(e) == "valor negativo":
                        print("\nError, no se puede usar un valor negativo\n")

                    else:
                        print("\nError desconocido\n")
                else:
                    for item in inventario:
                        if item["herramienta"] == herramienta_comprada:
                            item["cantidad"] += cantidad_comprada
                    break




def programa():

    inventario = [

    ]

    while True:

        eleccion = menu_principal()

        if eleccion == 7:
            break

        elif eleccion == 1:
            carga_inicial(inventario)
        
        elif eleccion == 2:
            ver_inventario(inventario)
        
        elif eleccion == 3:
            consulta(inventario)

        elif eleccion == 4:
            reporte_de_agotados(inventario)
        
        elif eleccion == 5:
            nuevo_producto(inventario)

        elif eleccion == 6:
            compra_venta(inventario)


programa()

