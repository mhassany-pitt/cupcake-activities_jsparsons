list1 = [1, 2, 3, 4, 5]
new_list = []
i = 0
while i < len(list1):
        num = list1[i]
        if num % 2 == 0:
                new_list.append(num * num)
        i += 1
print(new_list)
