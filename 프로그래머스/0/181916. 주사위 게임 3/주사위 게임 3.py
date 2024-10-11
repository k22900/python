def solution(a, b, c, d):
    nums=[a,b,c,d]
    # nums_cnt=collections.Counter(nums)
    # nums_sort=str(nums_cnt.most_common())
    # if len(nums_cnt)==1:
    #     res=1111*int(nums_sort[5])
    nums.sort(reverse=True)
    numList=[nums[0]]
    numList_cnt=[]
    temp=nums[0]
    cnt=1
    
    for idx in range(1,len(nums)):
        if nums[idx]==temp:
            cnt+=1
        else:
            numList.append(nums[idx])
            numList_cnt.append(cnt)
            cnt=1
            temp=nums[idx]
    numList_cnt.append(cnt)
    cntList=[]
    for i in range(len(numList)):
        cntList.append([numList_cnt[i],numList[i]])#cntList=[[cnt,key],[cnt,key]]
    cntList.sort(reverse=True)
    if len(cntList)==1:
        res=1111*cntList[0][1]
    elif len(cntList)==2:
        if cntList[0][0]==3:
            num=10*cntList[0][1]+cntList[1][1]
            res=pow(num,2)
        else:
            res=(cntList[0][1]+cntList[1][1])*abs(cntList[0][1]-cntList[1][1])
    elif len(cntList)==3:
        res=cntList[1][1]*cntList[2][1]
    elif len(cntList)==4:
        res=cntList[len(cntList)-1][1]
#         
    
    answer = res
    return answer