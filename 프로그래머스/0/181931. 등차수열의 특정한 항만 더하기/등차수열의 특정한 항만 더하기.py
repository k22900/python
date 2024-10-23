def solution(a, d, included):
    answer = 0
    res = 0
    resultArr = []
    for i in range(len(included)):
        res = a+(i*d)
        if included[i] == True: resultArr.append(res)
    answer = sum(resultArr)
    return answer