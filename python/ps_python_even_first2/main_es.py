def pares_primero(lista_num):
        i = 0
        j = len(lista_num) - 1
        while i < j:
                while i < j and lista_num[i] % 2 == 0:
                        i += 1
                while i < j and lista_num[j] % 2 != 0:
                        j -= 1
                if i < j:
                        temp = lista_num[i]
                        lista_num[i] = lista_num[j]
                        lista_num[j] = temp
        return lista_num
