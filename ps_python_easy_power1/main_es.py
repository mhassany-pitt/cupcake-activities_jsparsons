def potencia(base, exp):
        resultado = 1
        i = 1
        while i < exp:
                resultado = resultado * base
                i += 1
        return resultado
nuevo_num = potencia(2, 5)
print(nuevo_num)
