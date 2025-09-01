# def solution(arr1, arr2):
#     highLenth=len(arr1)
#     lineLenth=len(arr1[0])
#     # line=[0 for n in range(lineLenth)]
#     high=[[0 for n in range(lineLenth)] for n in range(highLenth)] 
#     for i in range(highLenth):
#         # tempList=[]
#         for k in range(lineLenth):
#             high[i][k]+=arr1[i][k]
#             high[i][k]+=arr2[i][k]
            
#             # tempList.append(res)
#         # answer.append(tempList)
#     return high
# print(solution([[1,2],[2,3]],[[3,4],[5,6]]))
def solution(s, n):
    answer=0
    for i in s:
        num=9
        if i.isupper():
            num=ord(i)
            num+=n
            if 90<num:
                num-=26
            
            
        elif i.islower():
            num=ord(i)
            num+=n
            if 122<num:
                num-=26
        i=chr(num)
        
            
        print(i)
    return answer
solution("a B z",4)