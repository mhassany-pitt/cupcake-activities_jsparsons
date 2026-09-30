def eliminar_duplicados(lista_de_num):
        nueva_lista = []
        for elemento in lista_de_num:
                if elemento not in nueva_lista:
                        nueva_lista.append(elemento)
        return nueva_lista
