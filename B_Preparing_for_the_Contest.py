def reverse(l, r, nums):
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l+1, r - 1


def solver(n, k):
    num = []
    ans = [0] * n
    for i in range(1, n+1):
        num.append(i)
    m = n - k -1
    for i in range(len(num)):
        ans[(i+m) % n] = num[i]

    reverse(0, m-1, ans)
    return ans


t = int(input())
for i in range(t):
    n, k = map(int, input().split(" "))
    print(solver(n, k))
