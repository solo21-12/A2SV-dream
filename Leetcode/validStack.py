class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        p = 0

        for i in pushed:
            stack.append(i)

            while p < len(popped) and stack and popped[p] == stack[-1]:
                stack.pop()
                p += 1

        return not stack
