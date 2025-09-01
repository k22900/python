import random
import heapq

# 여기서 k 번째 수를 찾아줘 , 최소 힙을 이용해서..
k=int(input())
minHeap = []
for _ in range(8000000000):
    heapq.heappush(minHeap,random.randint(0, 5000000))
# print(minHeap)
for _ in range(k-1):
    heapq.heappop(minHeap)
print(heapq.heappop(minHeap))
# print()