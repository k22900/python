
# i와j로 슬라이싱 한뒤 거기서 k번째 값을 찾는다
# i=리스트 슬라이싱 시작점
# j=리스트 슬라이싱 끝점
# k=슬라이싱된 리스트에서 찾아야될 값의 위치
import sys
input=sys.stdin.readline
array=[1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer=[]
for l in range(len(commands)):
    st= commands[l][0]
    end= commands[l][1]
    findIdx= commands[l][2]
    # print(st,end,findIdx)
    tempList=array[st-1:end]
    tempList.sort()
    answer.append(tempList[findIdx-1])
print(answer)