# # if 배아파 / 배아프다면
# # if x>=10 / x가 10이상이라면
# # if x == 1 / x가 1 이라면
# # if x != 1 / x가 1 아니라면
# # if (x == 1) and (y > 0) x가 1 이고, y 가 0이상이라면
# # if (x == 1) or (y > 0) x가 1 이거나 y 가 0이상이라면

# #  bool 연산

# # 1:True(참,사실) / 0:False(거짓)
# # T and T => 사실이고 사실이라면  => 사실
# # F and F => 거짓이고 거짓이라면  => 거짓
# # T and F => 거짓이고 거짓이라면  => 거짓
# # F and T => 거짓이고 거짓이라면  => 거짓

# # and : (앞에가 참)이면서 (뒤에 참이여야) -> 참
# # 여행지 선택 하는 기준 : 조건1 = 200km 이하 이면서 조건2 = 인기가 많은곳

# # 홍대 (T and T) -> T
# # 해운대 (F and T) -> F
# # 강릉 (T and F) -> F

# # T--->|
# # and  |----> T
# # T--->|

# # T--->|
# # and  |----> F
# # F--->|

# # F--->|
# # and  |----> F
# # T--->|

# # F--->|
# # and  |----> F
# # F--->|

# # or : (앞에가 참)이거나 (뒤에가 참) -> 참

# # 내이상형 : 160 , 165 ,170
# # cm = 165
# # if (cm == 160 or cm == 165 or cm == 170 or cm == 175):
# #     print("다좋아!")
# # else:
# #     print("이건좀 ...")

# # T--->|
# #  or  |----> T
# # F--->|

# # F--->|
# #  or  |----> T
# # T--->|

# # T--->|
# #  or  |----> T
# # T--->|

# # F--->|
# #  or  |----> F
# # F--->|

# ------------------------------------
# # if , else , elif (else + if)
# # if 조건 :
# #   들여쓰기

# # elif 조건 :
# #   들여쓰기

# # else :
# #   들여쓰기


# # if - elif - else

# # <if>
# # num = 5
# # num = 6

# # if num == 6:
# #     print("good!")

# # num = 7
# # num = 8


# # <if-if>
# num = 1
# num = 2
# if num == 2:
#     print("good!")
# num = 3
# if num == 3:
#     print("good!")
# num = 4

# # <if - elif>
# if num == 2:
#     print("good!")
# elif num == 3:
#     print("good!")


# <elif> 만 사용 절대 안돼
# <else> 만 사용 절대 안돼

# <if>-<if>

# if kg == 55:
#    if cm == 164:
#         print("내꺼야!")

# if kg == 55 and cm == 164:


# if :
#     res = b-a
# else:
#     res = a-b

# print(res)


heightForC, weight = map(int, input().split())

heightForM = heightForC / 100

bmiStats = weight/(heightForM**2)

bmiStats = int(bmiStats)

print(bmiStats)
if bmiStats >= 25:
    print("Obesity")