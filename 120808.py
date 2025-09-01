from math import lcm
def solution(numer1, denom1, numer2, denom2):
    answer = [0,0]
    denoms=[denom1,denom2]
    numers=[numer1,numer2]
    minMultiple=lcm(denom1,denom2)
    if denom1==minMultiple:
        temp=minMultiple//denom2
        numers[1]*=temp#numers[1]=numer2이다
    elif denom2==minMultiple:
        temp=minMultiple//denom1
        numers[0]*=temp#numers[0]=numer1이다
    else:
        for i in range(2):
            numberGap=minMultiple//denoms[i]
            numers[i]*=numberGap
    answer[0],answer[1]=sum(numers),minMultiple
    if answer[0]%answer[1]==0:
        temp=answer[0]//answer[1]
        answer[1]=answer[1]//answer[0]
        answer[0]=temp
    if answer[1]==0:
        answer[1]=1        
        
    return answer
numer1,denom1,numer2,denom2=999,999,999,999
print(solution(numer1,denom1,numer2,denom2))