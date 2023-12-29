import math

def can_build_square(buckets):
    total_squares = sum(buckets)
    square_side = int(math.sqrt(total_squares))
    
    if square_side * square_side == total_squares:
        return "YES"
    else:
        return "NO"

t = int(input())

for _ in range(t):
    n = int(input()) 
    squares_in_buckets = list(map(int, input().split()))  # Squares in each bucket
    
    result = can_build_square(squares_in_buckets)
    print(result)
