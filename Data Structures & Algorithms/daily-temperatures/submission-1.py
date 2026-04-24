class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            if len(stack) == 0 or temperatures[stack[-1]] >= temperatures[i]:
                stack.append(i)
            else:
                while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                    res[stack[-1]] = i - stack[-1]
                    stack.pop() 
                stack.append(i)

        return res