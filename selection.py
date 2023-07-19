class Solution:
    def select(self, arr, j):
        ans = j - 1

        for i in range(j, len(arr)):
            if arr[i] <= arr[ans]:
                ans = i

        return ans

    def selectionSort(self, arr, n):
        l = 0
        while l < n - 1:
            min_val = self.select(arr, l+1)

            arr[l], arr[min_val] = arr[min_val], arr[l]
            l += 1
        return arr
