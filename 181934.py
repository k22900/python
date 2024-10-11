def solution(ineq, eq, n, m):
    if eq=="=":
        if ineq=="<":
            if n<=m:
                res=1
            else:
                res=0
        elif ineq==">":
            if n>=m:
                res=1
            else:
                res=0
    elif eq=="!":
        if ineq=="<":
            if n<m:
                res=1
            else:
                res=0
        elif ineq==">":
            if n>m:
                res=1
            else:
                res=0
    answer = res
    return answer
ineq="<"
eq="="
n=20
m=50