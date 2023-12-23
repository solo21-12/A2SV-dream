def solver(nums):
    l, r = 0, 0

    for i in range(5):
        for j in range(5):
            if nums[i][j] == 1:
                l = i + 1
                r = j + 1
                break

    ans = (abs(3-l) + abs(3-r))

    return ans


nums = []
for i in range(5):
    temp = list(map(int, input().split(" ")))
    nums.append(temp)

print(solver(nums))
