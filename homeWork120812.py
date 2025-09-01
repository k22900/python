from collections import Counter

def solution(array):
    answer = 0
    arrCnt=0
    arrCnt=Counter(array)
    arrCntVal=list(Counter.values(arrCnt))
    arrCntKey=list(Counter.keys(arrCnt))
    # print(arrCntVal,arrCntKey)
    if len(arrCntVal) > 1:
        numCnt=Counter(arrCntVal)
        # maxNum=max(arrCntVal)
        sortedVal=sorted(arrCntVal,reverse=True)
        # print(sortedVal)
        # print(arrCntVal,arrCntKey)
        # print(maxNum)
        firstBigNum=sortedVal[0]
        secondBigNum=sortedVal[1]
        # print(firstBigNum,secondBigNum)
        if firstBigNum == secondBigNum:
            res = -1 
        else:
             res = arrCntKey[arrCntVal.index(firstBigNum)]
    elif len(arrCntVal)== 1:
        res= arrCntKey[0]
    return res


print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2]))
print(solution([1]))
print(solution([1,1,2,3])) 
print(solution([1]))
print(solution([1]))
