class stack:
    top=-1
    def __init__(self):
        self.stack=[None]*10

    def push(self,item):
        #top=-1
        if item not in self.stack:
            if self.top==11:
                print("stack overflow")
            else:
                self.top+=1
                self.stack[self.top]=item
        #return self.stack
    def pop(self):
        #top=len(self.stack)
        if self.top==-1:
            print("Underflow")
        else:
            s=self.stack.pop(self.top)
            print(s)
            self.top-=1
        #return self.stack
s=stack()
s.push(10)
s.push(11)
s.push(12)
s.push(16)
s.pop()
print(s.stack[:s.top+1])