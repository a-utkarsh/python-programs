'''
Python3 program to rearrange a linked list in such a way that all odd positioned node are stored before all even positioned nodes
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:

    def __init__(self):
        self.head=None

    def insertAtBeg(self,key):
        newNode=Node(key)
        newNode.next=self.head
        self.head=newNode

    def rearrangeEvenOdd(self):

        #Corner Cases
        if(self.head==None or self.head.next==None ):
            return

        odd=self.head
        even=self.head.next
        evenFirst= even

        while(odd.next.next and even.next.next) is not None:
                odd.next=even.next
                odd=even.next
                even.next=odd.next
                even=odd.next

        if odd.next.next is not None:
            odd.next=even.next
            odd=even.next
            even.next=None

        odd.next=evenFirst
        return

    def printList(self):
        temp=self.head
        while temp:
            print(temp.data,end="")
            print("->", end="")
            temp=temp.next
        print("Null")
llist = LinkedList()

llist.insertAtBeg(7)
llist.insertAtBeg(6)
llist.insertAtBeg(5)
llist.insertAtBeg(4)
llist.insertAtBeg(3)
llist.insertAtBeg(2)
llist.insertAtBeg(1)
print("Before Rearrange")
llist.printList()
llist.rearrangeEvenOdd()
print("After Rearrange")
llist.printList()

