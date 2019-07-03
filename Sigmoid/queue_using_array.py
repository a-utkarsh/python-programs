class Queue:
    def __init__(self):
        self.capacity = 10
        self.queue=[None]*self.capacity
        self.rear=0
        self.front=0

    def enqueue(self,item):
        if(self.rear==self.capacity):
            print("queue is full")
            return
        else:
            self.queue[self.rear]=item
            self.rear+=1
    def dequeue(self):
        if(self.front==self.rear):
            print("queue is empty")
            return
        else:
            for i in range(self.rear-1):
                self.queue[i]=self.queue[i+1]
            #self.queue[self.rear-1]=None
            self.rear-=1
q=Queue()
q.enqueue(10)
q.enqueue(12)
q.enqueue(13)
q.enqueue(18)
print(q.queue[:q.rear])
q.dequeue()
q.enqueue(19)
q.dequeue()
print(q.queue[:q.rear])