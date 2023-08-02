from typing import List


class Solution:
    def longestSubarray(self,nums: List[int], limit: int) -> int:
        max_queue = []
        min_queue = [] 
        l = 0
        ans = 0

        for r in range(len(nums)):
            while max_queue and nums[r] > nums[max_queue[-1]]:
                max_queue.pop()

            while min_queue and nums[r] < nums[min_queue[-1]]:
                min_queue.pop()

            max_queue.append(r)
            min_queue.append(r)

            while nums[max_queue[0]] - nums[min_queue[0]] > limit:
                if max_queue[0] == l:
                    max_queue.pop(0)
                if min_queue[0] == l:
                    min_queue.pop(0)
                l += 1

            ans = max(ans, r - l + 1)

        return ans