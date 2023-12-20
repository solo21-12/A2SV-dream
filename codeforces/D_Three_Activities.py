def max_sum_no_match(n, arr1, arr2, arr3):
    arr1.sort(reverse=True)
    arr2.sort(reverse=True)
    arr3.sort(reverse=True)

    result = 0
    for x in range(3):
        for y in range(3):
            for z in range(3):
                if arr1[x][1] != arr2[y][1] and arr1[x][1] != arr3[z][1] and arr2[y][1] != arr3[z][1]:
                    result = max(result, arr1[x][0] + arr2[y][0] + arr3[z][0])
    return result

t_cases = int(input())
for _ in range(t_cases):
    size = int(input())
    array1 = list(map(int, input().split()))
    array2 = list(map(int, input().split()))
    array3 = list(map(int, input().split()))

    array1 = [(array1[i], i + 1) for i in range(size)]
    array2 = [(array2[i], i + 1) for i in range(size)]
    array3 = [(array3[i], i + 1) for i in range(size)]

    result = max_sum_no_match(size, array1, array2, array3)
    print(result)
