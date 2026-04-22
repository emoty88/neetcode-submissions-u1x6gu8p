class MinStack:

    def __init__(self):
        self.s = []
        self.min = float('inf')
        

    def push(self, val: int) -> None:
        self.s.append(val)
        self.min = min(self.min, val)
        

    def pop(self) -> None:
        self.s.pop()
        

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return min(self.s)
        
