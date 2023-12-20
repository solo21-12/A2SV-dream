from collections import Counter


def solver(word):
    count = Counter(word)
    ans  =0
 
    for key,value in count.items():
        if value >= (ord(key) - ord('A') + 1):
            ans += 1

    return ans


t = int(input())

for i in range(t):
    n = input()
    word = [char for char in input()]
    print(solver(word))