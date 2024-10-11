# 연속으로 같은 숫자가 나올때 제거하는 문제
# 조건:순서유지O,중복된숫자가 연속으로X

arr=[1,1,3,3,0,1,1]
# nums=[]
# temp=-1
# # for i in arr:
# #     if i!=temp:
# #         nums.append(i)
# #         temp=i
# print(nums)

answer=[]
answer.append(arr[0])
for  idx,rear in enumerate(arr):
    
    if  idx==0:
        continue
    front=arr[idx-1]
    if rear==front:
        continue
    else:
        answer.append(rear)
print(answer)