# brute force
class Solution:
    def checkExist(self, num, start, nums):
        count = 0
        for i in range(start, len(nums)):
            if nums[i] == num:
                count += 1
        return count

    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            count += self.checkExist(nums[i], i+1, nums)

        return count


# optimized
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        for value in count.values():
            ans += ((value * (value - 1)) // 2)

        return ans
