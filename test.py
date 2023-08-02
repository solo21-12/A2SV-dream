from typing import List


def longestSubarray( nums: List[int], limit: int) -> int:
        l,r=0,1
        ans = 0

        while r < len(nums):
            temp = nums[l:r]
            a = max(temp)
            b = min(temp)
            diff = abs( a- b)
            if diff < limit and diff > 0:
                ans = max(len(temp),ans)

            if diff < limit:
                r += 1
            else:
                l += 1

        return ans 



print(longestSubarray([4,2,2,2,4,4,2,2],0))