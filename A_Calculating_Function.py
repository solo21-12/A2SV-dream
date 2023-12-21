def calculate_f(n):
    return n // 2 if n % 2 == 0 else -(n + 1) // 2

n = int(input().strip())

result = calculate_f(n)
print(result)
