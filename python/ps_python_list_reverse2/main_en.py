list1 = [1, 2, 3, 4, 5]
new_list = []
i = 0
while i < len(list1):
        element = list1[i]
        new_list.insert(0, element)
        i += 1
print(new_list)
