class InvalidInputError(Exception):
    def __init__(self, n):
        self.n = n

# recursive implementation
def fib1(n):
    if n < 0:
        raise InvalidInputError(n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib1(n - 1) + fib1(n - 2)

# iterative implementation
def fib2(n):
    if n < 0:
        raise InvalidInputError(n)
    tmp1 = 0
    tmp2 = 1
    for i in range(0, n):
        tmp3 = tmp1
        tmp1 = tmp2
        tmp2 = tmp3 + tmp2
    return tmp1

# iterative implementation with arrays
def fib3(n):
    if n < 0:
        raise InvalidInputError(n)
    l = [0, 1]
    for i in range(2, n + 1):
        l.append(l[i - 1] + l[i - 2])
    return l[n]

# fib1(25)
# fib2(25)
# fib3(25)
