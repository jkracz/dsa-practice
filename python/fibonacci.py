# iterative will be faster in this case, because we only need to loop through ~n times (O(N))
# the recursive approach will actually take O(2^N), bc the number of recursive calls grows exponentially with N


def iterativeFib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    a = 0
    b = 1
    for i in range(1, num):
        tmp = a
        a = b
        b = tmp + b
    return b


slow_calculations = 0


def recursiveFib(num):
    global slow_calculations
    slow_calculations += 1
    if num == 0 or num == 1:
        return num
    return recursiveFib(num - 1) + recursiveFib(num - 2)


# to improve the recursive func, we should use memoization

fast_calculations = 0


def memoize_fib(func):
    cache = {}

    def mem_wrapper(num):
        if num not in cache:
            global fast_calculations
            fast_calculations += 1
            cache[num] = func(num)
        return cache[num]

    return mem_wrapper


@memoize_fib
def memRecursiveFib(num):
    if num == 0 or num == 1:
        return num
    return memRecursiveFib(num - 1) + memRecursiveFib(num - 2)


print(f"SLOW res: {recursiveFib(35)} calcs: {slow_calculations}")
print(f"FAST res: {memRecursiveFib(100)} calcs: {fast_calculations}")
