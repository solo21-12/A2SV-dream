def pangram(n: int, word: str) -> str:
    if n < 26:
        return "NO"

    chars = [0] * 26
    for i in word:
        if not chars[ord(i.lower()) - ord('a')]:
            chars[ord(i.lower()) - ord('a')] += 1

    return "YES" if sum(chars) == 26 else "NO"


n = int(input())
word = input()

print(pangram(n, word))
