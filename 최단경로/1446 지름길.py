# 그래프, 최단경로, 일방통행
# -> 다익스트라

import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(m + 1)]

dp = [i for i in range(m + 1)]
# 일방통행
for _ in range(n):
    a, b, c = map(int, input().split())
    if b > m:
        continue
    graph[a].append((b, c))
for i in range(m):
    graph[i].append((i+1,1))

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(pq, (cost, i[0]))


distance = [int(1e9)] * (m + 1)
dijkstra(0)
print(distance[m])
