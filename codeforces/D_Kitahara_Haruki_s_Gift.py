from typing import Counter


apples = int(input())
nums = list(map(int, input().split(" ")))
count = Counter(nums)

handers = count[100]
two = count[200]

if two % 2 == 0:
    if handers % 2 != 0:
        print("NO")
    else:
        print("YES")
else:

    if handers > 0 and handers % 2 == 0:
        print("YES")
    else:
        print("NO")
