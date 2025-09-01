# from collections import Counter
# def solution(i, j, k):
#     nums=[]
#     for v in range(i,j+1):#i부터 j수를 구한다
#         v=str(v)
#         for j in v:
#             nums.append(j)
#     cntNum=Counter(nums)
#     answer = cntNum.get(k)
#     answer = 0
#     return answer


# print(solution(1,13,1))
from collections import Counter
def solution(array):
    nums=""
    for v in array:
        v=str(v)
        nums+=v
    cntedNum=Counter(nums)
    return cntedNum.setdefault("7",0)
print(solution([7,77,17]))