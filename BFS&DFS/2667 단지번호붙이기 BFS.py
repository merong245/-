import sys
from collections import deque
input=sys.stdin.readline

n = int(input())

grid = [list(input().rstrip())
        for _ in range(n)]

visited = [[False for _ in range(n)]
           for _ in range(n)]

def can_go(x,y):
    return 0<=x<n and 0<=y<n and not visited[x][y] and grid[x][y] == '1'

def bfs():

    dxs, dys = [0,0,-1,1],[1,-1,0,0]
    cnt = 1
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = dx+x, dy+y
            if can_go(nx,ny):
                visited[nx][ny] = True
                q.append((nx,ny))
                cnt += 1
    return cnt

num_of_dange = 0
ans = []
q =deque()
for i in range(n):
    for j in range(n):
        if grid[i][j] == '1' and not visited[i][j]:
            q.append((i,j))
            visited[i][j] = True
            num_of_dange += 1
            ans.append(bfs())

print(num_of_dange)

for i in sorted(ans):
    print(i)
            
