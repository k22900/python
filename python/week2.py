# 변수 와 초기화

# 변수의 명(주소) = 값
a = 313 # 초기화
# 데이터 값을 네이밍

# 함수 ?
# 어떤기능을 네이밍.

# k : 매개변수(동전) -> [ 기능 ]/함수명(자판기) -> k*3 : 리턴값 (음료수)

# <선언부>
def mul3(num):
    # <구현부>
    # 함수의 기능을 자세히 적어줘 
    # 만들고 싶은것 어떤수를 받아서 3을 곱해줘 그것을 리턴해줘 
    return num * 3

def mul(num1,num2):
    # <구현부>
    # 함수의 기능을 자세히 적어줘 
    # 만들고 싶은것 어떤수를 받아서 3을 곱해줘 그것을 리턴해줘 
    ans = num1 * num2
    return ans
# var = mul(2,5)


print(3,4,end="\n",sep=" ")
print(3,4)

# \n ew line : 줄 바꿈 

# end="\n" : 옵션1 / print 함수에서 전체의 끝에 값을 설정하는 옵션 / Default : \n
# sep=" "  : 옵션2 / print 함수에서 매개변수간의 분리하는 옵션 / Default : 공백하나

# 함수 
# print(mul3(40)) # 매개변수가 1개

# 초기화 , 호출 을 헷갈리면 안돼!
# 변수 : 초기화
# 함수 : 선언 + 호출 

# 두개 같나?
# print(type(3))   # 자료형 int / # 매개변수가 1개
# print(type("3")) # 자료형 str / # 매개변수가 1개

# print(3,5) # 매개변수가 2개
# print(3,5,7) # 매개변수가 3개

# 3 5 7 
# 왜 따옴표가 안나왔지? 
# 왜 띄어써졌지?


