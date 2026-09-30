MAX = 5
for i in range(MAX):
        total = 0
        for j in range(MAX, i, -1):
                total += j
        print(total)
