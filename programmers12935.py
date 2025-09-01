#배열이 입력될때 제일 작은수를 제거하고 그배열을 리턴하되 제거후 배열이 비었으면 배열에 -1을넣고 리턴
def solution(arr:list):
    
    minNum=min(arr)
    arr.remove(minNum)
    if len(arr)==0:
        arr.append(-1)
    answer = arr
    
    return answer

arr=[4,3,2,1]
print(solution(arr))