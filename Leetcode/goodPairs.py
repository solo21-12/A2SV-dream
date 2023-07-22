from typing import List


def numIdenticalPairs(self, nums: List[int]) -> int:
    frequency = {}
    count = 0
    for i in nums:
        frequency[i] = frequency.get(i, 0) + 1

    for key, val in frequency.items():
        currentSum = (val*(val-1)) // 2
        count += currentSum

    return count


#  Number of good pairs equals the following formula val * (val - 1) // 2
