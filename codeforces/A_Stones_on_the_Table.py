

def counter(word:str)->int:
    count = 0
    l,r=0,1

    while  r < len(word):
        if s[l] == s[r]:
            count += 1
        
        r += 1
        l += 1

    return count
        


n = int(input())
s = input()

print(counter(s))