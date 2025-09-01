def solution(a, b, c):
    answer = 0
    res=0
    num=len(list({a,b,c}))#중복제거 후 배열로 형변환 후 그배열의 길이 를 num에 저장(초기화)
    if num == 3: # 길이의 값이 3(중복X)인가?
        res=(a+b+c)
    elif num==1: #길이의 값이 1(전부 같은값)인가?
        res=(a*3)*((a**2)*3)*((a**3)*3)
    elif num==2:#길이의 값이 2(2개 중복)인가?
        res=((a+b+c)*((a**2)+(b**2)+(c**2)))
    answer=res
    return answer
print(solution(4,4,4))
# 473