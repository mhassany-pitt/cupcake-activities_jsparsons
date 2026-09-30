lista1 = [1, 2, 3, 4, 5]
nueva_lista = [0] * len(lista1)
i = 0
j = len(lista1) - 1
while i < len(lista1):
        j = j - 1
        nueva_lista[j] = lista1[i]
        i += 1
print(nueva_lista)
