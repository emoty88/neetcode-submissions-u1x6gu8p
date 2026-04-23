class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] in ['+', '-', '*', '/']:
                n1 = stack.pop()
                n2 = stack.pop()
                # print(f'{n2} {tokens[i]} {n1}')
                stack.append(int(eval(f'{n2}{tokens[i]}{n1}')))
            else:
                stack.append(int(tokens[i]))

        return stack[0]