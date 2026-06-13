#este es el segundo parcial de programacion de la UTN 


# Contexto del Problema:

# Una ferretería local necesita digitalizar el control de sus productos para evitar pérdidas de stock.
# Actualmente manejan sus datos de forma manual y requieren un programa que permita gestionar 
# las herramientas a la venta y sus unidades disponibles en tiempo real.



#Inventario donde se van a guardar las herramientas
inventario = {

}


#Funcion inicial para que el usuario carge herramientas y cantidades antes de empezar el programa
def carga_inicial():

    while True:
        try:
            cantidad = int(input("\nCuantas herramientas quiere cargar?\n"))

        except ValueError:
            print("\nError, solo use numeros por favor\n")
        
        else:
            #Carga de herramientas una vez tenemos la cantidad validada
            for i in range(cantidad):

                while True:
                    try:
                        nombre_herramienta = input("Herramienta: ")

                        if nombre_herramienta in inventario:
                            raise ValueError("duplicado")

                        herramienta_stock_inicial = int(input("Cantidad: "))

                    
                    except ValueError as e:

                        if str(e) == "duplicado":
                            print("\nError, herramienta ya cargada\n")
                        else:
                            print("\nCantidad invalida, use numeros\n")
                    
                    else:

                        inventario[nombre_herramienta] = herramienta_stock_inicial
                        break #para salir de while que mantiene al usuario cargando cantidades
        break #para salir del while de carga de herramientas y emepzar con el programa







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

            











#CARGA DE HERRAMIENTAS


#creo que puedo usar carga_inicial()








#VISUALIZAR INVENTARIO

def ver_inventario():

    for herramienta, cantidad in inventario.items():
        print(f"{herramienta} : {cantidad}")







#CONSTULTA DE STOCK 

def consulta():
    
    while True:
        try:
            buscar_herramienta = input("\nBuscar: ")
            if not (buscar_herramienta in inventario):
                raise ValueError("no se encuentra")

        except ValueError as e:
            if str(e) == "no se encuentra":
                print(f"\nNo se encuentra la herramienta {buscar_herramienta}\n")
                break

            else:
                print("\nerror de entrada\n")
        else:
            print(f"{buscar_herramienta} : {inventario[buscar_herramienta]}")
                












#REPORTE DE AGOTADOS

def reporte_de_agotados():
    agotados = False
    for herramienta, cantidad in inventario.items():
        if cantidad == 0:
            print(f"{herramienta}")
            agotados = True
    if agotados == False:
        print("\nNo hay herramientas sin stock\n")










#ALTA DE NUEVO PRODUCTO

def nuevo_producto():
    try:
        nuevo_producto = input("Nueva herramienta: ")

        if nuevo_producto in inventario:
            raise ValueError("duplicado")
        
        cantidad = int(input("Cantidad: "))

    except ValueError as e:
        if str(e) == "duplicado":
            print("\nError, herramienta ya en stock\n")
        else:
            print("\nError\n")
    else:

        inventario[nuevo_producto] = cantidad
        











#ACTUALIZACION DE STOCK (COMPRA/VENTA)

def compra_venta():
    while True:
        try:
            eleccion = int(input("1) Venta\n2) Compra"))
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

                    if herramienta_vendida not in inventario:
                        raise ValueError("herramienta no encontrada")
                    
                    cantidad_vendida = int(input("Cantidad vendida: "))

                    if cantidad_vendida > inventario[herramienta_vendida]:
                        raise ValueError("stock insuficiente")

                except ValueError as e:
                    if e == "herramienta no encontrada":
                        print("\nError. No se encontró esa herramienta\n")
                    elif e == "stock insuficiente":
                        print("\nNo hay suficiente stock\n")
                    else:
                        print("error desconocido")
                else:
                    inventario[herramienta_vendida] -= cantidad_vendida
                    break
            else:
                print(inventario)

                try:
                    herramienta_comprada = input("Herramienta comprada: ")

                    if herramienta_comprada not in inventario:
                        raise ValueError("herramienta no encontrada")
                    
                    cantidad_comprada = int(input("Cantidad: "))
                        

                except ValueError as e:
                    
                    if e == "herramienta no encontrada":
                        print("\nError. herramienta no registrada en stock, cargala en \"Alta de nuevo producto\"\n")

                    else:
                        print("\nError desconocido\n")
                else:
                    inventario[herramienta_comprada] += cantidad_comprada
                    break

                    











#SALIR










def programa():


    while True:

        eleccion = menu_principal()

        if eleccion == 7:
            break
        
        elif eleccion == 2:
            ver_inventario()
        
        elif eleccion == 3:
            consulta()

        elif eleccion == 4:
            reporte_de_agotados()
        
        elif eleccion == 5:
            nuevo_producto()

        elif eleccion == 6:
            compra_venta()


carga_inicial()
programa()

