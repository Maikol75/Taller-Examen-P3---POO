class Animal: 
    def __init__(self, codigo, raza, edad):
        self.codigo = codigo
        self.edad = int(edad)
        self.raza = raza
        
    def devolver(self):
        return f"Código: {self.codigo}, Raza: {self.raza}, Edad: {self.edad} años"
