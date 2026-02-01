class Solution:
    def __init__(self, size):
        self.top=-1
        self.size=size
        self.st=[None]*self.size

    def push(self, x):
        if self.top>=self.size-1:
            return "Overflow"
        self.top+=1
        self.st[self.top]=x
        
    def peek(self):
        if self.top==-1:
            return "No elements"
        else:
            return self.st[self.top]
        
    def pop(self):
        if self.top==-1:
            return "Underflow"
        else:
            print(self.st[self.top])
            self.top-=1

    def sizeSt(self):
        return self.top+1