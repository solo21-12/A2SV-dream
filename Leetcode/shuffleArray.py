class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_num = []
        for i in range(n):
            new_num.append(nums[i])
            new_num.append(nums[i+n])
        return new_num