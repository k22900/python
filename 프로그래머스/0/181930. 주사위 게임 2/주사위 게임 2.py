def solution(a, b, c):
    answer = 0
    res=0
    num=len(list({a,b,c}))
    if num == 3: 
        res=(a+b+c)
    elif num==1: 
        res=(a*3)*((a**2)*3)*((a**3)*3)
    elif num==2:
        res=((a+b+c)*((a**2)+(b**2)+(c**2)))
    answer=res
    return answer