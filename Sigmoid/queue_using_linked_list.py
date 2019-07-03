class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class QueueLL:
    def __init__(self):
        self.rear=self.front=None

    def enqueue(self,item):
        newNode=Node(item)
        if self.rear==None:
            self.front=self.rear=newNode
            return
        else:
            self.rear.next=newNode
            self.rear=newNode

    def dequeue(self):
        if self.front==None:
            print("queue is empty")
            return
        else:
            newNode=self.front
            self.front=newNode.next
        if self.front==None:
            self.rear=None
        return (str(newNode.data))
q = QueueLL()
q.enqueue(10)
q.enqueue(20)
q.dequeue()
q.dequeue()
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
print(q.dequeue())