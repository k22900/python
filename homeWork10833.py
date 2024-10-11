# 모두 똑같이 나누어준다
# 남는 사과수는 최소한으로
# 서로 다른 학교일때는 학생이 받는 사과 개수는 다를 수 있다.
schoolNum=int(input())
leftoverApples=0
for _ in range(schoolNum):
    appleNum,numberStudents=map(int,input().split())
    res=numberStudents%appleNum
    leftoverApples+=res
print(leftoverApples)