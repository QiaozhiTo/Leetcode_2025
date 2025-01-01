# two stacks
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.ministack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        self.ministack.append(min(val, self.ministack[-1] if self.ministack else val))
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.ministack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.ministack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()