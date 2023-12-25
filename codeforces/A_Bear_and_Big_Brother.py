n, k = map(int, input().split(" "))
count = 0
while n <= k:
    n *= 3
    k *= 2
    count += 1


print(count)
