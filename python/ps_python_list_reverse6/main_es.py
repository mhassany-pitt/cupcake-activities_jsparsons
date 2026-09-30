lista1 = [1, 2, 3, 4, 5]
nueva_lista = [0] * len(lista1)
j = len(lista1)
for i in range(len(lista1)):
        j = j - 1
        nueva_lista[j] = lista1[i]
        print(nueva_lista)
