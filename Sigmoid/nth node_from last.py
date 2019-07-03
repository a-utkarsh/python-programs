class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def insertBeg(self,item):
        newNode=Node(item)
        newNode.next=self.head
        self.head=newNode

    def nthNode(self,n):
        refrence_p=self.head
        main_p=self.head
        count=0
        while count<n:
            if (refrence_p is None):
                print("%d is greater than the no. pf nodes in list" % (n))
                return
            refrence_p=refrence_p.next
            count+=1

        while refrence_p!=None:
            main_p=main_p.next
            refrence_p=refrence_p.next
        return main_p.data

    def printllist(self):
        temp = self.head
        while temp:
            print(temp.data, end="=>")
            temp = temp.next
        print("Null")
llist=LinkedList()
llist.insertBeg(5)
llist.insertBeg(4)
llist.insertBeg(3)
llist.insertBeg(2)
llist.insertBeg(1)
llist.printllist()
print(llist.nthNode(10))
