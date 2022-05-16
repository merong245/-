# 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠긴다

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

grid = [list(map(int,input().split())) for _ in range(n)]
max_num = 0
for i in range(n):
    for j in range(n):
        max_num= max(max_num,grid[i][j])

def bfs(x,y,grid,visited,k):
    q = deque()
    dxs, dys = [1,-1,0,0],[0,0,-1,1]
    q.append((x,y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs,dys):
            nx, ny = dx+x, dy+y
            if 0<=nx<n and 0<=ny<n and grid[nx][ny] > k and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True

max_cnt = 1
for k in range(1,max_num+1):
    tmp = [[0]* n for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] > k and not visited[i][j]:
                bfs(i,j,grid,visited,k)
                cnt += 1
    max_cnt = max(cnt,max_cnt)

print(max_cnt)