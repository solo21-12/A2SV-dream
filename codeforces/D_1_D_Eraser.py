def min_operations(t, test_cases):
    for _ in range(t):
        n, k, s = test_cases[_]
        black_count = s.count('B')
        segments = black_count // k
        if black_count % k != 0:
            segments += 1
        print(segments)

# Reading input
t = int(input())
test_cases = []
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    test_cases.append((n, k, s))

# Calling function with inputs
min_operations(t, test_cases)
