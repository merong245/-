import sys
input = sys.stdin.readline

n = int(input())

grid = [list(map(int,input().split())) for _ in range(n)]

cnt_p1 = 0
cnt_0 = 0
cnt_m1 = 0
        

def solution(x,y,n):
    
    num = grid[x][y]
    global cnt_p1, cnt_0, cnt_m1
    
    for i in range(x,x+n):
        for j in range(y,y+n):
            if grid[i][j] != num:
                solution(x,y,n//3)
                solution(x,y+n//3,n//3)
                solution(x,y+n//3*2,n//3)
                solution(x+n//3,y,n//3)
                solution(x+n//3*2,y,n//3)
                solution(x+n//3,y+n//3,n//3)
                solution(x+n//3*2,y+n//3,n//3)
                solution(x+n//3*2,y+n//3*2,n//3)
                solution(x+n//3,y+n//3*2,n//3)
                return
    if num == 1:
        cnt_p1 +=1
    elif num == 0:
        cnt_0 +=1
    else:
        cnt_m1 +=1
            
solution(0,0,n)
print(cnt_m1, cnt_0, cnt_p1 , sep = "\n")
