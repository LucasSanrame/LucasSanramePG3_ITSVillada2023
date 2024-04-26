class Operaciones:
    def __init__(self, n1, n2):
        self.numero1 = n1
        self.numero2 = n2

    def sumar(self):
        self.resutlado_suma= self.numero1 + self.numero2
        print("suma: ", self.resutlado_suma)
    
    def restar(self):
        self.resutlado_resta= self.numero1 - self.numero2
        print("resta: ", self.resutlado_resta)
    
    def dividir(self):
        self.resutlado_division= self.numero1 / self.numero2
        print("division: ", self.resutlado_division)
    
    def multiplicacion(self):
        self.resutlado_mult= self.numero1 * self.numero2
        print("multiplicacion: ", self.resutlado_mult)
    
operacion = Operaciones()

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

operacion.dividir()
operacion.sumar()
operacion.restar()
operacion.multiplicacion()