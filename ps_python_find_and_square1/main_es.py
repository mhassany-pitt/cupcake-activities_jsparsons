def encontrar_y_elevar_al_cuadrado(lista):
        nueva_lista = []
        i = 0
        while i < len(lista):
                numero = lista[i]
                if numero % 2 == 0:
                        nueva_lista.append(numero * numero)
                i += 1
        return nueva_lista
