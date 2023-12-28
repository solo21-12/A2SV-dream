t = int(input())


def solver(nums):
    if nums[0] == nums[1]:
        return nums[2]
    elif nums[0] == nums[2]:
        return nums[1]
    return nums[0]

for i in range(t):
    nums = list(map(int, input().split(" ")))
    print(solver(nums))
