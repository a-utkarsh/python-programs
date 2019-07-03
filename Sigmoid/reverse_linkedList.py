class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def insertBeg(self,key):
        newNode=Node(key)
        newNode.next=self.head
        self.head=newNode

    def reverse(self):
        prev=None
        curr=self.head
        while(curr!=None):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data,end="=>")
            temp = temp.next
        print("Null")

llist = LinkedList()
llist.insertBeg(20)
llist.insertBeg(4)
llist.insertBeg(15)
llist.insertBeg(85)

print("Given Linked List")
llist.printList()
llist.reverse()
print("\nReversed Linked List")
llist.printList()
