class Animal: 
    def init(self, codigo, raza, edad):
        self.codigo = codigo
        self.edad = edad
        self.raza = raza

    def devolver(self):
        return f"Código: {self.codigo}, Raza: {self.raza}, Edad: {self.edad} años"
