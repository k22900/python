#Hidx=논문n편중 인용횟수h번이상인 논문의 개수는?
#어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.
# h번 이상 인용된 논문의 개수>=h
# 주어지는것 citations라는 각논문의 인용 횟수를 담은 배열
# h의 기준은? citations의 0번인덱스 값?False 0, citations의 길이중간 올림한것?False, citations의 내부 값의 평균값? False 0,citations의 길이중간 반올림한것?
import math
def solution(citations:list):
    citationsLen=len(citations)/2
    num=round(citationsLen)
    
    citations.sort()
    baseValue= citations[num]
    idx=citations.index(baseValue)
    # for v in citations:
    #     if v>=baseValue:
    #         idx=citations.index(v)
    #         break
    res=citations[idx:]
    
    answer = len(res)
    return answer

citations=[3, 0, 6, 1, 5]
print(solution(citations))