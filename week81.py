def solution(arr):
    answer = 0
    cnt=0
    while True:
        before=[v for v in arr]
        for idx,val in enumerate(arr):
            if val >= 50 and val % 2 == 0:
                arr[idx]=val // 2
            elif val < 50 and val % 2 == 1:
                arr[idx]=(val * 2)+1
        if before == arr:
            break
        cnt+=1
    answer=cnt  
    return answer
print(solution([1, 2, 3, 100, 99, 98]))