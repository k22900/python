import heapq

n=int(input())

nList=[]
minHeap=[]
for _ in range(n):
    temp=int(input())
    if temp==0:
        if len(minHeap)==0:
            print(0)
        else:
            res=heapq.heappop(minHeap)
            print(res)
            nList.append(res)
            
        continue
    else:
        heapq.heappush(minHeap,temp)
print(res)