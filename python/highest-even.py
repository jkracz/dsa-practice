def highest_even(li):
    # init highest even element (start at 0)
    # got thru list; check if each element is even and if it's greater than the current highest
    current_highest_even = 0
    for item in li:
        if item % 2 == 0 and item > current_highest_even:
            current_highest_even = item
    return current_highest_even


print(highest_even([10, 1, 2, 3, 400, 5, 8, 11]))
x = [5, [4, 4], "poo"]
