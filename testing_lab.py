
def devolverNumero():
    intentos = 1
    while True:
        try:
            numero = int(input())
        
        except ValueError:
            print("eso no es un numero\n")

        else:
            return numero
        
        finally:
            print(f"intento n°{intentos}")
            intentos += 1

devolverNumero()