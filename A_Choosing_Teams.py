from typing import List


def choose_team(nums: List[int], k: int) -> int:
    teams = 0
    for num in nums:
        if num + k <= 5:
            teams += 1

    return (teams) // 3


n, k = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))

print(choose_team(nums, k))
