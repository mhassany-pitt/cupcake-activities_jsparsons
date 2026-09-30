lst = [8, 3, 2, 5, 7, 5, 6]
result = []
odds = []
for n in lst:
        if n % 2 == 0:
                result.append(n)
        else:
                odds.append(n)
for i in range(len(odds)):
        result.append(odds[i])
print(result)
