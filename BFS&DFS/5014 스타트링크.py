import sys
from collections import deque
input = sys.stdin.readline


f,s,g,u,d = map(int,input().split())
s= s-1
g= g-1

elevator = [0] * f
visited = [0] * f

def bfs(f,s,u,d):
    q= deque()
    q.append(s)
    visited[s] = 1

    while q:
        n = q.popleft()
        if 0<= n+u < f and not visited[n+u]:
            q.append(n+u)
            visited[n+u] = visited[n] + 1
        if 0<= n-d < f and not visited[n-d]:
            q.append(n-d)
            visited[n-d] = visited[n] + 1


bfs(f,s,u,d)
print("use the stairs" if not visited[g] else visited[g]-1)
            
    
    
