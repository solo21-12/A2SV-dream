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
