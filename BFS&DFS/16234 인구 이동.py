import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y, visited, day):
    dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]
    q = deque()
    q.append((x, y))
    visited[x][y] = day
    res = [[], 0]

    while q:
        x, y = q.popleft()
        res[0].append((x, y))
        res[1] += population[x][y]

        for dx, dy in zip(dxs, dys):
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] != day:
                    if l <= abs(population[x][y] - population[nx][ny]) <= r:
                        q.append((nx, ny))
                        visited[nx][ny] = day

    return res


def solution(n, l, r, population):
    day = 0

    visited = [[-1 for _ in range(n)] for _ in range(n)]

    while True:
        moved = 0
        for i in range(n):
            for j in range(n):
                if visited[i][j] != day:
                    union_country = bfs(i, j, visited, day)
                    if 1 < len(union_country[0]):
                        moved += 1
                        for [x, y] in union_country[0]:
                            population[x][y] = union_country[1] // len(union_country[0])

        if moved == 0:
            break
        day += 1
    return day


n, l, r = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, l, r, population))
