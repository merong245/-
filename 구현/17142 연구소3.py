import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

answer = int(1e9)
un_act_viruses = []
cases = []
blank_cnt = 0


def bfs(act_viruses,blank_cnt):

    q = deque()
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    for x, y in act_viruses:
        q.append((x, y))
        visited[x][y] = 0
    dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

    while q:
        x, y = q.popleft()

        # 감염시킬 빈칸이 없는 경우
        if blank_cnt == 0:
            return max(map(max,visited))

        for dx, dy in zip(dxs, dys):
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] < 0:
                    # 빈칸 감염
                    if grid[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] +1
                        blank_cnt -= 1
                        q.append((nx, ny))
                    # 바이러스 활성화
                    if grid[nx][ny] == 2:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))

    # 루프를 다 돈 경우에 빈칸이 남은 경우
    return int(1e9)

def choose(depth, virus):
    if len(virus) == m:
        cases.append(list(virus))
        return
    elif depth == len(un_act_viruses):
        return

    virus.append(un_act_viruses[depth])
    choose(depth + 1, virus)
    virus.pop()
    choose(depth + 1, virus)


# 바이러스 모으기
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            un_act_viruses.append((i, j))
        elif grid[i][j] == 0:
            blank_cnt += 1

# 활성화 바이러스 선택
choose(0, [])
for act_viruses in cases:
    answer = min(bfs(act_viruses,blank_cnt), answer)

# 결과가 INF인 경우 -1
print(answer if answer != int(1e9) else -1)
