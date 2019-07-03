class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stackLL:
    def __init__(self):
        self.head=None

    def push(self,item):
        if self.head is None:
            self.head=Node(item)

        else:
            newNode=Node(item)
            newNode.next=self.head
            self.head=newNode

    def pop(self):
        if self.head is None:
            return None
        else:
            popped=self.head.data
            self.head=self.head.next
            return popped
