def solution(arr, query):
    for val in query:
        if val>0 and val<len(arr)-1:
            if val%2==0:
                arr[:val+1]
            elif val%2==1:
                arr[val:]
          
    answer=arr
    return answer
arr=[0,1,2,3,4]
query= [4,1,2]
answer=solution(arr,query)
print(answer)
arr.append