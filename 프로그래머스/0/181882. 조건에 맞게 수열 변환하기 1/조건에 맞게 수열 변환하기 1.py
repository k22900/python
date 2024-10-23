# arr[i]>=50 and arr[i]%2==0 = arr[i]/=2
# arr[i]<50 and arr[i]%2==1 = arr[i]*=2

def solution(arr):
    answer = []
    for val in arr:
        if val >= 50 and val % 2 == 0:
            answer.append(val / 2)
        elif val < 50 and val % 2 == 1: 
            answer.append(val * 2) 
        else:
            answer.append(val)
    return answer