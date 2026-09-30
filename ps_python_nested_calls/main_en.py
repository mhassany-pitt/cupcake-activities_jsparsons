def calculate(first, second):
    return second * 3 + first
def double(value):
    return value * 2
print(double(double(5)))
print(calculate(double(3), 2 + calculate(5, 1)))
