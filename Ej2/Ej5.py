class Persona:
    def __init__(self, nom="", ed=0):
        self.nombre = nom
        self.edad = ed
    
    def cargar_datos(self):
        self.nombre = input("Ingrese el nombre de la persona: ")
        self.edad = int(input("Ingrese la edad de la persona: "))
    
    def imprimir(self):
        print("Nombre:", self.nombre, "Edad:", self.edad)

class Empleado(Persona):
    def __init__(self, nom="", ed=0, su=0):
        super().__init__(nom, ed)
        self.sueldo = su
    
    def cargar_datos(self):
        super().cargar_datos()
        self.sueldo = float(input("Ingrese el sueldo del empleado: "))
    
    def impuestos(self):
        if self.sueldo > 3000:
            print("Se deberán pagar impuestos")
        else:
            print("No se deben pagar impuestos")
    
    def imprimir(self):
        super().imprimir()
        print("Salario:", self.sueldo)

if __name__ == "__main__":
    persona = Persona()
    persona.cargar_datos()
    persona.imprimir()

    empleado = Empleado()
    empleado.cargar_datos()
    empleado.impuestos()
    empleado.imprimir()