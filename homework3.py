def solution(n):
    answer = [[0]*n for _ in range(n)]
    currentX,currentY=0,0
    Move_X_List=[1,0,-1,0]
    Move_Y_List=[0,1,0,-1]
    cnt=1
    turnCnt=0
    while cnt <= n*n:
        answer[currentY][currentX]=cnt
        nextX=currentX+Move_X_List[turnCnt%4]
        nextY=currentY+Move_Y_List[turnCnt%4]
        cnt+=1
        if 0<= nextX < n and 0<= nextY <n and 0==answer[nextY][nextX]: #1번항목:X의 범위 감지 2번항목:Y의 범위 감지 3번항목:다음 위치가 0인가
            currentX=nextX
            currentY=nextY
        else:
            turnCnt+=1
            currentX=currentX+Move_X_List[turnCnt%4]
            currentY=currentY+Move_Y_List[turnCnt%4]
    return answer
print(solution(5))