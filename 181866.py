myString="dxccxbbbxaaaa"
answer=[]
temp=""
startIdx=0
for idx,val in enumerate(myString):
    if val=="x":
        temp=myString[startIdx:idx]
        if temp=="":
            startIdx=idx+1
            continue    
        else:
            answer.append(temp)
            temp=""
            startIdx=idx+1
temp=myString[startIdx:]
if temp!="":
    answer.append(temp)
    temp=""
answer.sort()
print(answer)
    
    
    
