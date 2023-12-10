n = int(input())
counter = 0

for i in range(n):
    word = input()

    if  word[1] == '+':
        counter += 1
    else:
        counter -= 1

print(counter)
