class Node:
    #Constructor to create a new node
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

result = []
def printPathRec(root, path, pathlen):

    if root is None:
        return

    if(len(path)>pathlen):
        path[pathlen]=root.data

    else:
        path.append(root.data)
    pathlen+=1

    if root.left is None and root.right is None:
        list1=path[:]
        result.append(list1)

    else:
        printPathRec(root.left,path,pathlen)
        printPathRec(root.right,path,pathlen)
    return result

root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(2)
print(printPathRec(root,[],0))



