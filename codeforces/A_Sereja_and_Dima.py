def game(n, nums):
    serja = dima = 0

    l, r = 0, len(nums) - 1

    for i in range(n):
        if i % 2 == 0:
            if nums[l] > nums[r]:
                serja += nums[l]
                l += 1
            else:
                serja += nums[r]
                r -= 1
        else:
            if nums[l] > nums[r]:
                dima += nums[l]
                l += 1
            else:
                dima += nums[r]
                r -= 1

    return [serja, dima]


n = int(input())
nums = list(map(int, input().split(" ")))

res = game(n, nums)
for i in res:
    print(i,end=" ")