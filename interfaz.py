from baseDatos import BaseDatos
from animal import Animal

class Interfaz:
    def __init__(self):
        self.bd = BaseDatos()

    def menu(self):
        while True:
            print("\nMenu")
            print("1. Agregar pollos")
            print("2. Mostrar pollos")
            print("3. Registrar produccion de huevos")
            print("4. Ver produccion de huevos")
            print("5. Eliminar pollo")
            print("6. Actualizar pollo")
            print("7. Salir")
            opcion = input("elije una opcion: ")

            if opcion == '1':
                codigo = input("Ingrese el codigo del pollo: ")
                raza = input("Ingrese la raza del pollo: ")
                edad = input("Ingrese la edad del pollo (años): ")
                pollo = Animal(codigo, raza, edad)
                self.bd.agregarPollo(pollo)

            elif opcion == '2':
                self.bd.mostrarPollo()
            elif opcion == '3':
                codigo = input("Ingrese el codigo del pollo: ")
                self.bd.registrarHuevos(codigo)
            elif opcion == '4':
                codigo = input("Ingrese el codigo del pollo: ")
                self.bd.mostrarProduccion(codigo)
            elif opcion == '5':
                codigo = input("Ingrese el codigo del pollo que vas a eliminar: ")
                self.bd.eliminarPollo(codigo)
            elif opcion == '6':
                codigo = input("Ingrese el código del pollo a actualizar: ")
                self.bd.actualizarPollo(codigo)    
            elif opcion == '7':
                print("Saliendo del programa")
                break
            else:
                print("Opcion invalida intente de nuevo")

if __name__ == "__main__":
    app = Interfaz()
    app.menu()