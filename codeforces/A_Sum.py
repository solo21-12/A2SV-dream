t = int(input())


def solver(nums):
    total = sum(nums)
    for i in nums:
        if i == (total - i):
            return "YES"
    return "NO"


for i in range(t):
    nums = list(map(int, input().split(" ")))
    print(solver(nums))
