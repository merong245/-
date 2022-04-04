from collections import deque

dxs, dys = [0,0,-1,1], [1,-1,0,0]


m, n = map(int,input().split())

grid = [list(input())
        for _ in range(n)]

# 가중치 
weight= [[0]* m for _ in range(n)]

# 방문
visited = [[False] *m for _ in range(n)]


def bfs():
    q= deque()
    q.append((0,0))
    visited[0][0] = True
    
    weight[0][0] = 0

    while q:
        x,y = q.popleft()
        for dx, dy in zip(dxs,dys):
            nx, ny= dx+x, dy+y
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                visited[nx][ny] = True
                if grid[nx][ny] == '0':
                    weight[nx][ny] = weight[x][y]
                    q.appendleft((nx,ny))
                else:
                    weight[nx][ny] = weight[x][y]+1
                    q.append((nx,ny))
bfs()
print(weight[n-1][m-1])
