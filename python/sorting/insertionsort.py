numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


# my failed first attempt
def insertionSortBad(arr):
    length = len(arr)
    for i in range(1, length):
        destination = i
        while destination - 1 >= 0 and arr[i] < arr[i - 1]:
            destination -= 1
        j = i
        while j >= destination:
            tmp = arr[j]
        for j in range(destination, i):
            tmp = arr[j + 1]
            arr[j + 1] = arr[j]


# O(N^2) time complexity, O(1) space complexity bc it is happening in place
def insertionSort(arr):
    length = len(arr)
    if length <= 1:
        return

    for i in range(1, length):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


insertionSort(numbers)
print(numbers)


# trying again on my own
# so for insertion sort, you assume that there is a sorted subarray at the front of the full array
# you need to look at each element, compare it with the last element in the sub array (the one before it), and determine where it fits
# insertion sort is typically O(n^2), meaning we will likely deal with nested loops

numbers2 = [1, 3, 4, 5, 2, 63, 87, 283, 4, 0]


def insertionSortBreak(arr):
    length = len(arr)
    if length <= 1:
        return

    for i in range(1, length):
        currentVal = arr[i]
        j = i - 1
        while arr[j] > currentVal and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = currentVal


insertionSortBreak(numbers2)
print(numbers2)
