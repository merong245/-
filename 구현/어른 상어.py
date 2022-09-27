import sys

input = sys.stdin.readline


def simulate(shark, smell, k):
    cnt = 0
    # 상어가 한마리 남을 때 까지, 그 상어는 번호가 1
    while(len(shark) != 1 and cnt < 1001):
        # 냄뿌
        for num, [x, y] in shark.items():
            smell[x][y] = [num, k]

        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # 이동
        for num, [x, y] in shark.items():

            mv_flag = False
            #  냄새 없는 칸이 있는 경우
            for d in sd_p[num - 1][sd[num - 1] - 1]:
                dx, dy = direction[d - 1]
                nx, ny = dx + x, dy + y
                if 0 <= nx < n and 0 <= ny < n and smell[nx][ny] == [0, 0]:
                    shark[num] = [nx, ny]
                    mv_flag = True
                    # 이동한 방향이 보고있는 방향
                    sd[num - 1] = d

                    grid[nx][ny].append(num)
                    grid[x][y].remove(num)

                    break
            # 위에 서 이동 못한경우
            if not mv_flag:
                # 냄새 있는 칸만 있는 경우
                # 본인의 냄새 방향으로
                for d in sd_p[num - 1][sd[num - 1] - 1]:
                    dx, dy = direction[d - 1]
                    nx, ny = dx + x, dy + y
                    if 0 <= nx < n and 0 <= ny < n and smell[nx][ny][0] == num:
                        shark[num] = [nx, ny]
                        # 이동한 방향이 보고있는 방향
                        sd[num - 1] = d
                        grid[nx][ny].append(num)
                        grid[x][y].remove(num)

                        break
        #한마리 남기기와 냄새 제거
        for i in range(n):
            for j in range(n):
                if len(grid[i][j])> 1:
                    winner = min(grid[i][j])
                    for t in grid[i][j]:
                        if t != winner:
                            shark.pop(t)
                    grid[i][j] = [winner]

                # 냄새 처리
                if smell[i][j][1]:
                    # 0되면 냄새 사라짐
                    if smell[i][j][1]-1 == 0:
                        smell[i][j] = [0,0]
                    # 냄새 1 감소
                    else:
                        smell[i][j][1] -= 1
        cnt += 1
    return cnt if cnt <1001 else -1
# k번 이동후 냄새 사라짐


# 냄새가 없는 칸으로 방향잡기
# 그런칸 없으면 자신의 냄새가 있는 칸
# 방금 이동한 방향이 보고있는 방향
# 각 상어마다 각 방향에 따른 이동 우선순위가 있음

# 이동후 한 칸에 여러 상어 있는 경우 가장 작은 번호 상어 제외 쫒겨남

# 1번 상어만 남게 되기 까지 몇초?

# 시뮬레이션

n, m, k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

# 방향 1 위 2 아래 3 왼 4오른쪽
# 상어가 보고 잇는 방향
sd = list(map(int, input().split()))
# 상어 우선순위 위 아래 왼 우 순서
sd_p = [[list(map(int, input().split())) for _ in range(4)] for _ in range(m)]

# 냄새 [상어번호, 유지시간]
smell = [[[0, 0] for _ in range(n)] for _ in range(n)]
shark = {}
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            # x,y
            shark[grid[i][j]] = [i, j]
            # 상어의 번호저장
            grid[i][j] = [grid[i][j]]
        else:
            grid[i][j] = []
print(simulate(shark, smell, k))
