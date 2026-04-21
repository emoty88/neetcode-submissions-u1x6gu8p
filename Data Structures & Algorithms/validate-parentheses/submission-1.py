class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if last == '(' and c != ')' or last == '[' and c != ']' or last == '{' and c != '}':
                    return False

        return True if len(stack)==0 else False
        