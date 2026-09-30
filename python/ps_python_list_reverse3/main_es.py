def lista_invertida(lista):
        nueva_lista = [0] * len(lista)
        i = 0
        j = len(lista) - 1
        while i < len(lista):
                j = j - 1
                nueva_lista[j] = lista[i]
                i += 1
        return nueva_lista
lista1 = [1, 2, 3, 4, 5]
lista2 = lista_invertida(lista1)
print(lista2)
