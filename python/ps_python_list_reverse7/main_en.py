def list_reverse(lst):
        new_list = [0] * len(lst)
        j = len(lst)
        for number in lst:
                j = j - 1
                new_list[j] = number
        return new_list
list1 = [1, 2, 3, 4, 5]
list2 = list_reverse(list1)
print(list2)
