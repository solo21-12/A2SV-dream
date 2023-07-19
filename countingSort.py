def countingSort(arr):
    ans = [0] * 100
    for i in arr:
        ans[i] += 1
    return ans
