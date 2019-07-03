class Stack:

    def __init__(self):
        self.stack=[]

    def push(self,value):
        if value not in self.stack:
            self.stack.append(value)
            print("item added is", value)
            return True
        else:
            return False

    def peek(self):
        return self.stack[0]

    def pop(self):
        if len(self.stack)>0:
            return self.stack.pop()

AStack = Stack()
AStack.push("Mon")
AStack.push("Tue")
print(AStack.pop())
AStack.push("Wed")
AStack.push("Thu")
print(AStack.pop())