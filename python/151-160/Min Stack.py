class MinStack:
    stack=[]
    Min=[]
    
    def __init__(self):
        self.stack=[]
        self.Min=[]
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if len(self.Min)>0:
            
            t=self.Min[-1]
            if t<=x:
                self.Min.append(t)
            else:
                self.Min.append(x)
        else:
            self.Min.append(x)

    # @return nothing
    def pop(self):
        if len(self.stack)>0:
            del self.stack[-1]
            del self.Min[-1]

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        if len(self.stack)>0:
            return self.Min[-1]
