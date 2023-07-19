def max_dominoes(M, N):
    total_squares = M * N
    max_dominoes = total_squares // 2
    return max_dominoes

# Accept input from the user in a single line
M, N = map(int, input().split())

max_dominoes_count = max_dominoes(M, N)
print(max_dominoes_count)