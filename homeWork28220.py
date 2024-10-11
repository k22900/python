# def deduplicator(numList,max,min):
#     duplicateCount=0
#     while True:
#         cnt=0
#         for i in numList:
#             if i<min or i>max:
#                 numList.remove(i)
#                 cnt+=1
#                 duplicateCount+=1
#         if cnt==0:
#             break
#     return duplicateCount


# # 쌓는탑 높이=N
# # 현재 높이의 칸수=i
# # 각 칸에 최대 불록 개수=R
# # 각 칸에 최소 블록 개수=L
# # 각층의 블록개수값=A
# # 조건1: 각층의 쌓인 블럭개수=L<=A<=R
# # 조건2: 각층의 블록은 단조증가 한다
# N,L,R=map(int,input().split())
# A=list(map(int,input().split()))
# cnt=0
# changeCount=0

        
# # print(A)
# if len(A)!=0:
#     while True:
#         for i in range(1,len(A)):
#             temp=A[i-1]
#             if A[i]>temp:#A[1]>A[0]
                
#                 A[i-1]=A[i]
#                 A[i]=temp
#                 cnt+=1
#                 changeCount+=1
#         if changeCount==0:
#             break
#         else:
#             changeCount=0
#     temp=deduplicator(A,R,L)
#     cnt+=temp
# else:
#     cnt=-1
    
# print(cnt,A)
N,L,R=map(int,input().split())
numsList=list(map(int,input().split()))

cnt=0
while True:
    tempCnt=0
    for i in range(1,N):
        val=numsList[i]
        if val > val-1:
            numsList[i]=numsList[i-1]
            numsList[i-1]=val
            tempCnt+=1
            cnt+=1
    print(numsList)
    if tempCnt==0:
        break
    

print(cnt)