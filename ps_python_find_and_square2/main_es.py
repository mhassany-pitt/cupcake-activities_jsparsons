lista1 = [1, 2, 3, 4, 5]
nueva_lista = []
i = 0
while i < len(lista1):
        numero = lista1[i]
        if numero % 2 == 0:
                nueva_lista.append(numero * numero)
        i += 1
print(nueva_lista)
