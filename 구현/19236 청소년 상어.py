import sys
import copy
input = sys.stdin.readline


def dfs(sx,sy, grid, res):
    global answer

    # 상어 이동
    sd = directions[grid[sx][sy][1]]
    res += grid[sx][sy][0]

    answer = max(res, answer)
    grid[sx][sy][0] = 0
    # 물고기 이동
    for i in range(1, 17):
        fx, fy = -1, -1
        for x in range(4):
            for y in range(4):
                if grid[x][y] and grid[x][y][0] == i:
                    fx, fy = x, y
                    break

        if fx == -1 and fy == -1:
            continue
        fd = grid[fx][fy][1]

        for i in range(8):
            nd = (fd + i) % 8
            nx, ny = fx + directions[nd][0], fy + directions[nd][1]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if (sx,sy) != (nx,ny):
                    grid[fx][fy][1] = nd
                    grid[nx][ny], grid[fx][fy] = grid[fx][fy], grid[nx][ny]
                    break

    # 상어 먹방
    for i in range(1, 4):
        nsx, nsy = sx + sd[0] * i, sy + sd[1] * i
        if 0 <= nsx < 4 and 0 <= nsy < 4 and grid[nsx][nsy]:
            temp = copy.deepcopy(grid)
            temp[sx][sy] = []
            # 상어 이동
            dfs(nsx,nsy, temp,res)



'''
각 물고기는 한칸 이동, 작은 순
이동할 수 있는 칸 = 빈칸 or 다른 물고기 있는칸
이동 불가 칸 = 상어 or 경계 밖
움직일 수 있을 때 까지 45도 반시계 회전
이동 불가하면 정지
이동시 다른 물고기랑 위치 바꾸기


상어는 여러개 칸 이동가능
물고기 칸이면 먹고 방향 가짐
이동 중 먹기 x
물고기 없는 칸 이동 x
상어 이동 불가시 집으로 

상어가 먹을 수 있는 물고기 번호의 합의 최댓값
방향 1~8까지 북 부터 반시계 방향
아이디어 백트래킹

'''
directions = {1:(-1,0),2:(-1,-1),3:(0,-1),4:(1,-1),
              5:(1,0),6:(1,1),7:(0,1),0:(-1,1)}

# 번호, 방향
grid = [[] for _ in range(4)]

for i in range(4):
    data = list(map(int,input().split()))
    for j in range(4):
        grid[i].append([data[2*j],data[2*j+1]])

# 상어 넣기 상어 번호 0

answer = 0
dfs(0,0,grid,0)
print(answer)






