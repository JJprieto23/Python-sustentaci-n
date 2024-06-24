def agregar_una_vez(lista, el):
    try:
        if el in lista:
            raise ValueError(f"Error: Imposible añadir elementos duplicados => {el}.")
        else:
            lista.append(el)
    except ValueError as e:
        print(e)

def main():

    entrada = input("Ingrese los elementos de la lista separados por espacios: ")

    lista = entrada.split()

    print(f"Lista inicial: {lista}")

    elementos_a_agregar = input("Ingrese los elementos que desea añadir a la lista separados por espacios: ")

    nuevos_elementos = elementos_a_agregar.split()

    for el in nuevos_elementos:
        agregar_una_vez(lista, el)

    print(f"Lista después de intentar agregar los elementos: {lista}")

    print("Gracias por usar este programa")

if __name__ == "__main__":
    main()
