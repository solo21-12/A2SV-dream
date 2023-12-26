from typing import List


def remove_smallest(nums:List[int],n):
    nums.sort()
    for i in range(n-1):
        if abs(nums[i+1] - nums[i]) > 1:
            return "NO"
        
    return "YES"

t = int(input())

for i in range(t):
    n = int(input())
    nums = list(map(int,input().split(" ")))
    print(remove_smallest(nums,n))


