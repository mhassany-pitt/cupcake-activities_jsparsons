def encontrar_y_elevar_al_cuadrado(lista):
        nueva_lista = []
        for i in lista:
                numero = i
                if numero % 2 == 0:
                        nueva_lista.append(numero * numero)
        return nueva_lista
