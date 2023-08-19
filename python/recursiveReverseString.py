def reverseStrIterative(string):
    i = len(string) - 1
    rev = ""
    while i >= 0:
        rev += string[i]
        i -= 1
    return rev


def reverseStrRecursive(string):
    if len(string) == 1:
        return string
    return reverseStrRecursive(string[1:]) + string[0]


print(reverseStrRecursive("yoyo mastery"))
# //should return: 'yretsam oyoy'
