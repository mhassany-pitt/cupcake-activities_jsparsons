amount = 0
i = 0
while i < 4:
    i += 1
    j = 0
    while j < 4:
        j += 1
        k = 0
        while k < 4:
            k += 1
            if k != i and k != j and i != j:
                    amount += 1
                    print(i, j, k)
print("The total number of 3 digit combinations is", amount)
