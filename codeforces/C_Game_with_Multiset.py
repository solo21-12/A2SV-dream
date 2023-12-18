def solve():
    freq = [0] * 32
    n = int(input())
    while n > 0:
        n -= 1
        tp = list(map(int, input().split()))
        if tp[0] == 1:
            x = tp[1]
            freq[x] += 1
        else:
            w = tp[1]
            temp = freq.copy()
            pos = True
            bit = 0
            while bit < 30:
                if (w >> bit) & 1:
                    if temp[bit]:
                        temp[bit] -= 1
                    else:
                        pos = False
                temp[bit + 1] += temp[bit] // 2
                bit += 1
            if pos:
                print("YES")
            else:
                print("NO")

totalTests = 1
# totalTests = int(input())
testNo = 1
while testNo <= totalTests:
    solve()
    testNo += 1
