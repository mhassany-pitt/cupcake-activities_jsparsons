str = "Summer"
num_of_char = {}
for letter in str:
        if letter in num_of_char:
                num_of_char[letter] += 1
        else:
                num_of_char[letter] = 1
print(num_of_char)
