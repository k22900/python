import heapq
N,K=map(int,input().split(" "))
A=list(map(int,input().split()))

minHeap=[]

# for i in A:
#     heapq.heappush(minHeap,i)

# for _ in range(K-1):
#     heapq.heappop(minHeap)
# print(heapq.heappop(minHeap))
A.sort()
print(A[K-1])