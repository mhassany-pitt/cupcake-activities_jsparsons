lista1 = [1, 2, 3, 4, 5]
nueva_lista = []
for i in range(len(lista1)):
        numero = lista1[i]
        if numero % 2 == 0:
                nueva_lista.append(numero * numero)
print(nueva_lista)
