from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        temp = [0] * n
        for i in range(n):
            j = (k + i) % n
            temp[j] = nums[i]

        for i in range(n):
            nums[i] = temp[i]
