# #1.  ' 이걸 출력해보세여 
# print("'")
# print("'")
# #2.  " 이걸 출력해보세요 
# print('"')
# print(""")
# #3.  \ 이걸 출력해보세요 
# print("\")

#4. print(" ", " ") 에서 인자는 몇개인가?
# 2

#5. print(3, " ",6) 에서 인자는 몇개인가?
# 3

#6. print(35, " ",6) 에서 인자는 몇개인가?
# 3

#7. print(" "+" ",6) 에서 인자는 몇개인가?
# 2

#8. 문자열간의 (+)합은 가능하다 (O/X)
# O

#9. 문자열와 숫자(실수,정수)간의 합은 가능하다 (O/X)
# X

#10. print()는 내장 함수 이다. (O/X)
# O

#11. print()의 옵션은 [ ]개이다
# 2

#12. 문자열 내부에 변수를 쓰기위해서 사용하는 방법을 보이시오 .
# print(f"{}")

#13. 우리가 배운 자료형을 영어로 모두 쓰시오. 
# 문자(str) 숫자 (int , float)

#14. 변수를 사용하고 싶을 때는, [  ]를 해야한다. 
# 초기화, 할당, 정의 

#15. @@ = ## , 다음과 같은 과정이 있을 때, 
# =(등호)를 기준으로 오른쪽은 [ 값 ]이다.
# =(등호)를 기준으로 왼쪽은 [ 변수명(주소) ]이다.


#########################################
# print() : 내장함수  ... 원래 있던거 
#   -> print의 기능은
# 괄호 안의 인자(매개변수)들(소스코드) ->  터미널        에 출력하는 것

# input() : 내장함수  ... 원래 있던거 
#   -> input의 기능은 
#  터미널에 있는 값 -> 소스코드     에 받아드린다.

# input 항상 어떤 값이던 str로 받아 .

# int1 = str(3) + str(3)
# store1 = input()

# print(int1,type(int1))
# print(store1,type(store1))

# int2 = int("33")
# print(int2,type(int2))

# int2 = int("Hi")
# print(int2,type(int2))

# 형변환이란 것을 배웠어요! 
# 왜 필요해요 ?  -> 원하는 형식으로 바꾸기위해서 
# 왜냐하면 input()은 항상 str 로만 받기 때문입니다. 

# whatNum = int(input())
# print(whatNum3, type(whatNum))

# int(input()) int(input()) int(input()) 
# a,b,c= map(int,input().split(" "))

# print(a,b,c,d,e,sep =" ")
# a b

# a,b = map(int, input().split(" "))
# print(a,b)
a=int(input())
print(a)