from animal import Animal

class BaseDatos:
    def __init__(self):
        self.animales = []
        self.produccionHuevos = {}

    def agregarPollo(self, animal):
        self.animales.append(animal)
        self.produccionHuevos[animal.getCodigo()] = []
        print("Pollo agregado correctamene")

    def mostrarPollo(self):
        if not self.animales:
            print("No hay pollos registraos")
        else:
            for a in self.animales:
                print(a)

    def registrarHuevos(self, codigo):
        if codigo in self.produccionHuevos:
            print("\nIngrese la cantidad de huevos por dia: ")
            total_semana = 0
            dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
            for dia in dias:
                while True:
                    try:
                        cant = int(input(f"{dia}: "))
                        if cant < 0:
                            print("no puede ser negativo")
                            continue
                        total_semana += cant
                        break
                    except ValueError:
                        print("ingrese un numero valido")
            self.produccionHuevos[codigo].append(total_semana)
            print(f"Produccion semanal registrada ({total_semana} huevos)")
        else:
            print("Pollo no encontrado")

    def mostrarProduccion(self, codigo):
        if codigo in self.produccionHuevos:
            totalHuevos = sum(self.produccionHuevos[codigo])
            print(f"El pollo {codigo} puso {totalHuevos} huevos en el mes")
        else:
            print("El codigo del pollo es invalido")

    def actualizarPollo(self, codigo):
        for animal in self.animales:
            if animal.getCodigo() == codigo:
                nueva_raza = input("Nueva raza (deje en blanco para no cambiar): ")
                nueva_edad = input("Nueva edad (deje en blanco para no cambiar): ")
                if nueva_raza:
                    animal.setRaza(nueva_raza)
                if nueva_edad:
                    animal.setEdad(nueva_edad)
                print("Datos actualizados correctamene")
                return
        print("No se encontro un pollo con ese codigo")

    def eliminarPollo(self, codigo):
        for animal in self.animales:
            if animal.getCodigo() == codigo:
                self.animales.remove(animal)
                if codigo in self.produccionHuevos:
                    del self.produccionHuevos[codigo]
                print(f"Pollo con codigo {codigo} eliminado")
                return
        print("No se encontro un pollo con ese codigo")