class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        frequency = {}
        item_sum = 0
        item_count = 0
        n = len(arr) // 2

        for i in arr:
            frequency[i] = frequency.get(i, 0) + 1

        sorted_list = sorted(
            frequency, key=lambda item: frequency[item], reverse=True)

        for i in sorted_list:
            item_sum += frequency[i]
            item_count += 1
            if item_sum >= n:
                return item_count

        return item_count
