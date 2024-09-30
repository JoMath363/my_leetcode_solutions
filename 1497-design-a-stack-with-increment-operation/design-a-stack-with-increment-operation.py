class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.maxSize = maxSize
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        if len(self.stack) < self.maxSize:
            self.stack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """

        if len(self.stack):
            return self.stack.pop()
            
        return -1
            
        

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """

        print(self.stack)

        size = min(len(self.stack), k)

        for i in range(size):
            self.stack[i] += val

        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)