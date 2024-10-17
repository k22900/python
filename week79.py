def solution(rank, attendance):
    participantList=[]
    cnt=0
    for i in range(1,len(rank)+1):#등수를 불러온다
            if cnt==3:#종료조건
                break
            if attendance[rank.index(i)]:#위에서 구한 등수로 rank에서의 인덱스를 찾아 attendance배열 에서 해당위치에 불값을 확인 
                participantList.append(rank.index(i))#맞으면 인덱스 값을 participantList에 추가후 cnt값을 +1한다
                cnt+=1
            
    # participantList.sort()
    answer = 0
    num=[10000,100,1]#num:a,b,c의 곱해질 값들
    for i in range(len(participantList)):
        res=participantList[i]*num[i]
        answer+=res
    return answer
ra=[3, 7, 2, 5, 4, 6, 1]
at= [False, True, True, True, True, False, False]

print(solution(ra,at))