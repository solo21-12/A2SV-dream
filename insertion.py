def printer(arr):
    for i in arr:
        print(i, end=' ')
    print("\t")


def insertionSort1(n, arr):
    for i in range(n-1, 0, -1):
        j = i
        temp = arr[j]
        while j > 0 and arr[j-1] >= arr[j]:
            arr[j] = arr[j-1]
            j -= 1
            printer(arr)
        arr[j] = temp

    printer(arr)
