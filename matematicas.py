def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

if __name__ == "__main__":

    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))

    print(f"La suma de {a} y {b} es: {suma(a, b)}")
    print(f"La resta de {a} y {b} es: {resta(a, b)}")
    print(f"La multiplicación de {a} y {b} es: {multiplicacion(a, b)}")
    print(f"La división de {a} y {b} es: {division(a, b)}")
