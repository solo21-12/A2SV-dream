class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        i = 0
        ans = []
        while i < len(l):
            brk = True
            subArray = nums[l[i]:r[i]+1]
            subArray.sort()

            d = subArray[1] - subArray[0]

            for j in range(len(subArray)-1):
                if subArray[j+1] - subArray[j] != d:
                    ans.append(False)
                    brk = False
                    break
            if brk:
                ans.append(True)
            i += 1

        return ans
