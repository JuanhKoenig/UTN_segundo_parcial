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

        except ValueError:
            print("Por favor solo use numeros")

        else:
            return eleccion #el usuario todavia puede devolver una opcion fuera de rango
            break
        










#CARGA DE HERRAMIENTAS










#VISUALIZAR INVENTARIO









#CONSTULTA DE STOCK 














#REPORTE DE AGOTADOS











#ALTA DE NUEVO PRODUCTO











#ACTUALIZACION DE STOCK (COMPRA/VENTA)












#SALIR