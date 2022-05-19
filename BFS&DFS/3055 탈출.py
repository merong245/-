import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())

grid = [list(input().rstrip()) for _ in range(n)]

s = (-1,-1)
w = []

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'S':
            s = (i, j, 0)
        if grid[i][j] == '*':
            w.append((i,j,1))


def bfs(s):
    q = deque()
    for a in w:
        q.append(a)
    q.append(s)
    visited= [[0] * m for _ in range(n)]
    visited[s[0]][s[1]] = 1
    dxs, dys = [0,0,-1,1],[1,-1,0,0]

    while q:
        x, y, f = q.popleft()
        for dx, dy in zip(dxs,dys):
            nx, ny = dx+x, dy+y
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny]:
                    if f == 0:
                        if grid[nx][ny] =='D':
                            return visited[x][y]

                        elif  grid[nx][ny] == '.':
                            q.append((nx,ny,f))
                            visited[nx][ny] = visited[x][y] + 1
                    else:
                        if grid[nx][ny] == '.':
                            q.append((nx,ny,f))
                            visited[nx][ny] = visited[x][y] + 1
    return "KAKTUS"
print(bfs(s))

