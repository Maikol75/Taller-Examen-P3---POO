from animal import Animal

class BaseDatos:
    def __init__(self):
        self.animales = []
        self.produccionHuevos = {}

    def agregarPollo(self, animal):
        self.animales.append(animal)
        self.produccionHuevos[animal.codigo]=[]
        print("Pollo agregado")

    def mostrarPollo(self):
        if not self.animales:
            print("No hay pollos registraos")
        else:
            for a in self.animales:
                print(a)
    
    def registrarHuevos(self, codigo):
        if codigo in self.produccionHuevos:
            print("\nIngrese la cantidad de huevos por dia: ")
            total_semana= 0
            dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
            for dia in dias:
                while True:
                    try:
                        cant = int(input(f"{dia}: "))
                        if cant < 0:
                            print("No puede ser negativo")
                            continue
                        total_semana += cant
                        break
                    except ValueError:
                        print("Ingrese un numero")
                self.produccionHuevos[codigo].append(total_semana)
                print(f"La produccion semanal fue registrada ({total_semana} huevos)")
        else:
                print("Pollo no encontrado")

    def mostrarProduccion(self, codigo):
        if codigo in self.produccionHuevos:
            totalHuevos= sum(self.produccionHuevos[codigo])
            print(f"El pollo {codigo} puso {totalHuevos} huevos en el mes")
        else:
            print("El codigo del pollo es invalido")

    def actualizarPollo(self, codigo):
        for animal in self.animales:
            if animal.codigo == codigo:
                nueva_raza = input("Nueva raza (deje en blanco para no cambiar): ")
                nueva_edad = input("Nueva edad (deje en blanco para no cambiar): ")
                if nueva_raza:
                    animal.raza = nueva_raza
                if nueva_edad:
                    animal.edad = nueva_edad
                print("Datos actualizados correctamente")
                return
        print("No se encontro un pollo con ese codigo")

    def eliminarPollo(self, codigo):
        for animal in self.animales:
            if animal.codigo == codigo:
                self.animales.remove(animal)
                if codigo in self.produccionHuevos:
                    del self.produccionHuevos[codigo]
                print(f"el pollo con codigo {codigo} fue eliminado")
                return

        print("No se encontr a un pollo con este codigo")
