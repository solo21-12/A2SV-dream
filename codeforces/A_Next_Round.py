def nextRound(nums, k, n):
    kth = nums[k - 1]
    counter = 0
    for i in range(n):
        if nums[i] >= kth and nums[i] > 0:
            counter += 1

    return counter


n, k = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))
print(nextRound(nums, k, n))
