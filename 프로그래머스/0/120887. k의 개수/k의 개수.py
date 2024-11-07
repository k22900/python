from collections import Counter
def solution(i, j, k):
    nums=[]
    for v in range(i,j+1):#i부터 j수를 구한다
        v=str(v)
        for j in v:
            nums.append(int(j))
    cntedNum=Counter(nums)
    res=cntedNum.get(k)
    if res != None:
         return res
    return 0