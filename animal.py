class Animal: 
    def __init__(self, codigo, raza, edad):
        self.__codigo = codigo
        self.__raza = raza
        self.__edad = int(edad)

    def getCodigo(self):
        return self.__codigo

    def getRaza(self):
        return self.__raza

    def getEdad(self):
        return self.__edad

    def setCodigo(self, nuevo_codigo):
        self.__codigo = nuevo_codigo

    def setRaza(self, nueva_raza):
        self.__raza = nueva_raza

    def setEdad(self, nueva_edad):
        try:
            nueva_edad = int(nueva_edad)
            if nueva_edad >= 0:
                self.__edad = nueva_edad
            else:
                print("la edad no puede ser negativa")
        except ValueError:
            print("la edad debe ser un numero entero")

    def __str__(self):
        return f"Codigo: {self.__codigo}, Raza: {self.__raza}, Edad: {self.__edad} años"