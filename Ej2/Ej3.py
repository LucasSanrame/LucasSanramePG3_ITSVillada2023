class triangulo:
    def inicializar(self,l1,l2,l3):
        self.lado1=l1
        self.lado2=l2
        self.lado3=l3

    def imprimir(self):
        if self.l1 > self.l2:
            if self.l1 > self.l3:
                print("El lado 1 es el mas grande")
            else:
                print("El lado 3 es el mas grande")
        else:
            if self.l2 > self.l3:
                print("El lado 2 es el mas grande")
    
    def equilatero(self):
        if self.l1 == self.l2 == self.l3:
            print("Es equilatero")
        else:
            print("No es equilatero")

Triangulo = triangulo()
lad1= 23
lad2= 4
lad3= 67
Triangulo.inicializar(lad1, lad2, lad3)
Triangulo.imprimir()
Triangulo.equilatero()