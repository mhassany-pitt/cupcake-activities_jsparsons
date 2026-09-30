def lista_invertida(lista):
        nueva_lista = [0] * len(lista)
        j = len(lista) - 1
        for i in range(len(lista)):
                j = j - 1
                nueva_lista[j] = lista[i]
        return nueva_lista
lista1 = [1, 2, 3, 4, 5]
lista2 = lista_invertida(lista1)
print(lista2)
