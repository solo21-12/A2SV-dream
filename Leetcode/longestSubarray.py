k = int(input())
a = list(map(int, input().split(" ")))


def solver(a, k):
    sum_counter = 0
    counter = 0
    l, r = 0, 0

    while r < len(a):
        sum_counter += a[r]

        while sum_counter > k and l <= r:
            sum_counter -= a[l]
            l += 1

        if sum_counter == k:
            counter = max(counter, (r-l+1))

        r += 1

    return counter


print(solver(a, k))
