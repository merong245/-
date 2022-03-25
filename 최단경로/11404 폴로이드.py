import sys
input = sys.stdin.readline
inf = int(1e9)

n = int(input())
m = int(input())

# 2차원 리스트
graph = [[inf for _ in range(n+1)]
         for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    u, v, w = map(int,input().split())
    # 같은 방향의 버스중 cost가 적은 버스 선택
    graph[u][v] = min(graph[u][v], w)

# 점화식을 따라 플로이드 워셜 알고리즘
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        # 도달 불가한 경우
        if graph[a][b] == inf:
            print(0, end = " ")
        else:
            print(graph[a][b], end=" ")
    print()
            
