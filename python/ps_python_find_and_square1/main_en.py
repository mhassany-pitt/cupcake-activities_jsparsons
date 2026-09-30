def find_and_square(lst):
        new_list = []
        i = 0
        while i < len(lst):
                num = lst[i]
                if num % 2 == 0:
                        new_list.append(num * num)
                i += 1
        return new_list
