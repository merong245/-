import sys
import heapq as h

inf = sys.maxsize
# 노드, 간선의 개수
n,m = map(int,input().split())

# 시작 노드
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for _ in range(n+1)]
# 최단 거리 테이블
distance = [inf] * (n+1)

# 간선 정보 담기
for _ in range(m):
    u,v,w = map(int,input().split())
    # u에서 v로 가는 가중치 w
    graph[u].append((v,w))
    

def dijkstra(start):
    # heap을 위한 우선순위 큐
    pq = []
    # 시작 노드의 최단 경로는 0
    h.heappush(pq,(0,start))
    
    distance[start] = 0
    while pq:
        # 가장 짧은 최단거리의 노드 꺼내기
        dist, now = h.heappop(pq)

        # 이미 처리된 적 있는 노드라면 무시
        # 처리된 적이 없다면 distance[now]는 inf
        if distance[now] < dist:
            continue
        # 현재 노드와 인접한 노드들 확인
        for i in graph[now]:
            cost = dist+i[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] =cost
                h.heappush(pq,(cost,i[0]))

# 다익스트라 수행                
dijkstra(start)

# 모든 노드까지 거
for i in range(1,n+1):
    if distance[i] == inf:
        print("INF")
    else:
        print(distance[i])
    
    
