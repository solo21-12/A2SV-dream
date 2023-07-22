from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = sorted(nums, key=lambda item: int(item), reverse=True)
        return nums[k-1]
