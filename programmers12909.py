from collections import deque



def solution(s):
    answer = True
    sheet=deque()    
    for v in s:
        if len(sheet) != 0:#sheet가 비었는가?
            if ")" == v:#)값이 ")"인가?
                if sheet[-1] == "(":#sheet의 마지막 값이 "("이여서 패어가 되는가? 
                    sheet.pop()
                else:
                    sheet.append(v)
            else:
                sheet.append(v)
        else:
            sheet.append(v)
        # print(sheet)  
    if len(sheet) == 0:#sheet의 값이 전부 패어 처리되어 비었는가?
        answer = True 
    else:
        answer = False
    return answer

s="(()("

print(solution(s))