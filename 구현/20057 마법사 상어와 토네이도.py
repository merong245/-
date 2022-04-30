import sys
import math
input = sys.stdin.readline

def scatting(r,c,direct):
    global ans
    left = [(-1,-1,0.1),(-1,0,0.07),(-1,1,0.01),(-2,0,0.02),
            (0,-2,0.05),(1,-1,0.1),(1,0,0.07),(1,1,0.01),(2,0,0.02),(0,-1,0)]
    right = [(tr, -tc, ratio) for tr, tc, ratio in left]
    up = [(tc, -tr, ratio) for tr, tc, ratio in left]
    down = [(-tc, tr, ratio) for tr, tc, ratio in left]
    tmp = 0
    if direct == 0:
        for tr, tc, ratio in left:
            if ratio == 0:
                new_sand=grid[r][c] -tmp
            else:
                new_sand = math.floor(ratio*grid[r][c])
                tmp += new_sand

            if 0<= r+tr < n and 0<=c+tc<n:
                grid[r+tr][c+tc] += new_sand
            else:
                ans += new_sand
    elif direct == 1:
        for tr, tc, ratio in down:
            if ratio == 0:
                new_sand=grid[r][c] -tmp
            else:
                new_sand = math.floor(ratio*grid[r][c])
                tmp += new_sand

            if 0<= r+tr < n and 0<=c+tc<n:
                grid[r+tr][c+tc] += new_sand
            else:
                ans += new_sand
    elif direct == 2:
        for tr, tc, ratio in right:
            if ratio == 0:
                new_sand=grid[r][c] -tmp
            else:
                new_sand = math.floor(ratio*grid[r][c])
                tmp += new_sand

            if 0<= r+tr < n and 0<=c+tc<n:
                grid[r+tr][c+tc] += new_sand
            else:
                ans += new_sand
    elif direct == 3:
        for tr, tc, ratio in up:
            if ratio == 0:
                new_sand=grid[r][c] -tmp
            else:
                new_sand = math.floor(ratio*grid[r][c])
                tmp += new_sand

            if 0<= r+tr < n and 0<=c+tc<n:
                grid[r+tr][c+tc] += new_sand
            else:
                ans += new_sand
    grid[r][c] = 0

n = int(input())

grid = [list(map(int,input().split())) for _ in range(n)]

r, c = n//2, n//2

direct = 0
d = [(0,-1),(1,0),(0,1),(-1,0)]
s = [1,2]
ans = 0
flag = False
while True:

    for _ in range(s[0]):
        r, c = r+d[direct][0], c+d[direct][1]
        scatting(r,c,direct)
        if r==0 and c==0:
            flag = True
            break

    if flag:
        break

    s[1]-=1
    if s[1] == 0:
        s[0]+=1
        s[1] = 2
    direct = (direct + 1) % 4


print(ans)