from math import trunc
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for n in tokens:
            if n in ['+', '-', '*', '/']:
                n1 = stack.pop()
                n2 = stack.pop()
                if n == "+": stack.append(n2+n1)
                elif n == "-": stack.append(n2-n1)
                elif n == "*": stack.append(n2*n1)
                elif n == "/": stack.append(trunc(n2/n1))
            else:
                stack.append(int(n))

        return stack[0]