import sys
input = sys.stdin.readline
import heapq as h

n = int(input())
m = int(input())
inf = int(1e9)
graph = [[] for _ in range(n+1)]
distance = [inf for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int,input().split())
    graph[u].append([v,w])

start, end = map(int,input().split())

def dijkstra(start):
    pq = []

    h.heappush(pq,(0,start))
    distance[start] = 0

    while pq:
        dist, now = h.heappop(pq)

        if distance[now]< dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                h.heappush(pq,(cost,i[0]))
        

dijkstra(start)

print(distance[end])
