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

    def detectLoop(self):
        s=[]
        temp=self.head
        while(temp):
            if temp in s:
                return True
            else:
                s.append(temp)
            temp=temp.next
        return False
llist=LinkedList()
llist.insertBeg(20)
llist.insertBeg(4)
llist.insertBeg(15)
llist.insertBeg(10)
#llist.head.next = llist.head
if( llist.detectLoop()):
    print ("Loop found")
else :
    print ("No Loop ")

#using Floyd's cycle-Finding algorithm
class LinkedList2:
    def __init__(self):
        self.head=None

    def insertBeg(self,key):
        newNode=Node(key)
        newNode.next=self.head
        self.head=newNode

    def detectLoop(self):
        slow_p=self.head
        fast_p=self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p=slow_p.next
            fast_p=fast_p.next.next
            if slow_p==fast_p:
                print("Loop Found")
                return

        print("Loop not found")

llist=LinkedList2()
llist.insertBeg(20)
llist.insertBeg(4)
llist.insertBeg(15)
llist.insertBeg(10)
llist.detectLoop()
