# 나누어주고 남는사과 개수를 출력하는 문제
# 남는사과의 개수는 최소화
# 학교마다 사과의 개수와 학생수는 다르다
num=int(input())#num=3
spareApple=0
for i in range(num):
    studentNum,appleNum=map(int,input().split())
    number=appleNum%studentNum
    spareApple+=number
print(spareApple)