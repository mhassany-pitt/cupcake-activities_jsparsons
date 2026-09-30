def factorial(n):
    if n < 3:
        return n
    else:
        return factorial(n-1) * n
