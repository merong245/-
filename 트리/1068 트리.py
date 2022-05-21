import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
parent = list(map(int,input().split()))
erase = int(input())

root = 0
v = [[] for _ in range(n)]
leaf = [0] * n
for i in range(n):
    if parent[i] == -1:
        root = i
    elif i == erase:
        continue
    else:
        v[parent[i]].append(i)

def dfs(x, par):
    if not v[x]:
        leaf[x] = 1
    for y in v[x]:
        if y == par:
            continue
        dfs(y,x)
        leaf[x] += leaf[y]

if root != erase:
    dfs(root,-1)
print(leaf[root])

