def potencia(base, exp):
        if exp == 0:
                return 1
        resultado = base
        temp = base
        for i in range(1, exp):
                for j in range(1, base):
                        resultado += temp
                temp = resultado
        return resultado
