# 기본아이디어:맨 처음은 가장작은것을 찾는다. 2번부터는 그다음으로 적은것들을 첮는다
def sol(nums):
    for i in range(len(nums)-1):
        m=i
        for j in range(i+1,len(nums)):
            if nums[m]>nums[j]:
                m=j
        nums[i],nums[m]=nums[m],nums[i]
        # FindMin(m,nums) 
    



target=[3,1,7,5]
sol(target)
print(target)
# 최소값을 찾는데 
# for i in range(len(target)):
#     temp=target[i:]
#     num=target[i]
#     min(temp)
