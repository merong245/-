import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def can_go(x,y):
    global n, m
    return x>=0 and y>= 0 and x<m and y<n and not visited[x][y] and grid[x][y]


def dfs(x,y,cnt):
    dxs ,dys = [-1,0,1,0],[0,1,0,-1]

    for dx, dy in zip(dxs,dys):
        nx, ny = dx+x, dy+y
        if can_go(nx,ny):
            visited[nx][ny] = True
            cnt = max(cnt,dfs(nx,ny, cnt+1))
    return cnt

def draw(pos):
    x1,y1,x2,y2 = pos
    for i in range(y1,y2):
        for j in range(x1,x2):
            grid[i][j] = 0
            

m, n, k = map(int,input().split())
    
grid = [[1 for _ in range(n)]
        for _ in range(m)
        ]

visited = [
    [False for _ in range(n)]
    for _ in range(m)
    ]


for _ in range(k):
    draw(map(int,input().split()))

ans = []
for i in range(m):
    for j in range(n):
        max_num = 1
        if grid[i][j] and not visited[i][j]:
            visited[i][j] = 1
            ans.append(dfs(i,j,1))

print(len(ans))
for i in sorted(ans):
    print(i, end=" ")
            

            
