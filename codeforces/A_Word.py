def checkWord(word: str) -> str:
    up = down = 0
    for i in word:
        if i == i.upper():
            up += 1
        else:
            down += 1

    if up > down:
        return word.upper()

    return word.lower()


word = input()
print(checkWord(word))
