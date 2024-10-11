import itertools
import math
import sys
input=sys.stdin.readline

# listMaximums=값들의 합을 저장하기 위한 배열
# sumValue=값을 합하고 조건 검증하기 전에 잠시저장을 위한 변수
# v=value의 약어 

def findMaxSum(valueList,limit):
    listMaximums=[]
    for v in valueList:
        sumValue=sum(v)
        if sumValue<=limit:
            listMaximums.append(sumValue)
    return max(listMaximums)


# maxLimit=게임에서 카드로 만들수있는 최대의 수
# N=게임에서 주어질 카드의 "장"수
# cardNums=카드들의 숫자값
# sumList=합할수있는 경우를 담는다
# findMaxSum=카드의 합의 최대를 구하기위한 함수이다
# res=최종값을 저장한다

# 조건1: 카드의 합은 3장의 합으로 만든다 
# 조건2: 카드의 합<= maxLimit

N,maxLimit=map(int,input().split())
cardNums=list(map(int,input().split()))
# print(cardNums)
sumList=itertools.combinations(cardNums,3)


res=findMaxSum(sumList,maxLimit)
print(res)