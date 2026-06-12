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

        except ValueError:
            print("Por favor solo use numeros\n")

        else:
            return eleccion #el usuario todavia puede devolver una opcion fuera de rango
            











#CARGA DE HERRAMIENTAS










#VISUALIZAR INVENTARIO









#CONSTULTA DE STOCK 














#REPORTE DE AGOTADOS











#ALTA DE NUEVO PRODUCTO











#ACTUALIZACION DE STOCK (COMPRA/VENTA)












#SALIR








#Programa

carga_inicial()
menu_principal()

