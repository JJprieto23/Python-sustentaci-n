class Estudiante:
    num_estudiantes = 0
    institucion_global = None

    def __init__(self, nombre, nota1, nota2, institucion):
        self.__nombre = nombre
        self.__nota1 = self.__validar_nota(nota1)
        self.__nota2 = self.__validar_nota(nota2)
        self.__institucion = institucion

        Estudiante.num_estudiantes += 1

        if Estudiante.institucion_global is None or Estudiante.institucion_global != institucion:
            Estudiante.institucion_global = institucion
    
    def __validar_nota(self, nota):
        if nota < 0 or nota > 5:
            raise ValueError("La nota debe estar entre 0 y 5.")
        return nota
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def nota1(self):
        return self.__nota1
    
    @nota1.setter
    def nota1(self, nueva_nota):
        self.__nota1 = self.__validar_nota(nueva_nota)
    
    @property
    def nota2(self):
        return self.__nota2
    
    @nota2.setter
    def nota2(self, nueva_nota):
        self.__nota2 = self.__validar_nota(nueva_nota)
    
    @property
    def institucion(self):
        return self.__institucion
    
    @classmethod
    def obtener_institucion_global(cls):
        return cls.institucion_global
    
    def obtener_nota_promedio(self):
        return (self.__nota1 + self.__nota2) / 2
    
    def obtener_rendimiento(self):
        promedio = self.obtener_nota_promedio()
        if promedio >= 0 and promedio < 3:
            return "Baja"
        elif promedio >= 3 and promedio < 4:
            return "Media"
        elif promedio >= 4 and promedio < 4.6:
            return "Alta"
        elif promedio >= 4.6 and promedio <= 5:
            return "Sobresaliente"
        else:
            return "Desconocido"
    
    def mostrar_informacion(self):
        rendimiento = self.obtener_rendimiento()
        return f"Nombre: {self.nombre}, Institución: {Estudiante.institucion_global}, Promedio de notas: {self.obtener_nota_promedio()}, Rendimiento: {rendimiento}"

def agregar_estudiante(num_estudiante):
    nombre = input(f"Ingrese el nombre del estudiante {num_estudiante}: ")
    institucion = input(f"Ingrese la institución del estudiante {num_estudiante}: ")
    while True:
        try:
            nota1 = float(input("Ingrese la nota 1 (de 0 a 5): "))
            nota2 = float(input("Ingrese la nota 2 (de 0 a 5): "))
            return Estudiante(nombre, nota1, nota2, institucion)
        except ValueError as e:
            print(e)  
            continue

def mostrar_escala_notas():
    tabla = (
        "+---------------+--------------+\n"
        "| Promedio      | Rendimiento  |\n"
        "|---------------|--------------|\n"
        "|  0  - 2.9     | Baja         |\n"
        "|---------------|--------------|\n"
        "|  3  - 3.9     | Media        |\n"
        "|---------------|--------------|\n"
        "|  4  - 4.5     | Alta         |\n"
        "|---------------|--------------|\n"
        "| 4.6 - 5       | Sobresaliente|\n"
        "+---------------+--------------+\n"
    )
    print(tabla)

if __name__ == "__main__":

    mostrar_escala_notas()
    
    estudiantes = []
    num_estudiante = 1
    
    while True:
        estudiante = agregar_estudiante(num_estudiante)
        estudiantes.append(estudiante)
        
        print("\nInformación de los estudiantes:")
        for idx, estudiante in enumerate(estudiantes, start=1):
            print(f"Número {idx}: {estudiante.mostrar_informacion()}")
        
        opcion = input(f"\n¿Desea agregar otro estudiante? (s/n): ")
        if opcion.lower() != 's':
            break
        
        num_estudiante += 1

    print(f"\nNúmero total de estudiantes: {Estudiante.num_estudiantes}")
