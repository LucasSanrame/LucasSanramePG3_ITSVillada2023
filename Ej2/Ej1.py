class Garry:
    
    def inicializar(self,nom):
        self.nombre=nom

    def imprimir(self):
        print("Nombre",self.nombre)

Clara=Garry()
Garrys=Garry()

Clara.inicializar("Clara")
Clara.imprimir()

Garrys.inicializar("Mod")
Garrys.imprimir()