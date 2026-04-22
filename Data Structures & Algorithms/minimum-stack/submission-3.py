class MinStack:

    def __init__(self):
        self.s = []
        self.mins = []
        

    def push(self, val: int) -> None:
        self.s.append(val)
        if len(self.mins) == 0:
            self.mins.append(val)
        else:
            self.mins.append(min(self.mins[-1], val))
        

    def pop(self) -> None:
        poped = self.s.pop()
        self.mins.pop()
        

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        print(self.mins)
        return self.mins[-1]
        
