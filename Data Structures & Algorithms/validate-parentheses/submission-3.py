class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(':')', '[':']', '{':'}'}

        for c in s:
            if c in pairs:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if pairs[last] != c:
                    return False

        return True if len(stack)==0 else False
        