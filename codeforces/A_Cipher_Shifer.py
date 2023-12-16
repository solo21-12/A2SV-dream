def decrypt(t, test_cases):
    for _ in range(t):
        n, s = test_cases[_]
        decrypted = ''
        for i in range(0, n, 2):
            decrypted += s[i]
        print(decrypted)

# Reading input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    s = input().strip()
    test_cases.append((n, s))

# Calling function with inputs
decrypt(t, test_cases)
