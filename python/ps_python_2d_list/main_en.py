COUNT = 3
list1 = []
for i in range(COUNT):
        list2 = [0] * COUNT
        for j in range(COUNT):
                list2[j] = i * COUNT + j
        list1.append(list2)
list1[2][2] = 99
print(list1)
