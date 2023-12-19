class Solution:
    def checkSelfDivide(self, num):
        temp = num
        while temp > 0:
            i = temp % 10
            temp = temp // 10
            if i == 0 or num % i != 0:
                return False

        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        nums = []
        for i in range(left, right + 1):
            if self.checkSelfDivide(i):
                nums.append(i)

        return nums
