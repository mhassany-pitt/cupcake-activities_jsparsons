new_list = []
for element in old_list:
        if element not in new_list:
                new_list.append(element)
print("The original list:", old_list)
print("The new list:", new_list)
