class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for num in nums:
            count = sum(val for key, val in counts.items() if key < num)
            ans.append(count)

        return ans
