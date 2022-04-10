import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

grid = [list(input().rstrip()) for _ in range(n)]

visited = [[False]* n for _ in range(n)]

def bfs(x,y, color,flag):
    q = deque()
    q.append((x,y))
    dxs, dys = [0,0,-1,1],[1,-1,0,0]
    visited[x][y] = True

    if flag:
        while q:
            x,y = q.popleft()
            for dx, dy in zip(dxs,dys):
                nx,ny= dx+x, dy+y
                if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                    if color in ('R','G'):
                        if grid[nx][ny] in ('R','G'):
                            q.append((nx,ny))
                            visited[nx][ny] = True
                    elif color == grid[nx][ny]:
                        q.append((nx,ny))
                        visited[nx][ny] = True
        return 
    
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs,dys):
            nx, ny = dx+x, dy+y
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if grid[nx][ny] == color:
                    q.append((nx,ny))
                    visited[nx][ny] = True



normal_cnt = 0 
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j,grid[i][j],0)
            normal_cnt += 1
cnt = 0
visited = [[False]* n for _ in range(n)]


for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j,grid[i][j],1)
            cnt += 1
print(normal_cnt, cnt)    
