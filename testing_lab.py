def menu_principal():

    while True:
        try:

            eleccion = int(input("1) Carga de herramientas\n2) Visualizar inventario\n3) Consulta de stock\n4) Reporte de agotados\n5) Alta de nuevo producto\n6) Actualizacion de stock (compra / venta)\n7) Salir\n"))

        except ValueError:
            print("Por favor solo use numeros\n")

        else:
            return eleccion #el usuario todavia puede devolver una opcion fuera de rango
            



menu_principal()