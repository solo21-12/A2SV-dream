def boyOrGirl(word: str) -> str:
    counter = {}
    distinct = 0
    for i in word:
        if i in counter:
            counter[i] += 1
            distinct -= 1
        counter[i] = 1
        distinct += 1

    return "CHAT WITH HER!" if distinct % 2 == 0 else "IGNORE HIM!"


word = input()


print(boyOrGirl(word))