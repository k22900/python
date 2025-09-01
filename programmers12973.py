def solution(s):
    answer = -1
    sheet=[]
    for v in s:
        if len(sheet) != 0:#sheet가 비었지 않은가?
            if sheet[-1] == v:#sheet의 마지막 인덱스와 값이 같은가 
                sheet.pop()
            else:#아니면 패어 처리가 아니므로 v값추가
                sheet.append(v)
        else:#아니면 비었으므로 v값추가
            sheet.append(v)
        # print(sheet)
    if len(sheet) == 0:   #전부 패어처리 되었는가?
        answer = 1
    else:#패어처리가 되지않았으면 0
        answer=0

    return answer

s="baabaa"

print(solution(s))