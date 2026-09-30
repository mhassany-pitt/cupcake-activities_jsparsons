def even_first(num_list):
        result = []
        odds = []
        for n in num_list:
                if n % 2 == 0:
                        result.append(n)
                else:
                        odds.append(n)
        for i in range(len(odds)):
                result.append(odds[i])
        return result
