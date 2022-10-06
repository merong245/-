import sys
from collections import deque
input = sys.stdin.readline

# -1 검 0 무지개 일반 M이하

# 그룹
# 일반블록 적어도하나 and 일반블록 색 전부 동일
# 검은 블록 x 무지개 제한 x
# 그룹의 블록의 개수는 2보다 크거나 같아야함

# bfs

def bfs(i,j,color):
    q = deque()
    q.append((i,j))
    dxs,dys = [-1,1,0,0],[0,0,-1,1]
    block_cnt = 1
    rainbow_cnt = 0
    blocks = [[i,j]]
    rainbows = []

    while q:
        x,y = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx, ny = dx+x, dy+y
            # 범위 안과 방문 하지 않았다면
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:

                if grid[nx][ny] == color:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    block_cnt += 1
                    blocks.append([nx,ny])
                elif grid[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    block_cnt += 1
                    rainbow_cnt += 1
                    rainbows.append((nx,ny))

    # 무지개 블록의 경우 다시 경로 지워주기
    for x,y in rainbows:
       visited[x][y] = 0
    blocks.sort()
    return [block_cnt,rainbow_cnt, blocks[0],blocks+rainbows]

def remove(block):
    for x,y in block:
        grid[x][y] = -2

def gravity(grid):
    for i in range(n-2,-1,-1):
        for j in range(n):
            if grid[i][j] > -1:
                r = i
                while True:
                    if 0<= r+1< n and grid[r+1][j] == -2:
                        grid[r+1][j] = grid[r][j]
                        grid[r][j] = -2
                        r += 1
                    else:
                        break

def rotate90(grid):
    return list(map(list,zip(*grid)))[::-1]


n, m = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]
score = 0
while True:
    blocks= []
    visited = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # 일반 블록인 경우, 기준
            if grid[i][j] >0 and not visited[i][j]:
                visited[i][j] = 1
                # blocks_info = [블록 개수, 무지개 블록수, 기준블록, 블록 좌표]
                blocks_info = bfs(i,j,grid[i][j])
                # 블록이 두개 이상
                if blocks_info[0] >= 2:
                    blocks.append(blocks_info)
    # 가장 큰 블록, 무지개 블록 수 , 기준 행, 기준 열
    blocks.sort(key = lambda x : (-x[0],-x[1],-x[2][0],-x[2][1]))
    if not blocks:
        break

    # 블록 제거
    remove(blocks[0][3])
    score += blocks[0][0]**2
    gravity(grid)
    grid = rotate90(grid)
    gravity(grid)

print(score)