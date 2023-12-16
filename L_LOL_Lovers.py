def find_division(n, items):
    bread_count = items.count('L')
    onion_count = items.count('O')
    
    for i in range(1, n):
        left_bread = items[:i].count('L')
        left_onion = items[:i].count('O')
        
        right_bread = bread_count - left_bread
        right_onion = onion_count - left_onion
        
        if left_bread != right_bread and left_onion != right_onion:
            print(i)
            return
    
    print(-1)

# Reading input
n = int(input())
items = input().strip()

# Calling function with inputs
find_division(n, items)
