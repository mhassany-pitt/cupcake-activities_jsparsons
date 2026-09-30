list1 = [1, 2, 3, 4, 5]
new_list = [0] * len(list1)
i = 0
j = len(list1) - 1
while i < len(list1):
        j = j - 1
        new_list[j] = list1[i]
        i += 1
print(new_list)
