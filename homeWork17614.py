# n까지 몇번의박수를 치는가
n=int(input())

compList=["3","6","9"]

cnt=0
for i in range(n+1):
    for s in str(i):
        # if s=="3" or s=="6" or s=="9":
            # cnt+=1
        if s in compList:  #리스트 안에 있는 원소들 중에 현제수가있는가 
            cnt+=1
print(cnt)