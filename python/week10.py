# 지금 까지 뭐했어 우리?
# 함수 , 조건문 , 연산자
# 함수: print(), input()
# python 언어가 어떤 규칙을 따르는지 .. (초기화하는 방법 , 자료형구분..)
# 
# 조건문 ... 반복문...
# 조건문으로 -> "설계할 수 있다!"
# 내가 원하는 값으로 필터링 
# 설계 ~> 프로그래밍하는거야 

# 1 2 3 4 5 6 7
# 조건: 5보다 큰놈 죽여  
# 1 2 3 4 5 
# 조건: 짝수 죽여  
# 1   3   5

# 반복문 
# 반복하는 것을 싫어해, 공부를 못하는이유! 반복을 싫어 !
# 1 1 1 1 1 1 1 1 1 1 (Ok!)
# for _ in range(10):
#     print(1 ,end=" ")

# 1 2 3 4 5 6 7 8 9 10

# 4 2 0 -2 -4 -6 -8 -10

# for , while


# for 변수 in range(숫자):
# 반복할 범위 : 0 ~ 숫자-1
# 변수 = 0
# 변수 = 1
# 변수 = ... 
# 변수 = 숫자-1

# for num in range(10):
#     print(num+1 ,end = " ")

# i = 1
# for _ in range(10):
#     print(i ,end = " ")
#     i+=1

# 다 같다면 

# 다 같지않을때 ..
    # 작은놈 .. 



a,b,c=map(int,input().split())

if a<=b and a<=c:
    print(a)
elif b<=a and b<=c:
    print(b)
elif c<=a and c<=b:
    print(c)

# -99 -100 -98

# a 가 13 의 배수니? 

# if a % 13 == 0:  



# A B -> True

# if A:
#     True
# elif B:
#     True
# else:
#     False

# if A or B:
#     True
# else:
#     False
    
    # A : a' and b' 
    # B : a'' and b''
