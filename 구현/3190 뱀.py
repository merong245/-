from collections import deque
import sys
input = sys.stdin.readline

# 보드의 크기
n = int(input())
# 사과 개수
k = int(input())

# 보드 판
grid = [[0]*n for _ in range(n)]

# 사과 위치 저장
for i in range(k):
    x,y = map(int,input().split())
    # 사과위치 2로 저장 
    grid[x-1][y-1] = 2


# 방향 변환 수
l = int(input())

direct = []
for _ in range(l):
    t, d = input().split()
    direct.append((int(t),d))

# 방향변환
def change_direct(d,c):
    if d == 'L':
        c = (c-1)%4
    else:
        c = (c+1)%4
    return c
    
def can_go(x,y):
    return 0<=x<n and 0<=y<n

def simulate():
    # 초기 설정
    c_direct = 0
    time = 0
    x, y= 0, 0

    # 뱀의 머리부터 몸통
    snake = deque()
    snake.append((x,y))
    
    dxs, dys = [0,1,0,-1],[1,0,-1,0]
    
    while True:
        time+=1
        x, y = x+dxs[c_direct], y+dys[c_direct]
        if can_go(x,y):
            # 사과가 있는 경우
            if grid[x][y] == 2:
                # 뱀의 머리만 이동
                grid[x][y] = 1
                snake.append((x,y))
            # 사과가 없는 경우
            elif grid[x][y] == 0:
                # 머리 이동
                grid[x][y] = 1
                snake.append((x,y))
                
                # 꼬리 빈칸으로 초기화
                tmp_x, tmp_y =snake.popleft()
                grid[tmp_x][tmp_y] = 0
            # 몸에 부딫힌 경우
            else:
                return time

            if len(direct) and direct[0][0] == time:
                time, n_direct = direct.pop(0)
                c_direct = change_direct(n_direct,c_direct)

        # 벽에 부딫힌 경
        else:
            return time
        
    
print(simulate())
