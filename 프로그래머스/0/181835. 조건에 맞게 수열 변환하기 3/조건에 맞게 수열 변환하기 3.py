def solution(arr, k):
    answer = []
    if k%2==0:
        for val in arr:
            res=val+k
            answer.append(res)
    elif k%2==1:
        for val in arr:
            res=val*k
            answer.append(res)
    return answer