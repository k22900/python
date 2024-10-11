# 주어진 정수들을 이어붙였을때 나올수있는 가장큰수 구하기
numbers=[6,10,2]
from itertools import permutations
permutations_numbers=list(permutations(numbers,len(numbers)))
# print(permutations_numbers)
temp=""
answer="0"
for idx in range(len(permutations_numbers)):
    for v in permutations_numbers[idx]:
        temp+=str(v)
    print(temp)
    if temp>answer:
        answer=temp
    temp=""

print(answer)