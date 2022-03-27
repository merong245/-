import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    while q:
        x = q.popleft()

        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

n, m = map(int,input().split())


graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    u, v= map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
q = deque()

for i in range(1,n+1):
    if not visited[i]:
        visited[i] = True
        q.append(i)
        bfs()
        cnt += 1
print(cnt)
    
    
