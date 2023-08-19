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


def recursiveFib(num):
    if num == 0 or num == 1:
        return num
    return recursiveFib(num - 1) + recursiveFib(num - 2)


print(iterativeFib(12))
print(recursiveFib(12))
