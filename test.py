from typing import *


def countFrequency(n: int, m: int, edges: List[List[int]]):
    nums = [0] * n
    for i in edges:
        if i <= n:
            nums[i-1] += 1

    return nums


n, m = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
print(countFrequency(n,m,arr))