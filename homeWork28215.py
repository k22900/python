# 대피소의 개수=K
# 집의 개수=N
# 조건1:모든집과의 거리중 max가 가장작을때

import math
N,K=map(int,input().split())
distance=[]
distanceMax=[]
x=[0]*N
y=[0]*N
for i in range(N):
   x[i],y[i]=map(int,input().split())
for i in range(N):
    for j in range(N):
        if i!=N:
            distance.append(abs(x[i]-x[j])+abs(y[i]-y[j]))
    distanceMax.append(max(distance))
    distance.clear
ans=min(distanceMax)
print(ans)