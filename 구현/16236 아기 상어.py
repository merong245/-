import sys
input =sys.stdin.readline
from collections import deque

n = int(input())

grid = [list(map(int,input().split())) for _ in range(n)]


# baby shark size and to eat
bs = [2,2]

fishes = [[] for _ in range(10)]

def can_eat_cnt():
    cnt = 0
    for i in range(1,bs[0]):
        cnt += len(fishes[i])
    return cnt
    
def get_min_dist(visited):
    min_dist = int(1e9)
    x, y = 0,0
    # 마지막에 저장된 값이 가장 왼쪽이고 위쪽
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            if visited[i][j] and grid[i][j] < bs[0] and grid[i][j] > 0:
                if min_dist>=visited[i][j]:
                    min_dist = visited[i][j]
                    x= i
                    y= j
    
    return x,y,min_dist

def bfs(x,y,visited):

    dxs, dys =[-1,1,0,0], [0,0,-1,1]
    q =deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and bs[0]>= grid[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))
            
def simulate(x,y):

    time = 0
    while True:

        # 현재 상어 위치
        visited = [[0 for _ in range(n)] for _ in range(n)]
        visited[x][y] = 1
        bfs(x,y,visited)
        nx, ny, min_dist = get_min_dist(visited)
        # 이동 불가한 경우
        if min_dist == int(1e9):
            return time
        else:
            time += min_dist-1
            x,y = nx , ny
            bs[1] -= 1
            # 상어 사이즈 조절
            if bs[1] == 0:
                bs[0] += 1
                bs[1] = bs[0]
            # 먹은자리 0
            grid[x][y] = 0


for i in range(n):
    for j in range(n):
        if grid[i][j] == 9:
            # 상어 위치
            grid[i][j] = 0
            print(simulate(i,j))
    
