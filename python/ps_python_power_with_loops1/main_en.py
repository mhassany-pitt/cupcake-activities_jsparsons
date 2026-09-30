def power(base, exp):
        if exp == 0:
                return 1
        result = base
        temp = base
        for i in range(1, exp):
                for j in range(1, base):
                        result += temp
                temp = result
        return result
