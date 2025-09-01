def solution(a, b): #5월 24일
    mon=[31,29,31,30,31,30,31,31,30,31,30,31]
    week=["FRI","SAT","SUN","MON","TUE","WED","THU"]
    num=0
    cnt=0
    while True:
        if cnt==a-1:
            break
        num+=mon[cnt]
        cnt+=1
    num+=b
    num=num%7
    
    answer = week[num-1]
    return answer
#1:31 2:29 3:31 4:30 5:31 6:30 7:31 8:31 9:30 10:31 11:30 12:31
print(solution(5,24))