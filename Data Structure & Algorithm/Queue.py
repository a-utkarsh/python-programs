class queue:
    def __init__(self, capacity):  #Capacity = total capacity of queue
        self.front = self.size=0   #size = actual length of queue
        self.rear =  capacity-1
        self.Q=  [None]*capacity
        self.capacity = capacity
    #Queue is full when size == capacity
    def isFull(self):
        if self.size ==self.capacity:
            return True
        else:
            return False
    #Queue is empty when size is 0

    def isEmpty(self):
        if self.size==0:
            return True
        else:
            return False
    # Function to add an item to the queue.

    def Enqueue(self,item):
        if self.isFull()==True:
            print("Queue is Full")
            return
        self.rear = (self.rear+1)%(self.capacity)
        self.Q[self.rear]= item
        self.size = self.size+1
        print("%s enqueued to queue" % str(item))

        # Function to remove an item from queue.
        # It changes front and size

    def DeQueue(self):
        if self.isEmpty():
            print("Empty")
            return

        print("%s dequeued from queue" % str(self.Q[self.front]))
        self.front = (self.front + 1) % (self.capacity)
        self.size = self.size - 1
        # Function to get front of queue

    def que_front(self):
        if self.isEmpty():
            print("Queue is empty")

        print("Front item is", self.Q[self.front])

        # Function to get rear of queue

    def que_rear(self):
        if self.isEmpty():
            print("Queue is empty")
        print("Rear item is", self.Q[self.rear])


# Driver Code
if __name__ == '__main__':
    queue = queue(30)
    queue.Enqueue(10)
    queue.Enqueue(20)
    queue.Enqueue(30)
    queue.Enqueue(40)
    queue.DeQueue()
    queue.que_front()
    queue.que_rear()
