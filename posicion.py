lista = [3, 5, 6, 8]

while True:
    try:
        pos = int(input("Ingrese la posición del elemento que desea obtener: "))
        print(f"El valor en la posición {pos} es {lista[pos]}")
        break

    except ValueError:
        print("Error: La posición ingresada no es un número entero válido.")
    
    except IndexError:
        print(f"Error: La posición {pos} no existe en la lista.")

print("Programa finalizado correctamente.")
