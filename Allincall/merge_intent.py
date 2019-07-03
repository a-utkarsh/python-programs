import heapq
n = int(input())
arr = list(map(int,input().split()))
cost,res=0,0
heapq.heapify(arr)
for i in range(1,len(arr)):
    cost = heapq.heappop(arr) + heapq.heappop(arr) - 1
    heapq.heappush(arr, cost+1)
    res += cost
print(res)