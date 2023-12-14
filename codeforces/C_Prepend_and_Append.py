def checker(word: str) -> int:
    l, r = 0, len(word) - 1

    while l < r:
        if word[l] != word[r]:
            l += 1
            r -= 1
        else:
            break 

    return r - l + 1


n = int(input())

for i in range(n):
    s = int(input())
    word = input()

    print(checker(word))
