lista1 = [1, 2, 3, 4, 5]
nueva_lista = []
i = 0
while i < len(lista1):
        elemento = lista1[i]
        nueva_lista.insert(0, elemento)
        i += 1
print(nueva_lista)
