import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int,input().split())
    tower = [0 for _ in range(n+1)]
    time = [0] + list(map(int,input().split()))
    done = [0] * (n+1)
    order = [[] for _ in range(n+1)]

    for _ in range(k):
        a, b = map(int,input().split())
        order[a].append(b)
        tower[b] += 1

    w = int(input())
    q = deque()
    for i in range(1,n+1):
        if tower[i] == 0:
            q.append(i)
            done[i] = time[i]

    while q:
        x = q.popleft()

        for i in order[x]:
            tower[i] -= 1

            if tower[i] == 0:
                q.append(i)
            done[i] = max(done[i], done[x]+time[i])
    print(done[w])



