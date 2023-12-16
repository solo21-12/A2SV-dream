def solver(n: int) -> int:
    left = right = count = 0
    for i in range(n):
        l, r = map(int, input().split(" "))
        left += l
        right += r

    half = n / 2

    if left > half:
        count += (n - left)
    else:
        count += left

    if right > half:
        count += (n - right)
    else:
        count += right

    return count


n = int(input())

    
print(solver(n))