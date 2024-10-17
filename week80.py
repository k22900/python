# def solution(str_list):
#     answer=[]
#     for idx,val in enumerate(str_list):
#         if val=="l":#"l"을 만나면은 "l"을 기준으로 앞쪽을 리스트 슬라이싱해서 answer을 초기화한다
#             answer = str_list[:idx]
#             break

            
#         elif val=="r":#"r"을 만나면은 "r"을 기준으로 뒤쪽을 리스트 슬라이싱을 해서 answer을 초기화한다
#             answer = str_list[idx+1:]
#             break
           
#     return answer


# str_list = ["u", "u", "l", "r"]
# print(solution(str_list))
# _______________________________________________
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
print(solution([0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]))