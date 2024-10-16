def solution(str_list):
    answer=[]
    for idx,val in enumerate(str_list):
        if val=="l":#"l"을 만나면은 "l"을 기준으로 앞쪽을 리스트 슬라이싱해서 answer을 초기화한다
            answer = str_list[:idx]
            break

            
        elif val=="r":#"r"을 만나면은 "r"을 기준으로 뒤쪽을 리스트 슬라이싱을 해서 answer을 초기화한다
            answer = str_list[idx+1:]
            break
           
    return answer