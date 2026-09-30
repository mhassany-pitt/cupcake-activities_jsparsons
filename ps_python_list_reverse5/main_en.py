def list_reverse(lst):
        new_list = [0] * len(lst)
        j = len(lst) - 1
        for i in range(len(lst)):
                j = j - 1
                new_list[j] = lst[i]
        return new_list
list1 = [1, 2, 3, 4, 5]
list2 = list_reverse(list1)
print(list2)
