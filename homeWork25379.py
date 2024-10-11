# 홀수짝수 최대1번 인접하는 시행의 최소 횟수
# 0 = 짝수
# nums=int(input())
# numList=list(map(int,input().split()))
# state=True
# cnt=0
# tmprrNmbr=0
# while state:
    # for idx,nowNum in enumerate(numList):
    #     if idx==0 and nowNum%2==0:
    #         if numList[idx+1]%2==0:
    #             pass
    #         else:
    #             tmprrNmbr=numList[idx+1]
    #             numList[idx+1]=numList[idx+2]
    #             numList[idx+2]=tmprrNmbr
    #             cnt+=1
    #     elif idx==(len(numList)-1):
    #         if nowNum%2==1:
    #             if numList[idx-1]%2==1 and numList[idx-2]%2==1:
    #                 cnt+=1
    #                 break
    #     elif numList[idx]%2==0:
    #         if numList[idx+1]%2==0:
    #             pass
    #         else:
    #             tmprrNmbr=numList[idx]
    #             numList[idx]=numList[idx+1]
    #             numList[idx+1]=tmprrNmbr
    #             cnt+=1
    #     elif numList[idx]%2==1:
    #         if numList[idx+1]%2==1:
    #             pass
    #         else:        
    #             tmprrNmbr=numList[idx]
    #             numList[idx]=numList[idx+1]
    #             numList[idx+1]=tmprrNmbr
    #             cnt+=1
    # print(cnt)
# ________________________________________________
# 진행순서=시계방향
# 룰은 기본적인 369게임
# 알고싶은것=n번까지의 박수 횟수
n=int(input())
cnt=0
for i in range(n+1):
    s=str(i)
    for w in s:
        if w=="3" or w=="6" or w=="9":
            cnt+=1
print(cnt)