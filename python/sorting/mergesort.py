numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def mergeSort(arr):
    arrLength = len(arr)
    mid = arrLength // 2
    if arrLength == 1:
        return arr

    left = arr[:mid]
    right = arr[mid:]

    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    leftLen = len(left)
    rightLen = len(right)
    merged = []
    i = 0
    j = 0
    while i < leftLen and j < rightLen:
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < leftLen:
        merged.append(left[i])
        i += 1
    while j < rightLen:
        merged.append(right[j])
        j += 1
    print(merged)

    return merged


print(mergeSort(numbers))
# print(numbers)
