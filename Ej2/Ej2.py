class Alumno:
    def inicializar(self,nom, n):
        self.nombre=nom
        self.nota=n

    def imprimir(self):
        print("Nombre",self.nombre,"Nota:", self.nota)

    def regular(self):
        if self.nota >= 4:
            print("aprobado") 
        else:
            print("desaprobado")

Olmos = Alumno()
Pozo = Alumno()

Olmos.inicializar("olmos", 3)
Olmos.imprimir()
Olmos.regular()

Pozo.inicializar("pozo", 6)
Pozo.imprimir()
Pozo.regular()