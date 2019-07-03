
class Graph:
    def __init__(self,vertex):
        self.V=vertex
        self.graph=[[0 for row in range(vertex)]for column in range(vertex)]

    def printSolution(self,dist):
        print("Vertex    distance from source")
        for node in range(self.V):
            print(node, "\t\t\t", dist[node])

    def minDistance(self,dist,sptset):
        import math
        min=math.inf
        min_index=-1
        for v  in range(self.V):
            if dist[v]<min and sptset[v]==False:
                min=dist[v]
                min_index=v
        return min_index

    def dijkstra(self,src):
        import math
        dist=[math.inf]*self.V
        dist[src]=0
        sptset=[False]*self.V

        for i in range(self.V):
            u=self.minDistance(dist,sptset)
            sptset[u]=True

            for v in range(self.V):
                if self.graph[u][v] > 0 and sptset[v]==False and dist[v]>dist[u]+self.graph[u][v]:
                    dist[v]=dist[u]+self.graph[u][v]
        self.printSolution(dist)
g=Graph(9)
g.graph=[[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
          ]
g.dijkstra(0)



