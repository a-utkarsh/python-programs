'''
Create a balanced binary search tree from a sorted array
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def bbst(array):
    if len(array)==0:
        return None
    mid= len(array)//2
    root=Node(array[mid])
    root.left=(bbst(array[:mid]))
    root.right=(bbst(array[mid+1:]))
    return root

def preorder(node):
    if not  node:
        return None
    print(node.data)
    preorder(node.left)
    preorder(node.right)
arr = [1, 2, 3, 4, 5, 6, 7]
root = bbst(arr)
print ("PreOrder Traversal of constructed BST ")
preorder(root)