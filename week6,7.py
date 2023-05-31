# +
# -
# *
# /
# // :몫
# %  :나머지
# n1,n2 = 2,4

# def calculator(num1,num2):
#     print("num1+num2:",num1+num2)
#     print("num1-num2:",num1-num2)
#     print("num1num2:",num1num2)
#     print("num1/num2:",num1/num2)
#     print("num1//num:",num1//num2)
#     print("num1%num2:",num1%num2)

# calculator(n1,n2)

# 초기화
# n1 = n1 + 1
# print(n1)
# n1 += 2;print(n1)
# n1 = 2;print(n1)
# n1 -= 2;print(n1)
# n1 /= 2;n1 = int(n1);print(n1)
# n1 //= 2;print(n1)
# n1 %= 2;print(n1)
# n1 더하기 1 (한 후 저장)
# 단순 연산과정을 좀 더 가독성 있게 표현하고 싶어
# a = 1

# a = a + 5
# a = a - 5

# a += 5
# a =+ 5(X)
# a =-5 (X)
# a += 5
# a -= 5

# a
# 5
# a = 5  # a를 5로 곱한 것으로 a를 초기화해줘

# a/5
# a%5 나누기를 한 후 나머지.!!!!
# 31%5 ~> 1
# 23%10 ~> 3
# a %= 4  # a를 4로 나눈 것의 나머지로 a를 초기화해줘

# a//5 나누기를 한 후 몫.!!!!
# 31//5 ~> 6
# 23//10 ~> 2
# a,b = map(int,input().split())
# print(a+b)
# res1 = a + b
# res2 = a - b
# res3 = a
#  b
# res4 = a / b
# print(res1,res2,res3,res4,sep ="\n")
# 변수는 소문자로 시작, 숫자나 기호로 시작할 수 없어요
# 예약어는 사용하지않는다. (def, int, str , return , sum , math, ...)
# 변수는 명사로 쓴다 .
# 함수는 동사로 시작한다.
# 중요하지않은 변수를 사용 할때 가 있는데
# 그럴 때는 i, j, k ..
# for i in range(0, 5):
# for j in range(10, 0, -2):
# print("Hi")
# print("\n")
# lastNum
# last_num
# num1
# iNum1
# inputNum1
# res
# ans
# 자주쓰는 것은 좀 줄여써!!
# input_num
# 상수를 선언
# 상수..? constant
# 변수 거의 똑같아요
# 변하지않는 수를 상수
# 상수는 대문자로만 이뤄져있어요
# PI = 3.141592

# [상수]최대속도 200 으로 정해둠
# MAX_SPEED = 200

# [변수]
# currSpeed = int(input())
# def speedUp(speed):
# return speed + 40
# for i in range(5):
# currSpeed = speedUp(currSpeed)
# if MAX_SPEED < currSpeed:
# currSpeed = MAX_SPEED
# print(currSpeed)
# 형변환
# a = int(input())
# var = int(var
py
# +
# -
# *
# /

# // :몫
# %  :나머지

n1,n2 = 2,4

def calculator(num1,num2):
    print("num1+num2:",num1+num2)
    print("num1-num2:",num1-num2)
    print("num1*num2:",num1*num2)
    print("num1/num2:",num1/num2)
    print("num1//num:",num1//num2)
    print("num1%num2:",num1%num2)

calculator(n1,n2)

# 초기화
# n1 = n1 + 1
print(n1)
n1 += 2;print(n1)
n1 *= 2;print(n1)
n1 -= 2;print(n1)
n1 /= 2;n1 = int(n1);print(n1)
n1 //= 2;print(n1)
n1 %= 2;print(n1)
# n1 더하기 1 (한 후 저장)
# 단순 연산과정을 좀 더 가독성 있게 표현하고 싶어
a = 1

a = a + 5
a = a - 5

a += 5
# a =+ 5(X)
# a =-5 (X)

a += 5
a -= 5

# a*5
a *= 5  # a를 5로 곱한 것으로 a를 초기화해줘

# a/5

# a%5 나누기를 한 후 나머지.!!!!
# 31%5 ~> 1
# 23%10 ~> 3


a %= 4  # a를 4로 나눈 것의 나머지로 a를 초기화해줘

# a//5 나누기를 한 후 몫.!!!!
# 31//5 ~> 6
# 23//10 ~> 2


# a,b = map(int,input().split())

# print(a+b)

# res1 = a + b
# res2 = a - b
# res3 = a * b
# res4 = a / b

# print(res1,res2,res3,res4,sep ="\n")


# 변수는 소문자로 시작, 숫자나 기호로 시작할 수 없어요
# 예약어는 사용하지않는다. (def, int, str , return , sum , math, ...)
# 변수는 명사로 쓴다 .
# 함수는 동사로 시작한다.
# 중요하지않은 변수를 사용 할때 가 있는데
# 그럴 때는 i, j, k ..

# for i in range(0, 5):
#     for j in range(10, 0, -2):
#         print("Hi")
#     print("\n")

# lastNum
# last_num

# num1
# iNum1
# inputNum1

# res
# ans
# 자주쓰는 것은 좀 줄여써!!
# input_num

# 상수를 선언
# 상수..? constant
# 변수 거의 똑같아요
# 변하지않는 수를 상수

# 상수는 대문자로만 이뤄져있어요
PI = 3.141592

# [상수]최대속도 200 으로 정해둠
MAX_SPEED = 200

# [변수]
# currSpeed = int(input())


# def speedUp(speed):
#     return speed + 40


# for i in range(5):
#     currSpeed = speedUp(currSpeed)

#     if MAX_SPEED < currSpeed:
#         currSpeed = MAX_SPEED

#     print(currSpeed)

# 형변환
a = int(input())
var = int(var)
