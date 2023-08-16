# 변수와 초기화 , 자료형
#
# 자료형
# 숫자, 문자 , 불(참,거짓)
# 숫자
#   정수(int) , 실수(float)
# 문자
#   문자열 (str)

# input() -> str
# int(input()) -> int(str) -> int
# float(input()) -> float(str) -> float


# print/출력 -> 다중출력과 출력관한 옵션들로 제어가가능
#    다중출력 : 여러개의 매개변수들을 전달하여서 출력
#          ex : print("hi",123,"poo",1.11) # 4 개 출력
#  다중출력 + 제어 : 여러개의 매개변수들을 전달하여서 출력
#          ex : print("hi",123,"poo",1.11,sep = " ", end = " ") # 4 개 출력

# input/입력 -> input,map(),split() 다중입력 과 단일입력 을 받았어
#          ex : map(int,input().split())

# 제어문 (프로그래밍)
# if - else - el(se)if

# if 문이 뭉탱이

condition_0 = False
condition_1 = False
condition_2 = False

if condition_0:
    pass
else:
    pass

if condition_2:
    pass

if condition_0:
    pass
elif condition_0 and condition_1:
    pass
else:
    pass


# + - * / // %
# % -> 짝홀 구분 , 배수 !


# 어떤 문제를 직면했을때
# 그 문제를 분석 및 해석하는 능력
# 스키마 + 트레이닝

# 배타적(이분법적)사고

# 예제 : 최대값
# 3개의 요소가있어 (a,b,c)

#   [I] a 최대가 되는 경우
#  [II] b 최대가 되는 경우
# [III] c 최대가 되는 경우

# U = [I] + [II] +[III]


# a >= b >= c
# a <= b <= c


# --------------------------------------------

# 반복문

# 왜 필요하지?
# -> 하기싫어 반복적인 작업 싫어!
# print(1)
# print(1)
# print(1)
# print(1)
# print(1)
# print(1)
# print(1)
# print(1)
# print(1)
# print(1)

# for , while

# for

# for _ in range(10):
#     print(1)
# for i in arr:
    # pass


for i in range(100, -5, -35):  # for i in range (4):
    # i = 100
    # i = 65
    # i = 30
    if i % 30 == 0:
        print(f"30의 배수 인 {i} 이다!~")
    else:
        print(i)

# range(시작점 , 끝점 , 증가폭 )

# for (i+5) in range(17): (x)
    # print(i, end=" ")