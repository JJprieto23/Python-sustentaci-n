def calcular_perimetro_cuadrado(lado):
    return 4 * lado

def calcular_perimetro_rectangulo(lado1, lado2):
    return 2 * (lado1 + lado2)

def calcular_perimetro_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3

def calcular_perimetro_rombo(lado):
    return 4 * lado

def main():
    lado_cuadrado = float(input("Ingrese el lado del cuadrado: "))
    
    lado1_rectangulo = float(input("Ingrese el primer lado del rectángulo: "))
    lado2_rectangulo = float(input("Ingrese el segundo lado del rectángulo: "))
    
    lado1_triangulo = float(input("Ingrese el primer lado del triángulo: "))
    lado2_triangulo = float(input("Ingrese el segundo lado del triángulo: "))
    lado3_triangulo = float(input("Ingrese el tercer lado del triángulo: "))
    
    lado_rombo = float(input("Ingrese el lado del rombo: "))
    
    perimetro_cuadrado = calcular_perimetro_cuadrado(lado_cuadrado)
    perimetro_rectangulo = calcular_perimetro_rectangulo(lado1_rectangulo, lado2_rectangulo)
    perimetro_triangulo = calcular_perimetro_triangulo(lado1_triangulo, lado2_triangulo, lado3_triangulo)
    perimetro_rombo = calcular_perimetro_rombo(lado_rombo)
    
    print("--EL PERÍMETRO DE LAS FIGURAS SON--")
    print(f"Perímetro del cuadrado: {perimetro_cuadrado}")
    print(f"Perímetro del rectángulo: {perimetro_rectangulo}")
    print(f"Perímetro del triángulo: {perimetro_triangulo}")
    print(f"Perímetro del rombo: {perimetro_rombo}")

if __name__ == "__main__":
    main()
