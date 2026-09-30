MAXIMO = 5
i = 0
while i < MAXIMO:
        suma = 0
        j = MAXIMO
        while j > i:
                suma = suma + j
                j = j - 1
        print(suma)
        i = i + 1
