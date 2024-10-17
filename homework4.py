def solution(n, control):    
    answer = n#answer을 n의 값으로 초기화    
    for val in control:#control문자열에 문자를 한자씩 호출        
        if val=="w":#val이 "w"인가            
            answer+=1#True라면은 answer에 값에 +1후에 초기화        
        elif val=="s":#val이 "s"인가            
            answer-=1#True라면은 answer에 값에 -1후에 초기화        
        elif val=="d":#val이 "d"인가            
            answer+=10#True라면은 answer에 값에 +10후에 초기화        
        elif val=="a":#val이 "a"인가             
            answer-=10#True라면은 answer에 값에 -10후에 초기화    
    return answer
print(solution(0,"wsdawsdassw"))