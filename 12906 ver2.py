# 연속으로 같은 숫자가 나올때 제거하는 문제
# 조건:순서유지O,중복된숫자가 연속으로X

arr=[1,1,3,3,0,1,1]
answer=[]
answer.append(arr[0])
temp=arr[0]
for  idx in range(1,len(arr)):
    if arr[idx]==temp:
        continue
    else:
        answer.append(arr[idx])
        temp=arr[idx]
print(answer)