#merge two linked list at alternate position
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def insertbeg(self,item):
        newNode=Node(item)
        newNode.next=self.head
        self.head=newNode

    def mergeList(self,q):
        p_current=self.head
        q_current=q.head
        while p_current!=None and q_current!=None:
            p_next=p_current.next
            q_next=q_current.next

            p_current.next = q_current
            q_current.next=p_next


            p_current=p_next
            q_current=q_next
        #q.head=q_current

    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data,end="=>")
            temp=temp.next
        print("Null")

llist1=LinkedList()
llist2=LinkedList()
llist1.insertbeg(5)
llist1.insertbeg(4)
llist1.insertbeg(3)
llist1.insertbeg(2)
llist1.insertbeg(1)
llist1.printlist()

llist2.insertbeg(6)
llist2.insertbeg(7)
llist2.insertbeg(8)
llist2.insertbeg(9)

llist2.printlist()
llist1.mergeList(llist2)
llist1.printlist()



