# 입력=int num
# 출력=Return bool
# 동작=홀수이면서 7의배수 or 짝수이면서 13의 배수인수
# def isStrangeNum(num):
#     if num%2==1 and num%7==0:
#         return True
#     elif num%2==0 and num%13==0:
#         return True
#     else:
#         return False
    
# print(isStrangeNum(7))
# print(isStrangeNum(52))
# print(isStrangeNum(6))


# __________________________________________________

# 입력=int num
# 출력=bool
# 구조=num이 3의배수인가?  

# 입력= int num
# 출력= bool
# 구조= num에 3,6,9중에 하나라도 들어있는가? 

def isMultiple3(num):
        if num%3==0:
            return True
        else:
            return False

            
def isIncluded369(num):
        i=str(num)
        if "3" in i or "6" in i or "9" in i:
            return True
        else:
            return False

a=3
b=10000000000
cnt=0
for i in range(a,b+1):
    if isMultiple3(i):
        cnt+=1
        print(i)
    elif isIncluded369(i):
        cnt+=1
        print(i)
print(cnt)












