import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int,input().split())

grid= [input().rstrip() for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

def dfs(x,y):
    visited[x][y] = True
    board = grid[x][y]
    if board == '-':
        dxs, dys = [0,0],[1,-1]
    else:
        dxs, dys = [-1, 1], [0, 0]

    for dx, dy in zip(dxs,dys):
        nx, ny = dx+x, dy+y
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            if grid[nx][ny] == board:
                dfs(nx,ny)

cnt = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i,j)
            cnt += 1
print(cnt)