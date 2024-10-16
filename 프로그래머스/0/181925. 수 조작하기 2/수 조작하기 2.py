def solution(numLog):
    answer = ''
    res=0
    for val in numLog:
        if res+1==val:
            answer=answer+"w"
        elif res-1==val:
            answer=answer+"s"
        elif res+10==val:
            answer=answer+"d"
        elif res-10==val:
            answer=answer+"a"
        res=val
        
    
    return answer