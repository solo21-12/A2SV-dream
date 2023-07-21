from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)

        def sorter(nums):
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i] + nums[j] < nums[j] + nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
            return nums

        nums = sorter(nums)

        return str(int("".join(nums)))



class Solution2:
    def largestNumber(self, nums: List[int]) -> str:
        for i,n in enumerate(nums):
            nums[i] = str(n)

        def comparetor(n1,n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        nums = sorted(nums,key = cmp_to_key(comparetor))

        return str(int("".join(nums)))