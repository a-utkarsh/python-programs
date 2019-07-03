class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def getmindepth(root):

    if root is None:
        return
    if root.left is None and root.right is None:
        return 1

    if root.left==None:
        return getmindepth(root.right)+1

    if root.right==None:
        return  getmindepth(root.left)+1

    return min(getmindepth(root.left),getmindepth(root.right))+1
'''
root = Node(1)
root.left = Node(2)
root.left.left=Node(7)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)
root.right.left.left=Node(6)
'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(getmindepth(root))

#The The above method may end up with complete traversal of Binary Tree even when the topmost leaf is close to root.
#A Better Solution is to do Level Order Traversal.
# While doing traversal, returns depth of the first encountered leaf node. Below is implementation of this solution.

def minDepth(root):
    if root is None:
        return
    q=[]
    q.append({'node':root, 'depth':1})
    while len(q)>0:
        qItem=q.pop(0)
        #get details of the removed item
        node=qItem['node']
        depth=qItem['depth']

        if node.left is None or node.right is None:
            return depth
        if node.left is not None:
            q.append({'node':node.left,'depth':depth+1})
        if node.right is not None:
            q.append({'node':node.right, 'depth':depth+1})

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(minDepth(root))