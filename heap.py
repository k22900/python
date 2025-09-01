
# heap

# # k = int(input())

# # minHeap = []
# # # heapq 는 math 같은 도구
# # for _ in range(20):
# #     heapq.heappush(minHeap, random.randint(0, 999))


# # temp = minHeap.copy()

# # for _ in range(k-1):
# #     heapq.heappop(minHeap)  # 루트 뽑아내기

# # kMin = minHeap[0]
# # print(kMin)

# # temp.sort()
# # print(temp[k-1])
# # minHeap.add(random.randint(0, 999))


# # math.ceil(1.3)  # func  (모듈을 참조)
# # # math 모듈에 있는 ceil 을 쓰겠다.

# # a = list()
# # a.append()  # method (obj를 참조)
# # a 객체에 append 해라
# #
# s = [x for x in range(10, -11, -1)]
# # heapq.heappush(s, -1*33)
# # heapq.heappush(s, -1*43)
# # heapq.heappush(s, -1*2)

# print(s, end="\n")  # heapq : min-heap 전용

# heapq.heapify(s)
# print(s)  # heapq : min-heap 전용


# # root !! root min 가장 최소야,
# # res = -1*heapq.heappop(s)
# # print(res)

# # res = -1*heapq.heappop(s)
# # print(res)

# =====================================
# [n 번째 수 찾기]
# 1.  n-1 heap pop 한다.
# 2.  사이즈가 n 짜리인 heap 한다.


import heapq


n = int(input())

heap = []
for _ in range(n):
    line = list(map(int, input().split()))
    for num in line:
        if len(heap) < n:#n은 목표된 크기|heap의크기가 목표보다 작은가?
            heapq.heappush(heap, num)
            
        elif heap[0] < num:#heap[0](최소힙->루트)의 크기가 num(line의 다음)보다 큰가(True=루트값을 교환후 최소힙을 사용해 재 정렬?)
            heapq.heapreplace(heap, num)
            
        else:
            pass
        print(heap)


print(heap[0])

'''

# heapq -> min heap
# log(n) -> good

# n 으로 잡아놓고
'''
# n * n => max heap, pop 5 번
n = int(input())

max_heap = []
for _ in range(n):
    line = list(map(int, input().split()))
    for e in line:
        heapq.heappush(max_heap, -1 * e)

for _ in range(n-1):
    heapq.heappop(max_heap)

print(-1 * max_heap[0])


# =====================================
