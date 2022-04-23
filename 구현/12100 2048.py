import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())

grid = [list(map(int,input().split())) for _ in range(n)]

def merge(direct, board):
    # 오른쪽
    if direct == 0:
        for i in range(n):
            end = n-1
            for j in range(n-2,-1,-1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][end] == 0:
                        board[i][end] = tmp
                    elif tmp == board[i][end]:
                        board[i][end] = board[i][end]*2
                        end-=1
                    else:
                        end -= 1
                        board[i][end] = tmp
    # 왼쪽                    
    elif direct == 1:
        for i in range(n):
            end = 0
            for j in range(1,n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][end] == 0:
                        board[i][end] = tmp
                    elif tmp == board[i][end]:
                        board[i][end] = board[i][end]*2
                        end+=1
                    else:
                        end += 1
                        board[i][end] = tmp
    # 위
    elif direct == 2:
        for i in range(n):
            end = 0
            for j in range(1,n):
                if board[j][i]:
                    tmp = board[j][i]
                    board[j][i] = 0
                    if board[end][i] == 0:
                        board[end][i] = tmp
                    elif tmp == board[end][i]:
                        board[end][i] = board[end][i]*2
                        end+=1
                    else:
                        end += 1
                        board[end][i] = tmp
    # 아래
    elif direct == 3:
        for i in range(n):
            end = n-1
            for j in range(n-2,-1,-1):
                if board[j][i]:
                    tmp = board[j][i]
                    board[j][i] = 0
                    if board[end][i] == 0:
                        board[end][i] = tmp
                    elif tmp == board[end][i]:
                        board[end][i] = board[end][i]*2
                        end -= 1
                    else:
                        end -= 1
                        board[end][i] = tmp
    return board

def simulate(curr, board):
    global ans
    if curr == 5:
        for i in range(n):
            for j in range(n):
                ans = max(ans,board[i][j])
        return
   
    
    for i in range(4):
        tmp = merge(i,deepcopy(board))
        simulate(curr+1,tmp)


    
ans = 0
simulate(0,deepcopy(grid))
print(ans)
    
    
