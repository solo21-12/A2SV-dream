n = int(input())
nums = list(map(int, input().split()))

max_ones = nums.count(1)

ones = 0
for i in range(n):
    for j in range(i, n):
        after_flip = max_ones + \
            nums[i:j + 1].count(0) - nums[i:j + 1].count(1)
        ones = max(ones, after_flip)

print(ones)
