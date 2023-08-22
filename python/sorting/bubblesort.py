# runs in O(n^2) time, O(1) space complexity bc we sort in place

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def bubbleSort(arr):
    transformations = True
    while transformations:
        transformations = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                transformations = True
                tmp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = tmp


# this bubblesort implementation also works in the same time and space complexity, however it could be less efficient
# bubblesort2 has a loop for each element of the collection, while the first implementation will stop looping if it notices there are no more transformations being made
# in an avg case, this makes no difference, but with large data set where the back half might be sorted, it could be more efficient
def bubbleSort2(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length - 1):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp


bubbleSort(numbers)
# bubbleSort2(numbers)
print(numbers)
