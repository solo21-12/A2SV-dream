def icpcBalloons()->int:
    n = int(input())
    s = input()
    counter = 0
    solved = []

    for i in s:
        if i not in solved:
            counter += 1
        solved.append(i)
        counter += 1
    return counter
    
        


t = int(input())

for i in range(t):
    print(icpcBalloons())