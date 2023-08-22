numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


# O(N^2) due to nested loops, but O(1) space complexity bc we are sorting in place
def selectionSort(arr):
    length = len(arr)
    for i in range(length):
        smallestIndex = i
        for j in range(i, length):
            if arr[j] < arr[smallestIndex]:
                smallestIndex = j
        tmp = arr[i]
        arr[i] = arr[smallestIndex]
        arr[smallestIndex] = tmp


selectionSort(numbers)
print(numbers)
