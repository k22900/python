


def rangeOut(y,x):
    if y<0 or y>=n or x<0 or x>=m:
        return True
    return False

def sol(y,x):
    global result
    dx=[1,0]
    dy=[0,1]
    
    for i in range(2):    
        nx=x+dx[i]
        ny=y+dy[i]
        
        if y==n-1 and x==m-1:
            result=1
            return 
        if rangeOut(ny,nx):
           continue
        if vis[ny][nx]:
            continue
        if grid[ny][nx]==0:
            continue
        vis[ny][nx]=True
        sol(ny,nx)


global n
global m
global result
n,m=map(int,input().split())
grid=[]
for _ in range(n):
    grid.append(list(map(int,input().split())))
vis=[]
temp=[]
for _ in range(m):
    temp.append(False)
for _ in range(n):
    vis.append(temp)
result =0    
sol(0,0)
print(result)
