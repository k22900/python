def solution(rank, attendance):
    participantList=[]
    cnt=0
    for i in range(1,len(rank)+1):
            if cnt==3:
                break
            if attendance[rank.index(i)]:
                participantList.append(rank.index(i))
                cnt+=1
            
    # participantList.sort()
    answer = 0
    num=[10000,100,1]#num:a,b,c의 곱해질 값들
    for i in range(len(participantList)):
        res=participantList[i]*num[i]
        answer+=res
    return answer