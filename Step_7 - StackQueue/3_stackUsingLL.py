class Node:
    def __init__(self, data=0, next=None):
        self.data=data
        self.next=next

class Stack:
    def __init__(self):
        self.top=None
    
    def push(self, data):
        newNode=Node(data)
        newNode.next=self.top
        self.top=newNode
    
    def pop(self):
        if self.top is None:
            return "Underflow"
        poppedData=self.top.data
        self.top=self.top.next
        return poppedData
    
    def peek(self):
        if self.top is None:
            return "Underflow"
        return self.top.data
    
    def display(self):
        temp=self.top
        while temp:
            print(temp.data, end="->")
            temp=temp.next
        print("None")
        
stack = Stack()
stack.push(5)
stack.push(15)
stack.push(25)
stack.display()         
print("Top:", stack.peek()) 
print("Popped:", stack.pop())  