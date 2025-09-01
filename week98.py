#목표: 주어진 수 전부사용해 목표값제작
# 숫자위치 변경X,+,-만 으로 목표값 제작
def backTracking(idx,target):
    global answer
    if idx>=l:#인덱스랑 크기 같나?
        if target==sum(stack):#목표값인가?#True
            answer += 1
        return
    for i in range(2):#False
        stack.append(grid[idx][i])
        backTracking(idx+1,target)
        stack.pop()

def solution(numbers,target):
    global l,grid,stack,answer
    answer=0
    l=len(numbers)
    grid=[[0,0] for _ in range(l)]#[[0,0][0,0][0,0][0,0]]
    for i, n in enumerate(numbers):
        grid[i][0]=n #[[1,0][4,0][2,0][3,0]]
        grid[i][1]= -1 * n #[[1,-1][4,-4][2,-2][3,-3]]
    stack=[]
    backTracking(0,target)
    return answer

if __name__=="__main__":
    numbers=list(map(int,input().split()))
    target=int(input())
    answer=solution(numbers,target)#start
    print(answer)
        
