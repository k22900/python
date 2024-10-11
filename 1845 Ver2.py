# n//2마리를 데려갈수있고 최대한 많은 종류를 데려가려할때의 종류의 수는?
# 단 최대로 데려갈수있는 수와 최대로 만들수있는 종류가걸렸을때 더작은쪽을 출력한다
from collections import Counter
nums=[3,1,2,3]
numsCnt=Counter(nums)
numberYouCanTake=len(nums)//2
# print(numberYouCanTake) 
if numberYouCanTake<=len(numsCnt):
    answer=numberYouCanTake
else:
    answer=len(numsCnt)
print(answer)