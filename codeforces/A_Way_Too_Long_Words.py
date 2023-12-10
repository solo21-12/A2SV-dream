num = int(input())
for i in range(num):
    word = input()
    if len(word) > 10:
        len_word = len(word[1:len(word)-1])
        new_word = word[0] +str(len_word)+ word[-1]
        print(new_word)
    else:
        print(word)