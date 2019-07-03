# Segregate odd and even in a linkedList
'''
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

    def segregate(self):
        startEven=None
        endEven=None
        startOdd=None
        endOdd=None
        currNode=self.head

        while currNode!=None:
            if currNode.data%2==0:
                if startEven==None:
                    startEven=currNode
                    endEven=startEven
                else:
                    endEven.next=currNode
                    endEven=endEven.next
            else:
                if startOdd==None:
                    startOdd=currNode
                    endOdd=startOdd
                else:
                    endOdd.next=currNode
                    endOdd=endOdd.next
            currNode=currNode.next
        if startEven is None or startOdd is None:
            return

        endOdd.next=startEven
        endEven.next=None
        self.head=startOdd

    def printLinkedList(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("Null")

llist=LinkedList()
llist.insertBeg(10)
llist.insertBeg(9)
llist.insertBeg(8)
llist.insertBeg(7)
llist.insertBeg(6)
llist.insertBeg(5)
llist.insertBeg(4)
llist.insertBeg(3)
llist.insertBeg(2)
llist.insertBeg(1)
print("Before Rearrange")
llist.printLinkedList()
print("After rearrange")
llist.segregate()
llist.printLinkedList()

#Longest Common Ancestor
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def findpath(root,path,k):
    if root is None:
        return False

    path.append(root.data)

    if root.data==k:
        return True

    if(root.left!=None and findpath(root.left,path,k)) or (root.right!=None and findpath(root.right,path,k)):
        return path

    path.pop()
    return False

def LCA(root,n1,n2):
    path1=[]
    path2=[]

    if findpath(root,path1,n1) is None or findpath(root,path2,n2) is None:
        return -1
    else:
        i=0
        while i<len(path1) and i<len(path2):
            if(path1[i]!=path2[i]):
                break
            i+=1
        return path2[i-1]

root=Node(1)
root.left=Node(2)
root.left.left=Node(4)
root.left.right=Node(5)
root.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(7)

print(LCA(root,4,6))



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def findPath(root, path, k):
    if root is None:
        return False

    path.append(root.data)
    if root.data == k:
        return True

    if (root.left is not None and findPath(root.left, path, k)) or (root.right is not None and findPath(root.right, path, k)):
        return path
    path.pop()
    return False


def LCA(root, n1, n2):
    path1 = []
    path2 = []

    if (not findPath(root, path1, n1) and findPath(root, path2, n2)):
        return -1
    else:
        i = 0
        while i < len(path1) and i < len(path2):
            if (path1[i] != path2[i]):
                break
            i += 1
        print(path1,path2)
        return path1[i - 1]


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(LCA(root, 4, 5))

#Dijkstra
class Graph:
    def __init__(self,vertex):
        self.V=vertex
        self.graph=[[0 for i in range(vertex)] for j in range(vertex)]

    def minDistance(self,dist,sptset):
        import math
        min_d=math.inf
        min_index=-1
        for v in range(self.V):
            if dist[v]<min_d and sptset[v]==False:
                min_d=dist[v]
                min_index=v
        return min_index

    def dijkstra(self,src):
        import math
        dist=[math.inf]*self.V
        dist[src]=0
        sptset=[False]*self.V

        for count in range(self.V):
            u = self.minDistance(dist, sptset)
            sptset[u] = True
            for v in range(self.V):
                if self.graph[u][v]>0 and sptset[v]==False and dist[v]>self.graph[u][v]+dist[u]:
                    dist[v]=self.graph[u][v]+dist[u]

        return dist


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]
print(g.dijkstra(0))

from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def BFS(self,s):
        visited=[False]*len(self.graph)
        queue=[]
        queue.append(s)
        visited[s]=True
        while queue:
            s=queue.pop(0)
            print(s)
            for i in self.graph:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True

g=Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
g.BFS(2)

from collections import  defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFSutil(self,v,visited):
        visited[v]=True
        print(v)
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSutil(i,visited)
    def DFS(self,v):
        visited=[False]*len(self.graph)
        self.DFSutil(v,visited)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.DFS(2)
class Trie:
    class Node:
        def __init__(self,c):
            self.char=c
            self.cnt=0
            self.children=[]
    def __init__(self):
        self.root=self.Node("*")
    def addWord(self,word):
        T=self.root
        for c in word:
            for child in T.children:
                if child.char==c:
                    break
            else:
                child=self.Node(c)
                T.children.append(child)
            T=child
            T.cnt+=1
    def searchWord(self,word):
        T=self.root
        for i, c in enumerate(word):
            for child in T.children:
                if child.char==c:
                    T=child
                    break
            if T.cnt==1:
                return word[:i+1]
        return word

    def prefix(self,arr):
        #T=self.root
        for word in arr:
            self.addWord(word)
        res=[]
        for word in arr:
            pref=self.searchWord(word)
            res.append(pref)

        return res
arr1=["zebra","dog","duck","dove"]
T=Trie()
print(T.prefix(arr1))
'''