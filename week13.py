# 변수와 초기화 , 자료형
#
# 자료형
# 숫자, 문자 , 불(참,거짓)
# 숫자
#   정수(int) , 실수(float)
# 문자
#   문자열 (str)
#   문자  chr
#   ASCII / 비트들 가지고 어떻게 문자(영어 혹은 기호)로 변환할꺼니 에대한 규격\

##################################
# int 정수 int(13141.3145) -> 13141
# float 실수  float(333) -> 333.0
# str 문자열 str(333) -> "333"
# int 정수 int("333") -> 333
# int 정수 int("daare") -> daare3(X)
##################################

# print/출력 -> 다중출력과 출력관한 옵션들로 제어가가능
# input/입력 -> input,map(),split() 다중입력 과 단일입력 을 받았어
# 터미널 -> 코드 -> 터미널
#
# 논리 (로직)
# if,  else , elif
# 코드 블록 (인덴트 = 들여쓰기 ) 유효범위
# 인덴트 된 부분만 실행
# 조건 연산 (and , or , not)


# if condition:
    # codeEx
    # codeEx
    # codeEx
# codeEx

# if condition:
    # codeEx
    # codeEx
    # codeEx
# else:
    # codeEx
    # codeEx
    # codeEx

# if condition:
    # codeEx
    # codeEx
    # codeEx
# elif condition:
    # codeEx
    # codeEx
    # codeEx
# else / 굳이 필요하지않다 .


# i == 1, i == 2, i == 3
i = 0
if i == 1:
    pass
elif i == 2:
    pass
# else:
#     pass
elif i == 3:
    pass
else:
    pass
# 변수와 초기화 , 자료형
#
# 자료형
# 숫자, 문자 , 불(참,거짓)
# 숫자
#   정수(int) , 실수(float)
# 문자
#   문자열 (str)
#   문자  chr
#   ASCII / 비트들 가지고 어떻게 문자(영어 혹은 기호)로 변환할꺼니 에대한 규격\

##################################
# int 정수 int(13141.3145) -> 13141
# float 실수  float(333) -> 333.0
# str 문자열 str(333) -> "333"
# int 정수 int("333") -> 333
# int 정수 int("daare") -> daare3(X)
##################################

# print/출력 -> 다중출력과 출력관한 옵션들로 제어가가능
# input/입력 -> input,map(),split() 다중입력 과 단일입력 을 받았어
# 터미널 -> 코드 -> 터미널
#
# 논리 (로직)
# if,  else , elif
# 코드 블록 (인덴트 = 들여쓰기 ) 유효범위
# 인덴트 된 부분만 실행
# 조건 연산 (and , or , not)


# if condition:
    # codeEx
    # codeEx
    # codeEx
# codeEx

# if condition:
    # codeEx
    # codeEx
    # codeEx
# else:
    # codeEx
    # codeEx
    # codeEx

# if condition:
    # codeEx
    # codeEx
    # codeEx
# elif condition:
    # codeEx
    # codeEx
    # codeEx
# else / 굳이 필요하지않다 .


# i == 1, i == 2, i == 3
i = 0
if i == 1:
    pass
elif i == 2:
    pass
# else:
#     pass
elif i == 3:
    pass
else:
    pass


# 예상치 못한 오류 나올 수 있기에 대비를 해야  
# 우리는 예외처리라는 것을 배워 
# 예외처리 < 오류를 내지않는게 더 중요해 
# 
# 21 번줄
# if n%2== 1: 홀수 애들 1,3,5,7 
    # print(31)
# else: 짝수 애들 2,4,6
    # if n ==2 :
    #     print(28)
    # else :
    #     print(30)
    
    
# 체온과 증상을 4개나와 
# 함수를 만드는거지 
# -> A 인지 체크 
# A2 이상 나오는 순간 -> E 


# 조건문에 논리연산을 안쓰는게 좋아 / 중첩으로 처리

cnt = 0

def check(s,c):
    cnt=0
    if s:
        if c>=37:
            cnt += 1
        else:
            pass
    else:
        if c>=37:
            pass
        else:
            pass
s1,c1 = map(int, input().split())
s2,c2 = map(int, input().split())
s3,c3 = map(int, input().split())

check(s1,c1)
check(s2,c2)
check(s3,c3)

if cnt>=2:
    print("E")
else:
    pass
