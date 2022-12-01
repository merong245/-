import sys
from collections import deque

input = sys.stdin.readline


def solution(n, m, board):
    q = deque()
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                q.append((i, j))
                visited[i][j] = 0
            elif board[i][j] == 0:
                visited[i][j] = 0

    # bfs
    while q:
        x, y = q.popleft()

        for dx, dy in zip([0, 0, -1, 1], [1, -1, 0, 0]):
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if board[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

    for i in range(n):
        print(*visited[i])


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
solution(n, m, board)
