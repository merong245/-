from collections import deque
n, m = map(int,input().split())
q= deque()
visited = [False] * 200001
q.append((n,0))

while q:
    now, time = q.popleft()
    if 0 <= now < 200001 and not visited[now]:
        visited[now] = True
        if now == m:
            print(time)
            break

        q.append((now*2, time))
        q.append((now-1,time+1))
        q.append((now + 1, time + 1))


