class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minimum = None
        self.minstack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.minstack:
            self.minimum = x
            self.minstack.append(x)
        elif x <= self.minimum:
            self.minimum = x
            self.minstack.append(x)
        else:
            self.minstack.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        item = self.minstack.pop()
        if self.minstack:
            self.minimum = min(self.minstack)
        else:
            self.minimum = None
        return item

    def top(self):
        """
        :rtype: int
        """
        return self.minstack[len(self.minstack) - 1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minimum
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()