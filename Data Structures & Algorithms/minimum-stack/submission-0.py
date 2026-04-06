class MinStack:
    
    def __init__(self):
        self.minStack = []
        self.hMap = []
    def push(self, val: int) -> None:
        self.minStack.append(val)
        val = min(val, self.hMap[-1] if self.hMap else val)
        self.hMap.append(val)
            
    def pop(self) -> None:
        self.minStack.pop()
        self.hMap.pop()
        
    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        return self.hMap[-1]
