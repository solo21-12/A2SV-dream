from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        mySum = 0
        piles.sort()
        l, r = 0, len(piles)-1
        while r > l:
            mySum += piles[r-1]
            l += 1
            r -= 2
        return mySum
