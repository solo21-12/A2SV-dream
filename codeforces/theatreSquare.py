import math

n, m, a = map(int, input().split())


def square2(n, m, a):
    x = math.ceil(n / a)
    y = math.ceil(m/a)

    return (x * y)


print(square2(n, m, a))
