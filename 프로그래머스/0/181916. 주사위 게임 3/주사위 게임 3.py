from collections import Counter


def solution(a, b, c, d):
    answer = 0
    nums=Counter(sorted([a,b,c,d])) 
    cntArr=list(nums.items())
    keyNum=sorted(cntArr,key=lambda x:x[1],reverse=True)    
    # test=
    # cnt=0
    # sortedNum=sorted(nums)#a,b,c,d의 배열인 nums를 정렬시킨 함수를 초기화 
    # numList=[sortedNum[0]]
    # temp=sortedNum[0]#기준점으로 사용할 값을 초기화
    # cntList=[1]#수의 중복 개수를 담을 배열 생성(초기화 및 선언) 
    # for idx in range(1,len(sortedNum)):#정렬된 배열 순회
    #     if sortedNum[idx]==temp:#기준점 과 같은가?
    #         cntList[cnt]+=1
    #     elif sortedNum[idx]!=temp:
    #         numList.append(sortedNum[idx])
    #         temp=sortedNum[idx]
    #         cntList.append(1)
    #         cnt+=1
        
    # numArr=[]
    # for cnt,num in zip(cntList,numList):#앝은 복사를 위한 반복문
    #     numArr.append([cnt,num])
    # numArr.sort(reverse=True)
    # res=0
    res=0
#_____여기 아래부터 조건검색_____
    if keyNum[0][1]==4:#주사위의 최소값이 4개가 같은 값이 일때
        res=1111*keyNum[0][0]
    elif keyNum[0][1]==3:#주사위의 최소값이 3개가 같은 값이 일때
        ans=(10*keyNum[0][0])+keyNum[1][0]
        res=pow(ans,2)
    elif keyNum[0][1]==2:#주사위의 최소값이 2개가 같은 값이 일때
        if keyNum[1][1]==2:#주사위의 두번쨰로 작은 최소값이 2개가 같은 값이 일때
            res=(keyNum[0][0]+keyNum[1][0])*abs(keyNum[0][0]-keyNum[1][0])
        elif keyNum[1][1]==1:#주사위의 두번쨰로 작은 최소값이 1개 일때
            res = (keyNum[1][0]*keyNum[2][0])
    elif keyNum[0][1]==1:#주사위 값이 중복이 없을때
        ans=keyNum[0][0]
        res=ans
        
        
    # print(cntArr,keyNum,sep="\n")
    
    answer=res
    
    
    return answer