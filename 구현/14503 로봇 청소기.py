from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
r, c, d = map(int,input().split())

grid = [list(map(int,input().split()))
        for _ in range(n)]

visited = [[False]* m for _ in range(n)]

# 북 동 남 서
direct = [(-1,0),(0,1),(1,0),(0,-1)]

# 1.현재 위치 청소
# 2-1왼쪽에 청소하지않은 빈 공간있으면 왼쪽 회전후 전진
# 2-2 2-1이 4번 실행후 바로 뒤가 벽이라면 작동을 멈추고 아니면 한 칸 후진


def simulate(r,c,d):
    q = deque()
    q.append((r,c))

    while q:
        x,y = q.popleft()

        # 1 현재위치 청소
        visited[x][y] = True

        # 2
        for i in range(1,5):
            # 왼쪽 확인
            c_d= (d-i)%4
            nx, ny = x+direct[c_d][0], y+direct[c_d][1]
            # a 왼쪽에 청소하지 않은 빈공간?
            if not visited[nx][ny] and not grid[nx][ny]:
                # 왼쪽 회전후 전진
                d=c_d
                q.append((nx, ny))
                # 1로 돌아감
                break
                
            # b 네번 반복했으면
            if i == 4:
                nx, ny = x-direct[d][0], y-direct[d][1]
                # 뒤쪽이 벽이 아니라면
                if not grid[nx][ny]:
                    #한칸 후진
                    q.append((nx,ny))
                    # 1번으로 돌아감
                    break
                elif grid[nx][ny]:
                    # 벽이면 작동 멈춤
                    ans = 0
                    for i in range(n):
                        for j in range(m):
                            if visited[i][j]:
                                ans +=1
                    return ans

    

print(simulate(r,c,d))

            
        
    
print(*visited, sep="\n")

    
    
