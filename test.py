class Solution:
    def subArraySum(self, arr, n, s):
        start = end = currentSum = 0

        while end < n or currentSum >= s:
            if currentSum == s:
                return [start+1, end+1]

            while currentSum > s:
                currentSum -= arr[start]
                start += 1

            if end < n:
                currentSum += arr[end]

            end += 1
        return [-1]
