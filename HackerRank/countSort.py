def countSwaps(arr):
    counts = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                counts += 1
                arr[j], arr[i] = arr[i], arr[j]
    print(f'Array is sorted in {counts} swaps.')
    print(f'First Element: {arr[0]}')
    print(f'Last Element: {arr[-1]}')
