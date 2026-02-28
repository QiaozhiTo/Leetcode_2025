class FreqStack:

    def __init__(self):
        self.stacks = {}
        self.maxCnt = 0
        self.cnt = {}        

    def push(self, val: int) -> None:
        valCnt = self.cnt.get(val, 0) + 1
        self.cnt[val] = valCnt
        if valCnt > self.maxCnt:
            self.maxCnt = valCnt
            self.stacks[self.maxCnt] = []
        self.stacks[valCnt].append(val)
    def pop(self) -> int:
        res = self.stacks[self.maxCnt].pop()
        self.cnt[res] -= 1
        if not self.stacks[self.maxCnt]:
            self.maxCnt -= 1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()