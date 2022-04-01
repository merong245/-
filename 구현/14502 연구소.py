import sys
from collections import deque
import copy
input = sys.stdin.readline

n, m = map(int,input().split())

grid = [list(map(int,input().split()))
        for _ in range(n)]

def can_go(x,y, temp):
    return 0<=x<n and 0<=y<m and not temp[x][y]

def bfs():
    
    q = deque()
    dxs , dys = [1,-1,0,0], [0,0,1,-1]
    temp = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            temp[i][j] = grid[i][j]
    
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                q.append((i,j))
    while q:
        
        x,y = q.popleft()

        for dx, dy in zip(dxs,dys):
            nx, ny = dx+x, dy+y

            if can_go(nx,ny,temp):
                temp[nx][ny] =2
                q.append((nx,ny))

    global ans
    cnt = 0
    for i in range(n):
        cnt += temp[i].count(0)
    ans = max(cnt,ans)
        

def make_wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                grid[i][j] = 1
                make_wall(cnt+1)
                grid[i][j] = 0


ans = 0
make_wall(0)
print(ans)
