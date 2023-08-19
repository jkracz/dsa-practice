# both functions are O(n) runtime complexity
# the recursive func is called n times, and our iterative loop will also run n times


def recursiveFactorial(num):
    if num == 1:
        return 1
    return num * recursiveFactorial(num - 1)


def iterativeFactorial(num):
    accumulator = 1
    for i in range(2, num + 1):
        accumulator *= i

    return accumulator


print(iterativeFactorial(2))
print(recursiveFactorial(2))
