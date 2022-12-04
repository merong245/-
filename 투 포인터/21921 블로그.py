import sys

input = sys.stdin.readline


def solution(x, n, board):

    left, right = 0, x
    now = sum(board[:x])
    answer = [now, 1]

    while right < n:
        now -= board[left]
        now += board[right]
        left += 1
        right += 1
        if answer[0] < now:
            answer[0] = now
            answer[1] = 1
        elif answer[0] == now:
            answer[1] += 1

    if answer[0]:
        print(answer[0])
        print(answer[1])
    else:
        print("SAD")


n, x = map(int, input().split())
board = list(map(int, input().split()))
solution(x, n, board)
