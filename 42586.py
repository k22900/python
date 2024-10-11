# 그 개발 완료 발표하는데 걸리는일수가 얼마나 걸리고 그일수와 같은게 몇개있는지 찿는다
# 조건: 먼저 배포 해야하는 놈보다 작업이 언저 끝나도 배포하지말고 대기시킨다

progresses=[93,30,55] 
speeds=[1,30,5]
from collections import defaultdict
import math
timeCounter=defaultdict(int)
temp=0
for idx in range(len(progresses)):
    time=math.ceil((100-progresses[idx])/speeds[idx])
    # print(time)
    if temp<time:
        temp=time
        timeCounter[temp] += 1
    else:
        timeCounter[temp] += 1
    # print(TimeCounter)
answer=list(timeCounter.values())
print(answer)