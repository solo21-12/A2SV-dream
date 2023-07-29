class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ope = ['+', '*', '/', '-']
        for i in tokens:
            if i in ope:
                a = (stack.pop())
                b = (stack.pop())
                if i == '+':
                    stack.append((a+b))
                elif i == '-':
                    stack.append((b - a))
                elif i == '*':
                    stack.append((a*b))
                if i == '/':
                    stack.append((int(b/a)))
            else:
                stack.append(int(i))

        return stack[-1]
