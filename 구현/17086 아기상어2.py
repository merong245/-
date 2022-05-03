import sys
from collections import deque
input= sys.stdin.readline

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited = [[0]*m for _ in range(n)]
    visited[x][y] = 1
    dxs , dys = [1,-1,0,0,1,-1,1,-1],[0,0,1,-1,1,-1,-1,1]
    while q:
        x, y = q.popleft()
        for dx ,dy in zip(dxs,dys):
            nx, ny = x+dx, y+dy
            if 0<= nx <n and 0<=ny<m and not visited[nx][ny]:
                if grid[nx][ny] == 1:
                    return visited[x][y]
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))





n, m = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]

ans = -int(1e9)
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            ans = max(bfs(i,j),ans)

print(ans)
