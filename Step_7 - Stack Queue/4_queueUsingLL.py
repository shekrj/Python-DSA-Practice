class Node:
    def __init__(self, data=0, next=None):
        self.data=data
        self.next=next
class Queue:
    def __init__(self):
        self.start=None
        self.end=None
        self.size=0

    def push(self, x):
        newNode=Node(x)
        if self.start is None:
            self.start=self.end=newNode
        else:
            self.end.next=newNode
            self.end=newNode
        self.size+=1
    
    def pop(self):
        if self.start is None:
            return "Underflow"
        poppedData=self.start.data
        self.start=self.start.next
        if self.start is None:
            self.end = None
        self.size-=1
        return poppedData
    
    def top(self):
        if self.start is None:
            return "Underflow"
        return self.start.data
    
    def display(self):
        temp=self.start
        while temp:
            print(temp.data, end="->")
            temp=temp.next
        print("None")

q=Queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.display()
print(q.pop())
print(q.pop())
print(q.pop())