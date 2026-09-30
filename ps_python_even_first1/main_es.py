lista_numeros = [7, 2, 4, 1, 3, 5, 6, 8]
i = 0
j = len(lista_numeros) - 1
while i < j:
        while i <= j and lista_numeros[i] % 2 == 0:
                i += 1
        while i <= j and lista_numeros[j] % 2 != 0:
                j -= 1
        if i < j:
                temp = lista_numeros[i]
                lista_numeros[i] = lista_numeros[j]
                lista_numeros[j] = temp
print(lista_numeros)
