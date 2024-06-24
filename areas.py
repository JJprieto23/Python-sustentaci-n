def area_cuadrado(lado):
    '''Calcula el área de un cuadrado.'''
    return lado * lado

def area_rectangulo(base, altura):
    '''Calcula el área de un rectángulo.'''
    return base * altura

def area_triangulo(base, altura):
    '''Calcula el área de un triángulo.'''
    return (base * altura) / 2

def area_rombo(diagonal_menor, diagonal_mayor):
    '''Calcula el área de un rombo.'''
    return (diagonal_menor * diagonal_mayor) / 2

if __name__ == "__main__":
    print("Cálculo de áreas de diferentes figuras geométricas")

    lado_cuadrado = float(input("Ingrese el lado del cuadrado: "))
    base_rectangulo = float(input("Ingrese la base del rectángulo: "))
    altura_rectangulo = float(input("Ingrese la altura del rectángulo: "))
    base_triangulo = float(input("Ingrese la base del triángulo: "))
    altura_triangulo = float(input("Ingrese la altura del triángulo: "))
    diagonal_menor_rombo = float(input("Ingrese la diagonal menor del rombo: "))
    diagonal_mayor_rombo = float(input("Ingrese la diagonal mayor del rombo: "))

    print("\nÁrea del cuadrado:", area_cuadrado(lado_cuadrado))
    print("Área del rectángulo:", area_rectangulo(base_rectangulo, altura_rectangulo))
    print("Área del triángulo:", area_triangulo(base_triangulo, altura_triangulo))
    print("Área del rombo:", area_rombo(diagonal_menor_rombo, diagonal_mayor_rombo))
