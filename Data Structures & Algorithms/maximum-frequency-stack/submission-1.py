class FreqStack:

    def __init__(self):
        self.count = {}
        self.maxCount = 0
        self.stacks = {}

    def push(self, val: int) -> None:
        self.count[val] = 1 + self.count.get(val, 0)
        if self.count[val] > self.maxCount:
            self.maxCount = self.count[val]
            self.stacks[self.maxCount] = []
        self.stacks[self.count[val]].append(val)



    def pop(self) -> int:
        res = self.stacks[self.maxCount].pop()
        self.count[res] -= 1
        if self.stacks[self.maxCount] == []:
            self.maxCount -= 1
        return res


        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()