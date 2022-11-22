import sys
from collections import deque

input = sys.stdin.readline

n, k, r = map(int, input().split())

road = set()
cows = []
board = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(r):
    r1, c1, r2, c2 = map(int, input().split())
    road.add((r1 - 1, c1 - 1, r2 - 1, c2 - 1))
    road.add((r2 - 1, c2 - 1, r1 - 1, c1 - 1))

for _ in range(k):
    r1, c1 = map(int, input().split())
    cows.append((r1 - 1, c1 - 1))
    board[r1-1][c1-1] = 1


def bfs(start):
    q = deque()
    start_cow = cows[start]
    q.append(start_cow)
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[start_cow[0]][start_cow[1]] = True

    dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if (nx, ny, x, y) in road:
                    continue
                else:
                    visited[nx][ny] = True
                    q.append((nx, ny))

    cnt = 0
    for cow in cows[start+1:]:
        cnt += not visited[cow[0]][cow[1]]
    return cnt


answer = 0
for i in range(k-1):
    # i 번째 소가 j번째 소에게 가는 것
    answer += bfs(i)

print(answer)
