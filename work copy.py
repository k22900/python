# 전제 arr1 과 arr2의 사이즈는 완전히 동일하다.
def solution(arr1, arr2):

    hLen = len(arr1)
    wLen = len(arr1[0])
    temp = [[0 for _ in range(wLen)]for _ in range(hLen)]

    for i in range(hLen):
        for k in range(wLen):
            temp[i][k] += arr1[i][k]
            temp[i][k] += arr2[i][k]

    return temp


print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))