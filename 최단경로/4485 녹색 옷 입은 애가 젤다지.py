import sys
import heapq as h
input = sys.stdin.readline
inf = sys.maxsize

def dijkstra():
    pq = []
    h.heappush(pq,(grid[0][0],0,0))
    distance[0][0] = 0

    while pq:
        cost, x, y = h.heappop(pq)
        if x == n-1 and y == n-1:
            print("Problem ",cnt,": ", distance[x][y], sep ="")
            break

        for dx, dy in zip(dxs,dys):
            nx, ny = dx+x, dy+y
            
            if 0<=nx<n and 0<=ny<n:
                new_cost = cost + grid[nx][ny]
                if new_cost < distance[nx][ny]:
                    distance[nx][ny] = new_cost
                    h.heappush(pq,(new_cost,nx,ny))
                

dxs, dys = [-1,1,0,0], [0,0,-1,1]

cnt = 1
while True :

    n = int(input())
    if n == 0:
        break
    
    grid = [list(map(int,input().split()))
            for _ in range(n)
            ]
    distance = [[inf for _ in range(n)]
                for _ in range(n)]

    dijkstra()
    cnt += 1
    
