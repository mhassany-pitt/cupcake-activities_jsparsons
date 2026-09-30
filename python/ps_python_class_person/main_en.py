class Person:
    def __init__(self, firstname, profession):
        self.__name = firstname
    def greet(self):
        return self.__name + ". Nice to meet you!"
safira = Person("Safiira", "biologist")
print(safira.greet())
