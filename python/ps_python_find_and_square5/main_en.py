list1 = [1, 2, 3, 4, 5]
new_list = []
for i in range(len(list1)):
        num = list1[i]
        if num % 2 == 0:
                new_list.append(num * num)
print(new_list)
