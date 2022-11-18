import heapq

n, m = map(int, input().split())

distance = [int(1e9)] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start):
    pq = []
    distance[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        dist, now = heapq.heappop(pq)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = i[1] + dist
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(pq, (cost, i[0]))


dijkstra(1)
print(distance[n])
