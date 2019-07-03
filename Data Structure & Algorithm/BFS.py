from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addEdg(self,u,v):
        self.graph[u].append(v)

    def BFS(self,s):
        visited=[False]*(len(self.graph))
        queue=[]
        queue.append(s)
        visited[s]=True

        while queue:
            s=queue.pop(0)
            print(s)
            for i in self.graph[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True
g=Graph()
g.addEdg(0,1)
g.addEdg(0,2)
g.addEdg(1,2)
g.addEdg(2,0)
g.addEdg(2,3)
g.addEdg(3,3)
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.BFS(2)
