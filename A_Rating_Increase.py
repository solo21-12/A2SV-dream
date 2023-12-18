t = int(input())


def solver(t: int):
    for i in range(t):
        l, r = 0, 1
        word = input()

        while r < len(word):
            if int(word[r]) > 0 and int(word[l:r]) < int(word[r:len(word)]):
                print(word[l:r], word[r:])
                break

            r += 1

        else:
            print(-1)
        

solver(t)
