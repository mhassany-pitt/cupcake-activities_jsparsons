list_num = [7, 2, 4, 1, 3, 5, 6, 8]
i = 0
j = len(list_num) - 1
while i < j:
        while i <= j and list_num[i] % 2 == 0:
                i += 1
        while i <= j and list_num[j] % 2 != 0:
                j -= 1
        if i < j:
                temp = list_num[i]
                list_num[i] = list_num[j]
                list_num[j] = temp
print(list_num)
