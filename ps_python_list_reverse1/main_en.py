def list_reverse(lst):
        new_list = []
        i = 0
        while i < len(lst):
                element = lst[i]
                new_list.insert(0, element)
                i += 1
        return new_list
list1 = [1, 2, 3, 4, 5]
list2 = list_reverse(list1)
print(list2)
