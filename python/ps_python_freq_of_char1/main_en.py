def freq_of_char(str):
        num_of_char = {}
        for letter in str:
                if letter in num_of_char:
                        num_of_char[letter] += 1
                else:
                        num_of_char[letter] = 1
        return num_of_char
