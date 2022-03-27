import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(i)

n, m = map(int,input().split())


graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    u, v= map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)
    
    
