def solution(arr, k):
    answer = []
    if k%2==0:#k가 짝수인가?
        for val in arr:
            res=val+k
            answer.append(res)
    elif k%2==1:#k가 홀수인가?
        for val in arr:
            res=val*k
            answer.append(res)
    return answer
print(solution([1, 2, 3, 100, 99, 98],3))