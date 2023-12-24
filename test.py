def sortedArray(a: [int], b: [int]) -> [int]:
    ans = []
    l,r=0,0
    while l < len(a) and r < len(b):
        if a[l] < b[r]:
            if a[l] not in ans:
                ans.append(a[l])
            l+= 1
        elif a[l] == b[r]:
            if a[l] not in ans:
                ans.append(a[l])
            l += 1
            r +=1
        else:
            if b[r] not in ans:
                ans.append(b[r])
            r += 1

    for i in range(l,len(a)):
        if a[i] not in ans:
            ans.append(a[i])
             
    for i in range(r,len(b)):
        if b[i] not in ans:
            ans.append(b[i])

    return ans





num1 = list(map(int,input().split(" ")))
num2 = list(map(int,input().split(" ")))

print(sortedArray(num1,num2))


