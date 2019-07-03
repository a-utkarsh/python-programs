class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    cnt=0
    def __init__(self):
        self.head=None


    def insertBeg(self,item):
        newNode=Node(item)
        newNode.next=self.head
        self.head=newNode

    def length(self):
        temp=self.head
        while temp:
            self.cnt = self.cnt + 1
            temp=temp.next
        return  self.cnt

    #by calculating length
    def middle(self):
        mid=self.length()//2

        count=0
        temp=self.head
        while count!=mid:
            temp=temp.next
            count+=1

        return temp.data
    #Using sloww pointer and fast pointer
    def middle2(self):
        slow_p=self.head
        fast_p=self.head
        while slow_p and fast_p and fast_p.next:
            slow_p=slow_p.next
            fast_p=fast_p.next.next
        return slow_p.data
    #delete middle element in linked list
    def printllist(self):
        temp=self.head
        while temp:
            print(temp.data,end="=>")
            temp=temp.next
        print("Null")


llist=LinkedList()

llist.insertBeg(5)
llist.insertBeg(4)
llist.insertBeg(3)
llist.insertBeg(2)
llist.insertBeg(1)
llist.printllist()

print(llist.middle())
print(llist.middle2())


