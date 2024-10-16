def solution(num_list):
    answer = num_list
    listLen=len(num_list)
    if num_list[listLen-1]>num_list[listLen-2]:#num_list의 마지막 값보다 그전값이 더 작은가
        res=num_list[listLen-1]-num_list[listLen-2]#True라면 마지막값에서 그전 값을 빼준다

    else:
        res=num_list[listLen-1]*2#False라면 마지막 값의 2배 값을 계산한다

    answer.append(res)
    return answer