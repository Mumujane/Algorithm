def fib(n):
    if n <= 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(20))


#
def dynamicfib(n):
    f = 0
    g = 1
    while 0 < (n):
        g = g + f
        f = g - f
        n -= 1

    return g


print(dynamicfib(20))
