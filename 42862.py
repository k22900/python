# 조건1:바로 앞 또는 뒤번호 학생에게 만 빌릴수있다
# 조건2:체육복X=수업참여X
# 조건3:여벌있던 학생이 도난됬을시 남한테 대여 불가
n=5
lost=[2,4]
reserve=[3]
cnt=0
delete=[]
for val in lost:
    for i in reserve:
        if val==i:
            cnt+=1
    if cnt==1:
        reserve.remove(val)
        delete.append(val)
        cnt=0
for i in delete:
    lost.remove(i)
delete=[]

for idx,val in enumerate(lost):
    if 0!=reserve.count(val-1):
        delete.append(val)
        reserve.remove(val-1)
    elif 0!=reserve.count(val+1):
        delete.append(val)
        reserve.remove(val+1)

for i in delete:
    lost.remove(i)
n-=len(lost)
print(n)