def even_first(num_list):
        i = 0
        j = len(num_list) - 1
        while i < j:
                while i < j and num_list[i] % 2 == 0:
                        i += 1
                while i < j and num_list[j] % 2 != 0:
                        j -= 1
                if i < j:
                        temp = num_list[i]
                        num_list[i] = num_list[j]
                        num_list[j] = temp
        return num_list
