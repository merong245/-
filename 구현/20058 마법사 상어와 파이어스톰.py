import sys
input = sys.stdin.readline

n , q =map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(2**n)]
L = list(map(int,input().split()))


def magic(l):
    temp = [[0 for _ in range(2**n)] for _ in range(2**n)]
    for i in range(0,2**n,2**l):
        for j in range(0,2**n,2**l):
            for x in range(2**l):
                for y in range(2**l):
                    temp[i+y][j+2**l-1-x] = grid[x+i][y+j]
    return temp

def dfs(x,y):
    cnt = 1
    stack = [(x,y)]
    grid[x][y] = 0
    while stack:
        x,y = stack.pop()
        for dx, dy in d:
            nx,ny = dx+x, dy+y
            if 0<=nx<2**n and 0<=ny<2**n and grid[nx][ny]>0:
                stack.append((nx,ny))
                grid[nx][ny] = 0
                cnt += 1
    return cnt


for l in L:
    grid = magic(l)
    d = [(-1,0),(1,0),(0,-1),(0,1)]

    cnt = [[0 for _ in range(2**n)] for _ in range(2**n)]
    for x in range(2**n):
        for y in range(2**n):
            for dx, dy in d:
                nx ,ny = x+dx, y+dy
                if 0<= nx < 2**n and 0<=ny<2**n and grid[nx][ny]:
                    cnt[x][y] += 1

    for x in range(2**n):
        for y in range(2**n):
            if grid[x][y] and cnt[x][y] <3:
                grid[x][y] -= 1

ice_cnt = 0
for i in range(2**n):
    for j in range(2**n):
        ice_cnt += grid[i][j]
print(ice_cnt)
ans = 0
for i in range(2**n):
    for j in range(2**n):
        if grid[i][j] > 0:
            ans = max(dfs(i,j),ans)
print(ans)