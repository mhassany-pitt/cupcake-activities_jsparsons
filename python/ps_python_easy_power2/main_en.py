base = 2
exp = 5
if exp == 0 and base == 0 or exp < 0:
        print("Error!")
else:
        result = 1
        i = 1
        while i <= exp:
                result = result * base
                i += 1
        print(result)
