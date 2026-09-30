def find_and_square(lst):
        new_list = []
        for i in lst:
                num = i
                if num % 2 == 0:
                        new_list.append(num * num)
        return new_list
