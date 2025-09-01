# 3 2
# 5 2 4 
# 1 2 3  
# 5 3 4 
def row_chack(num,N,m):#행 확인
    number=num[0]
    cnt=0
    for n in num:
        
        if n==number:
            cnt+=1
        else:
            number=n
            cnt=1
        if cnt>=m:
            return True
            
    return False

def column_chack(li,N,m,x):#열 확인
    num=li[0][x]
    cnt=0
    for y in range(N):
        n=li[y][x]
        if n==num:
            cnt+=1
        else:
            num=n
            cnt=1
        if cnt>=m:
            return True
        
    return False

# N,M=3,2
N,M=map(int,input().split())
grid=[0]*N
for i in range(N):
    grid[i]=list(map(int,input().split()))
# grid=[[1,2,2],[1,3,4],[1,2,3]]

sqrCnt=0
sqrCnt1=0
for I in range(N):
    li=grid[I]
    if row_chack(li,N,M):
        sqrCnt+=1
    if column_chack(grid,N,M,I):
        sqrCnt+=1
print(sqrCnt)
# print(sqrCnt1)
    