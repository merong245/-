import sys
input =sys.stdin.readline

t = int(input())

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x,y):
    x = find_parent(x)
    y= find_parent(y)

    if x!=y:
        parent[x] =y
        cnt[y] += cnt[x]

for _ in range(t):
    f = int(input())
    parent = dict()
    cnt = dict()

    for _ in range(f):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            cnt[a] = 1
        if b not in parent:
            parent[b] = b
            cnt[b] = 1
        union_parent(a,b)
        print(cnt[find_parent(a)])
