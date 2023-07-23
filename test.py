import math

n, m, a = map(int, input().split())


def square(n, m, a):
    rec = n * m
    sqr = a*a
    if rec % sqr == 0:
        return rec // sqr
    else:
        x = (n//a) + 1
        m = m - a
        b = ((m//a) + 1) * x
        return b + x




def square2(n, m, a):
    x = math.ceil(n / a)
    y = math.ceil(m/a)

    return (x * y) 


print(square2(n,m,a))
