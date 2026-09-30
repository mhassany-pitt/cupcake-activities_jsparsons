def pares_primero(lista_num):
        resultado = []
        impares = []
        for n in lista_num:
                if n % 2 == 0:
                        resultado.append(n)
                else:
                        impares.append(n)
        for i in range(len(impares)):
                resultado.append(impares[i])
        return resultado
