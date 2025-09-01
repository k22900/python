def sol(d,pos):
    if d=="W":
        pos[1]-=1
    elif d=="N":
        pos[0]+=1
    elif d=="E":
        pos[1]+=1
    elif d=="S":
        pos[0]-=1
    
    return
def rangeChack(x,y):
    if x<0 or x>=7:
        return True
    if y<0 or y>=7:
        return True
    return False
def serch(grid):
    x=0
    y=0
    dx=[0,1]
    dy=[1,0]
    
    g=0
    
    while True:
        if x==6 and y==6:
            break
    #     if x<6:
    #         if grid[y][x+1]==0:
    #             x+=1
    #         elif grid[y+1][x]==0:
    #             y+=1
    #     elif x==6:
    #         y+=1
    #     print(x,y,sep=",")
        next_x=x+dx[g]
        next_y=y+dy[g]
        if rangeChack(next_x,next_y):
            g=abs(g-1)
            continue
        if grid[next_y][next_x] == 1:
            g=abs(g-1)
            continue
        
        x=next_x
        y=next_y
        print(y,x)
    
grid = []

for i in range(7):
    grid.append(list(map(int,input().split())))
serch(grid)
# print(grid)
# 0 1 1 1 1 1 1
# 0 1 1 1 1 1 1
# 0 0 0 0 1 1 1
# 1 1 1 0 1 1 1
# 1 1 1 0 0 0 0
# 1 1 1 1 1 1 0
# 1 1 1 1 1 1 0
