class Node:
    linknode=None
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
    #Usiing Hashing
    def intersection(self,head1,head2):
        s=[]
        temp1=head1
        while temp1:
            s.append(temp1)
            temp1=temp1.next
        temp2=head2
        while(temp2):
            if temp2 in s:
                #self.linknode=temp2.data
                return temp2.data
            temp2=temp2.next
        return False
    #Using length and without using extra space
    def intersectLen(self,head1,head2):
        headA=head1
        headB=head2
        len1=0
        len2=0
        while head1:
            head1=head1.next
            len1+=1
        while head2:
            head2=head2.next
            len2+=1
        diff=abs(len1-len2)
        head1=headA
        head2=headB
        if len1>len2:
            for i in range(diff):
                head1=head1.next
        else:
            for i in range(diff):
                head2=head2.next
        for i in range(min(len1,len2)):
            if head1 is head2:
                return head1.data
            head1=head1.next
            head2=head2.next
        return None







    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data,end="=>")
            temp=temp.next
        print("Null")
firstList = LinkedList()
firstList.insertBeg(5)
firstList.insertBeg(4)
firstList.insertBeg(3)
firstList.insertBeg(2)
firstList.insertBeg(1)

secList = LinkedList()
secList.insertBeg(10)

temp = secList.head.next
secList.head.next = firstList.head.next.next.next

print("First List:")
firstList.printlist()
print("\nSecond List:")
secList.printlist()

if firstList.intersection(firstList.head,secList.head):
    print("\nMerge Point is ",firstList.intersection(firstList.head,secList.head))
else:
    print("\nNo Intersection node")
print(firstList.intersectLen(firstList.head,secList.head))
