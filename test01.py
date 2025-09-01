def find(x,y,P):
    # 1의 개수확인
    cnt=0
    for i in range(y-2,y+1):
        for j in range(x-2,x+1):
            n=P[i][j]
            
            if n==1:
                cnt+=1
    # print(cnt)
    return cnt
def coin(N,P):
    # 시작점=[2,2],범위지정>탐색
    num=0
    for y in range(2,N):
        for x in range(2,N):
            res=find(x,y,P)
            if num<res:
                num=res
            
    
    
    return num

N=int(input())
coinList=[0]*N
for i in range(N):
    coinList[i]=list(map(int,input().split()))
print(coinList)

print(coin(N,coinList))
# [1,1,1,0,1],
# [0,0,1,1,0],
# [0,1,1,0,0],
# [1,1,1,0,1],
# [0,0,1,1,0]
# coinList=[[1,1,1,0,1],[0,0,1,1,0],[0,1,1,0,0],[1,1,1,0,1],[0,0,1,1,0]]