# 첫글자=X
# 문자열s를 왼쪽부터 오른쪽으로 읽으면서 x랑 같은거랑 다른거랑 개수가 같아질때 분리후 종료후 다시시작(조건1)
# 만약 두횟수가 다른상태어서 s의 글자가 없다면 문자열 분리후 종료(조건2)
def solution(s):
    answer = 0
    
    sCnt=0
    oCnt=0
    
    x=None
    for w in s:
        if x is None:
            x=w
            sCnt+=1
        else:
            if x==w:
                sCnt+=1
            else:
                oCnt+=1
        if sCnt==oCnt:
            x=None
            answer+=1
            sCnt=oCnt=0
    if x is None:
        return answer
    else:
        answer+=1
        return answer

s="aaabbaccccabba"
print(solution(s))