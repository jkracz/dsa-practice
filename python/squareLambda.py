# square
li = [5, 4, 3]
print(list(map(lambda item: item**2, li)))

# list sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

a.sort(key=lambda tup: tup[1])
print(a)

# dupes (comprehensions)

some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

dupes = list({char for char in some_list if some_list.count(char) > 1})

print(duplicates)
print(dupes)
