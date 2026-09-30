lista = [8, 3, 2, 5, 7, 5, 6]
resultado = []
impares = []
for n in lista:
        if n % 2 == 0:
                resultado.append(n)
        else:
                impares.append(n)
for i in range(len(impares)):
        resultado.append(impares[i])
print(resultado)
