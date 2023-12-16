def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    
    for i in range(n):
        if (a[i] % 2) != (b[i] % 2):
            return False
    return True

t = int(input())
for _ in range(t):
    print("YES" if solve() else "NO")
