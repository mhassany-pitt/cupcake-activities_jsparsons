base = 2
exp = 5
if(exp == 0):
        print(1)
else:
        resultado = base
        temp = base
        for i in range(1, exp):
                for j in range (1, base):
                        resultado += temp
                temp = resultado
        print(resultado)
