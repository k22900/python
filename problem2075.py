import heapq
import random

n=int(input())
numList=[]
maxheap=[]
nList=[]

for _ in range(n):
    row = [random.randint(-10**9, 10**9) for _ in range(n)]
    
    for num in row:
        heapq.heappush(maxheap,num*-1)
# print(maxheap)
for _ in range(n-1):
    res=heapq.heappop(maxheap)
    nList.append(res)
print(nList)
print(len(nList))
print(len(row))
print(len(maxheap))
print(-1*heapq.heappop(maxheap))
