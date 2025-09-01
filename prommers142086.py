def solution(s):
    answer = []
    search={}#단어의 직전 출현 인덱스 저장
    cnt=0#인덱스 대체
    for w in s:#문자열 s 를 순환해 단어를 때오고
        idx=search.get(w,-1)#전에 단어가 나온적있는지 확인하고
        if idx == -1:#있으면 -1을 넣고
            answer.append(-1)
            
        else:#아니면 현제 인덱스값과 전에 나왔던 인덱스 확인후 위치 비교
            n=cnt-idx
            answer.append(n)
        search[w]=cnt#나타난 위치 최신화하고
        cnt+=1    #수동으로 인덱스올리고
    return answer

s="banana"
print(solution(s))