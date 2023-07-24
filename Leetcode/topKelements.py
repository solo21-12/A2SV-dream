def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    frequency = {}
    ans = []
    for i in nums:
        frequency[i] = frequency.get(i, 0)+1

    frequently_elements = sorted(
        frequency, key=lambda x: frequency[x], reverse=True)[:k]

    return frequently_elements
