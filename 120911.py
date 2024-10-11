# 대문자는 소문자로 바꿔주고 정렬하는 문제이다
# print(ord("a"),ord("A"))
my_string="Bcad"
# my_string=list(my_string)
# for idx,val in enumerate(my_string): 
#     temp=ord(val)
#     if temp<97:
#         temp+=32
#         my_string[idx]=chr(temp)
answer=my_string.lower()
answer=sorted(answer)
# print(type(answer))
# answer=''
# for val in my_string:
#     answer+=val
for val in my_string:
    print(val.islower())
print(*answer,sep="")
print("".join(answer))

