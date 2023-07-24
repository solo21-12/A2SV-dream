class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_tags = ['[', '{', '(']
        tags = {
            '}': '{',
            ')': "(",
            ']': '[',
        }
        if len(s) < 2:
            return False

        for i in s:
            if i in open_tags:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                else:
                    close = stack.pop()
                    if tags[i] != close:
                        return False

        return True if len(stack) == 0 else False
