import sys
from collections import deque

input = sys.stdin.readline

n, m, k  = map(int,input().split())
grid = [list(input())
        for _ in range(n)]

visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n) ]


def can_go(x,y,wall):
    return 0<=x<n and 0<=y<m and not visited[x][y][wall]


def bfs():
    q = deque()
    q.append((0,0,0))
    visited[0][0][0] = 1

    dxs, dys = [-1,0,1,0] ,[0,1,0,-1]

    while q:
        x, y, wall = q.popleft()
        if x== n-1 and y==m-1:
            return visited[x][y][wall]

        for dx, dy in zip(dxs,dys):
            nx,ny = dx+x, dy+y
            if can_go(nx,ny,wall):
                if grid[nx][ny]== '0':
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    q.append((nx,ny,wall))
                elif wall < k and grid[nx][ny] == '1':
                    visited[nx][ny][wall+1] = visited[x][y][wall]+1
                    q.append((nx,ny,wall+1))
    return -1
print(bfs())
