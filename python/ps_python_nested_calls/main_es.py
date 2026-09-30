def calcular(primero, segundo):
    return segundo * 3 + primero
def doble(valor):
    return valor * 2
print(doble(doble(5)))
print(calcular(doble(3), 2 + calcular(5, 1)))
