# n x n 격자 , m개 파이어볼
# 첫 파이어볼은 각자 위치에서 이동 대기
# i번 파이어볼 m,d,s 질량, 방향, 속력
# 파이어볼 방향은 인접 8칸 의미
# 7 0 1
# 6   2
# 5 4 3

# 1 모든파이어볼이 자신의 방향d으로 속력 s만큼 이동
# 이동중에는 여러개 파이어볼 가능

# 2 이동끝난뒤 2개 이상의 파이어볼인 경우
# 2-1 하나로 합쳐짐
# 2-2 4개의 파이어볼로 나누어짐
# 2-3 각각 질량 속력 방향은 다음과 같음
# 2-3-1 질량 floor 질량의합/5
# 2-3-2 속력 floor 속력의 합/합챠진 파이어볼 개수
# 2-3-3 합쳐진 방향이 모두 홀수 or 짝수인 경우 0,2,4,6 아니면 1,3,5,7
# 2-4 질량 0의 파이어볼은 소멸

# 마법사가 k번 명령후 남아있는 질량의 합

import sys
from copy import deepcopy
import math
input = sys.stdin.readline



n,m,k = map(int,input().split())

grid = [[[] for _ in range(n)]
        for _ in range(n)]
#  r,c,m,s,d
fires = []
for _ in range(m):
    r,c,m,s,d = map(int,input().split())
    grid[r-1][c-1].append((m,s,d))

for _ in range(k):
    # 1
    dir = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    tmp = [[[] for _ in range(n)]
            for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for t in grid[i][j]:
                m,s,d = t[0],t[1],t[2]
                nr, nc = i+dir[d][0]*s, j+dir[d][1]*s
                nr = (n + nr)%n
                nc = (n + nc)%n
                tmp[nr][nc].append((m,s,d))
    grid = tmp


    # 2
    for i in range(n):
        for j in range(n):
            sum_m = 0
            sum_s = 0
            odd = 0
            cnt = len(grid[i][j])
            if cnt > 1:
                while grid[i][j]:
                    m,s,d = grid[i][j].pop()
                    sum_m += m
                    sum_s += s
                    if d%2:
                        odd+=1
                m = math.floor(sum_m/5)
                s = math.floor(sum_s/cnt)

                # 2-4
                if m == 0:
                    continue
                if odd==cnt or odd == 0:
                    for t in range(4):
                        grid[i][j].append((m,s,t*2))
                else:
                    for t in range(4):
                        grid[i][j].append((m,s,t*2+1))


ans = 0
for i in range(n):
    for j in range(n):
        for t in range(len(grid[i][j])):
            ans += grid[i][j][t][0]
print(ans)
