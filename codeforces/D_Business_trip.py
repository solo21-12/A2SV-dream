k = int(input())
gr = list(map(int, input().split()))

gr.sort(reverse=True)

m = 0
cg = 0

while  cg < k and  m < 12:
     cg +=  gr[ m]
     m += 1

if  cg >= k:
    print( m)
else:
    print(-1)