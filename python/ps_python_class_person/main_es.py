class Person:
    def __init__(self, nombre, profesion):
        self.__nombre = nombre
    def saludar(self):
        return self.__nombre + ". Encantado de conocerte!"
safiira = Person("Safiira", "biologa")
print(safiira.saludar())
