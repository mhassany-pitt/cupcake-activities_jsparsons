def potencia(base, exp):
        temp = 1.0
        while exp > 0:
                if exp % 2 == 0:
                        base = base * base
                        exp = exp // 2
                else:
                        temp = base * temp
                        exp = exp - 1
        resultado = temp
        return resultado
