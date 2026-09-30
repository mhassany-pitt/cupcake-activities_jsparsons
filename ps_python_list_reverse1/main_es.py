def lista_invertida(lista):
        nueva_lista = []
        i = 0
        while i < len(lista):
                elemento = lista[i]
                nueva_lista.insert(0, elemento)
                i += 1
        return nueva_lista
lista1 = [1, 2, 3, 4, 5]
lista2 = lista_invertida(lista1)
print(lista2)
