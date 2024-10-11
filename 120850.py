# 문자를 제외한 만 배열에 담아 오름차순 정렬후 출력한다
# print(ord("0"),ord("1"),ord("2"),ord("3"),ord("4"),ord("5"),ord("6"),ord("7"),ord("8"),ord("9"))
my_string="p2o4i8gj2"
answer=[]
# for idx,val in enumerate(my_string):
#     temp=ord(val)
#     if temp>=48 and temp<=57:
#         answer.append(int(my_string[idx]))
for v in my_string:
    if v.isdecimal():
        answer.append(v)
answer=list(map(int,answer))
answer.sort()

print(answer)
answer.sort()