def lista_de_residuos(lista1, lista2):
        nueva_lista = []
        if len(lista1) == len(lista2):
                for i in range(len(lista1)):
                        if lista2[i] == 0:
                                nueva_lista.append(2)
                        else:
                                resultado = lista1[i] % lista2[i]
                                nueva_lista.append(resultado)
        return nueva_lista
lista1 = [19, 3, 4, 2]
lista2 = [4, 2, 1, 0]
print(lista_de_residuos(lista1, lista2))
