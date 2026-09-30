def list_of_remainders(list1, list2):
        new_list = []
        if len(list1) == len(list2):
                for i in range(len(list1)):
                        if list2[i] == 0:
                                new_list.append(2)
                        else:
                                result = list1[i] % list2[i]
                                new_list.append(result)
        return new_list
list1 = [19, 3, 4, 2]
list2 = [4, 2, 1, 0]
print(list_of_remainders(list1, list2))
