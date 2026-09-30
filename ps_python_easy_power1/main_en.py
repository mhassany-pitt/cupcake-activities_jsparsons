def power(base, exp):
        result = 1
        i = 1
        while i < exp:
                result = result * base
                i += 1
        return result
new_num = power(2, 5)
print(new_num)
