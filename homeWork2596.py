binaryDictionary=["000000","001111","010011","011100","100110","101001","110101","111010"]

def binaryMatcher(val):
    
    for idx,v in enumerate(binaryDictionary):
        cnt=0
        for orgBinary,inThebinary in zip(val,v):
            if orgBinary!=inThebinary:#이진코드가 상이할 때
                cnt+=1
        if cnt<=1:
            return chr(ord("A")+idx)
        
    return False#1개 이하로 틀린게 하나도 없다

def binaryAnalyzer(val):#val=000000
    
    for idx,v in enumerate(binaryDictionary):
        if val==v:#완전히 일치할시
            binaryOutput=(chr(ord("A")+idx))
            return binaryOutput
        # 완전히 일치하는게없을때 아래로
    result=binaryMatcher(val)
    return result
                
            
            
                
        
# 특정 6자 이진배열=1단어
# 1자 까지 달라도 알수있다
# 문자(해석가능시)또는 특정위치출력(해석불가시)
# n=단어의 개수

import sys
input=sys.stdin.readline

n=int(input())
binaryValue=input()
# print(binaryValue)

binaryWord=[]# binaryWord=입력받은 이진을 해석하기전에 6자로 분할한것
for i in range(n):
    binaryWord.append(binaryValue[i*6:(i*6)+6])
# print(binaryWord)

convertedCharacter=[]

for i in range(n):
    res=binaryAnalyzer(binaryWord[i])#6개 짜리 이진코드를 단어로 번역해 주기위한것
    if res==False:
        convertedCharacter.clear()
        convertedCharacter.append(i+1)
        break
    else:
        convertedCharacter.append(res)
        
for i in range(len(convertedCharacter)):
    print(convertedCharacter[i],end="")