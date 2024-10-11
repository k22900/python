binaryList=["000000","001111","010011","011100","100110","101001","110101","111010"]
def errorDetector(errorIndex,errorValue):
    cnt=0
    for Text,test in zip(binaryList[errorIndex],errorValue):
        # print(errorIndex)
        if  Text!=test:
            cnt+=1
            # print(cnt,Text,test)
    if cnt<=1:
        return True
    else:
        return False
def converter(val):
    for idx,wordCode in enumerate(binaryList):
        if wordCode==val:#완벽일치의 경우
            # print(chr(idx+ord("A")))
            return chr(idx+ord('A'))    
        n=errorDetector(idx,val)
        if n==True:#1개 이하의 숫자가다를때
            return chr(idx+ord('A'))    
    #2개 이상의 숫자가 다를때
    return n
        
            
            
         

wordCount=int(input())
# 0과1로 이루어진 수6개를 사용하여 문자를 표기할수있다
# 6자중 1개 까지는 틀려도 문자를 이해하는데 문제X
# 아닐때는 알수없으므로 처음나온 순서의 위치만 숫자로 출력한다
binaryInput=input()
binaryOut=[]
idx=0
for i in range(wordCount):
    idx=i*6
    # print(binaryInput[idx:idx+6])
    val=converter(binaryInput[idx:idx+6])
    # print(val)
    if val==False:
        binaryOut=[i+1]
        break
    else:
        binaryOut.append(val)
for i in range(len(binaryOut)):
    print(binaryOut[i],end="")
    