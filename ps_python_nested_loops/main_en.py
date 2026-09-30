MAX = 5
i = 0
while i < MAX:
        sum = 0
        j = MAX
        while j > i:
                sum = sum + j
                j = j - 1
        print(sum)
        i = i + 1
