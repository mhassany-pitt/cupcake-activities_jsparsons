base = 2
exp = 5
if exp == 0 and base == 0 or exp < 0:
        print("Error!")
else:
        resultado = 1
        i = 1
        while i <= exp:
                resultado = resultado * base
                i += 1
        print(resultado)
