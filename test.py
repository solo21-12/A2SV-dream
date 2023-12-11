from typing import *

l = 0

def reverseArray(n: int, nums: List[int]) -> List[int]:
    global l
    if l >=  (n-1) - l:
        return 
    
    nums[l],nums[(n-1)-l] = nums[(n-1)-l],nums[l]
    l+= 1
    reverseArray(n,nums)

    return nums

print(reverseArray(7,[3,1,1,4,2,6,11]))