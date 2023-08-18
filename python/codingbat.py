def front_back(str):
    if len(str) <= 1:
        return str
    front = str[0]
    back = str[-1]
    middle = str[1 : len(str) - 1]
    return back + middle + front


def last2(str):
    substr = str[-2:]
    the_rest = str[: len(str) - 2]
    counter = 0
    for i in range(0, len(the_rest) - 1):
        print(f"LOOP {the_rest[i : i + 2]}")
        if the_rest[i : i + 2] == substr:
            counter += 1
    return counter


def make_bricks(small, big, goal):
    remainingInches = goal
    if big > 0:
        remainingInches = remainingInches % (5 * big)
        print(remainingInches)
    if small >= remainingInches:
        return True
    else:
        return False


print(make_bricks(3, 2, 8))
print(8 // 5)
