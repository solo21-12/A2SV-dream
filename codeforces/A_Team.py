n = int(input())
def team(n:int)->int:
    counter = 0
    for i in range(n):
        nums = map(int,input().split(" "))
        if sum(nums) >= 2:
            counter += 1

    return counter


print(team(n))