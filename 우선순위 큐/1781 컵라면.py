import sys,heapq

input = sys.stdin.readline

n = int(input())

solved = [False] * 200_001
problems = []
answer = 0
pq = []
for _ in range(n):
    date, ramen = map(int, input().split())
    problems.append((date, ramen))

# 마감 기한 순으로 오름차순
problems.sort(key=lambda x: x[0])

for p in problems:
    # 우선순위 큐에 라면 수를 값으로 넣기
    heapq.heappush(pq,p[1])

    # 마감 기한이 pq의 길이보다 짧다면 해당 문제는 기한내에 풀 수 없음
    # 따라서 우선순위가 가장 낮은, 즉 라면 수가 가장 적은 노드를 pop
    if len(pq) > p[0]:
        heapq.heappop(pq)

answer = sum(pq)
print(answer)