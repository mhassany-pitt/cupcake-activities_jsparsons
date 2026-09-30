num = 50
lista1 = []
lista2 = []
lista3 = []
for i in range(1, num + 1):
        if i % 2 == 0 and i % 5 == 0:
                lista1.append(i)
        elif i % 2 == 0:
                lista2.append(i)
        elif i % 5 == 0:
                lista3.append(i)
print("divisible solo por 2:")
print(lista2)
print("divisible solo por 5:")
print(lista3)
print("divisible por 2 y 5:")
print(lista1)
