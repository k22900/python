from collections import Counter
def solution(array):
    nums=""
    for v in array:
        v=str(v)
        nums+=v
    cntedNum=Counter(nums)
    return cntedNum.setdefault("7",0)