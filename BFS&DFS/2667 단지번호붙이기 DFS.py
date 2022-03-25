import sys
from collections import deque
input=sys.stdin.readline

n = int(input())

grid = [list(input().rstrip())
        for _ in range(n)]

visited = [[0 for _ in range(n)]
           for _ in range(n)]

def can_go(x,y):
    return 0<=x<n and 0<=y<n and not visited[x][y] and grid[x][y] == '1'

def dfs(x,y,cnt):

    visited[x][y] = cnt

    dxs, dys = [0,0,-1,1], [1,-1,0,0]
    for dx, dy in zip(dxs,dys):
        nx, ny = dx+x, dy+y
        if can_go(nx,ny):
            dfs(nx,ny,cnt)
cnt = 1
for i in range(n):
    for j in range(n):
        if grid[i][j] == '1' and not visited[i][j]:
            dfs(i,j,cnt)
            cnt += 1
            
print(cnt-1)

ans = [0 for _ in range(cnt-1)]
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            ans[visited[i][j]-1] += 1
            
for i in sorted(ans):
    print(i)
        
