# 2홀수
# 일의자리 5아닐것
# 3으로 나누어 떨어지지 않으면서 9로는 나누어 떨어지는수?

# 파라미터=정수
# 리턴=불

def isPerfactNum(n):
    if n%2==0:
        return False
    if n%10==5:
        return False
    if n%3==0 and n%9!=0:
        return False
    return True


n=int(input())

if isPerfactNum(n):
    print(f"{n}은 온전수이다.")
else:
    print(f"{n}은 온전수가 아니다.")

