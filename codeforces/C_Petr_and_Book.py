def solver(n: int, days) -> int:
    count = 0
    i = 0
    while True:
        count += days[i]
        if count >= n:
            return i + 1 
        i = (i + 1) % len(days)


n = int(input())
days = [int(num) for num in input().split(" ")]
print(solver(n, days))
