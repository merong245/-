import sys
input = sys.stdin.readline

dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]

def solution():
    global board

    board = [list(input().rstrip()) for _ in range(r)]

    answer = 0
    q = set()
    q.add((0, 0, board[0][0]))

    while q:
        x, y, alpha = q.pop()
        answer = max(answer, len(alpha))

        for dx, dy in zip(dxs, dys):
            nx, ny = dx + x, dy + y
            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in alpha:
                q.add((nx, ny, alpha + board[nx][ny]))

    return answer


r, c = map(int, input().split())

print(solution())
