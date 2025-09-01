from math import ceil


def solution(my_str, n):
    answer = []
    # my_str=list(my_str)
    executionCount=ceil(len(my_str) / n)
    
    for i in range(executionCount):
        if executionCount!=n and i==executionCount:
            answer.append(my_str[i*n:])
        elif i==0:
            answer.append(my_str[:n])
        else:
            answer.append(my_str[i*n:(i+1)*n])
        
    return answer
my_str="abc1Addfggg4556b"
n=6
print(solution(my_str,n))
my_str="abcdef123"
n=3
print(solution(my_str,n))