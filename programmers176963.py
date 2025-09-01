def add(p,point):
    num=0
    for i in p:
        temp=point.get(i,0)
        num+=temp
    return num

def solution(name, yearning, photo):
    answer = []
    point={}
    for k,v in zip(name,yearning):
        point[k]=v
    for p in photo:
        n=add(p,point)
        answer.append(n)
    return answer

name=["may", "kein", "kain", "radi"]
yearning=[5, 10, 1, 3]
photo=[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

print(solution(name,yearning,photo))
