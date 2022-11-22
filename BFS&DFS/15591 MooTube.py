import sys
from collections import deque

def bfs(k,v):
    q = deque()
    q.append((v, int(1e9)))
    visited = [False for _ in range(N + 1)]
    while q:
        now, usado = q.popleft()

        if not visited[now] and usado>=k:
            visited[now] = True
            q.extend(USADO[now])
    return sum(visited)
input = sys.stdin.readline

N, Q = map(int, input().split())
USADO = dict()

for _ in range(N - 1):
    p, q, r = map(int, input().split())
    if p in USADO:
        USADO[p].append((q, r))
    else:
        USADO[p] = [(q, r)]
    if q in USADO:
        USADO[q].append((p, r))
    else:
        USADO[q] = [(p, r)]

for _ in range(Q):
    answer = 0
    k, v = map(int, input().split())
    print(bfs(k,v)-1)

