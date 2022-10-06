import sys
input = sys.stdin.readline

def get_distance(x,y,opened):
    res = int(1e9)
    for cx,cy in opened:
        res = min(abs(x-cx) + abs(y-cy),res)
    return res

def choose(opened, depth,k):
    global ans
    if len(opened) == k:
        temp = 0
        for x,y in home:
            temp += get_distance(x,y,opened)
        ans = min(temp,ans)
        return
    elif depth == len(chickens):
        return


    opened.append(chickens[depth])
    choose(opened,depth+1,k)
    opened.pop()
    choose(opened, depth + 1,k)


n, m = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]

ans = int(1e9)
home = []
chickens = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            home.append((i,j))
        elif grid[i][j] == 2:
            chickens.append((i,j))


for i in range(1,m+1):
    choose([],0,i)
print(ans)