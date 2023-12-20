class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        ans = n * 2
        for i in range(1,ans):
            if i % 2 == 0 and i % n == 0:
                ans = min(ans,i)
        return ans

        