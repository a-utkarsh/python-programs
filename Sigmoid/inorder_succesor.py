class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def minvalue(node):
    current=node
    while current is not None:
        if current.left==None:
            break
        current=current.left
    return current.data


def inorderSuccesor(root,n):
    if n.right is not None:
        return minvalue(n.right)
    succ=None
    while root!=None:
        if n.data<root.data:
            succ=root
            root=root.left
        elif(n.data>root.data):
            root=root.right
        else:
            break
    return succ
root=Node(20)
root.left=Node(8)
root.left.left=Node(4)
root.left.right=Node(12)
root.left.rig.ht.left=Node(10)
root.left.right.right=Node(14)
root.right=Node(22)
temp=root.right
print(inorderSuccesor(root,temp))


