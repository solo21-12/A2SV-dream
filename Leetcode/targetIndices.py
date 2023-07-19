class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        temp = {}
        for i in range(len(nums)):
            temp[nums[i]] = temp.get(nums[i], []) + [i]

        return temp[target] if target in nums else []
