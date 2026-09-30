CANTIDAD = 3
lista1 = []
for i in range(CANTIDAD):
        lista2 = [0] * CANTIDAD
        for j in range(CANTIDAD):
                lista2[j] = i * CANTIDAD + j
        lista1.append(lista2)
lista1[2][2] = 99
print(lista1)
