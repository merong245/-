import sys
from collections import deque
input=sys.stdin.readline

n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    v1, v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    
visited = [False] * (n+1)

def dfs(v):

    visited[v] = True
    print(v, end = " ")
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(i)

def bfs():

    while q:
        v = q.popleft()
        for i in sorted(graph[v]):
            if not visited[i]:
                q.append(i)
                visited[i] = True
                print(i, end = " ")
        
    
dfs(v)
print()

q= deque()
visited = [False] * (n+1)
visited[v] = True
q.append(v)
print(v, end = " ")
bfs()
