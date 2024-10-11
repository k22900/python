
# 한명빼고 다 완주했을때 완주못한선수의 이름을구하자
# partCnt=participant를 Counter형식으로 변환 한것
# completCnt=completion을 Counter형식으로 변환한것
from collections import Counter

participant=["leo", "kiki", "eden"]
completion=["eden", "kiki"]

partCnt=Counter(participant)
completCnt=Counter(completion)

result=partCnt-completCnt
for key,val in result.items():
    answer=key

print(answer)