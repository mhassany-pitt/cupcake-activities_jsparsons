def remove_dup(list_of_num):
        new_list = []
        for element in list_of_num:
                if element not in new_list:
                        new_list.append(element)
        return new_list
