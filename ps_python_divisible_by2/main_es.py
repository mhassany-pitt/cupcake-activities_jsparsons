num = 100
for i in range(1, num + 1):
        if i % 2 == 0 and i % 5 == 0:
                print(i, "es divisible por 2 y 5")
        elif i % 5 == 0:
                print(i, "es divisible solo por 5")
        elif i % 2 == 0:
                print(i, "es divisible solo por 2")
        else:
                print(i, "no es divisible por 2 ni 5")
