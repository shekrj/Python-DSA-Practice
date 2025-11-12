class Solution:
    def __init__(self, size):
        self.size=size
        self.que=[None]*self.size
        self.cursize=0
        self.start=-1
        self.end=-1
    
    def push(self, x):
        if self.cursize==self.size:
            return "Overflow"
        if self.cursize==0:
            self.start=0
            self.end=0
        else:
            self.end=(self.end+1)%self.size
        self.que[self.end]=x
        self.cursize+=1
    
    def pop(self):
        if self.cursize==0:
            return "Underflow"
        el=self.que[self.start]
        if self.cursize==1:
            self.start=-1
            self.end=-1
        else:
            self.start=(self.start+1)%self.size
        self.cursize-=1
        return el
    
    def top(self):
        if self.cursize==0:
            return "Underflow"
        else:
            return self.que[self.start]
    
    def sizeFunc(self):
        return self.cursize