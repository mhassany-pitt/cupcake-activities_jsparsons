lista1 = [1, 2, 3, 4, 5]
        nueva_lista = []
        for i in lista1:
                numero = i
                if numero % 2 == 0:
                        nueva_lista.append(numero * numero)
        print(nueva_lista)
