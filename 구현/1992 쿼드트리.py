import sys
input = sys.stdin.readline

n = int(input())

grid = [list(input().rstrip()) for _ in range(n)]


def solution(x,y,n):
    
    color = grid[x][y]
    
    for i in range(x,x+n):
        for j in range(y,y+n):
            if grid[i][j] != color:
                print('(', end="")
                solution(x,y,n//2)
                solution(x,y+n//2,n//2)
                solution(x+n//2,y,n//2)
                solution(x+n//2,y+n//2,n//2)
                print(')' , end ="")
                return 
            
    print(color, end="")

solution(0,0,n)
