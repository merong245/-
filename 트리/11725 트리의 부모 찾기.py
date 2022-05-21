import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
nodes = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int,input().split())
    nodes[a].append(b)
    nodes[b].append(a)

def dfs(x, par):
    for y in nodes[x]:
        if y == par:
            continue
        parent[y] = x
        dfs(y, x)

dfs(1,-1)
for i in range(2,n+1):
    print(parent[i])


