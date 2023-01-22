import sys, heapq

sys.stdin = open("../input.txt", "r")
input = sys.stdin.readline

n = int(input())
answer = 0
lectures = []
for _ in range(n):
    p, d = map(int, input().split())
    lectures.append((p, d))

# 마감기한 순으로 오름차순 정렬
lectures.sort(key=lambda x: x[1])
pq = []

for lecture in lectures:
    # 마감 기한 순서로 금액을 기준으로 힙에 넣어주기
    heapq.heappush(pq, lecture[0])
    # 힙의 개수가 마감 기한보다 클 때 heappop시 가장 작은 금액의 녀석이 나감
    if (len(pq) > lecture[1]):
        heapq.heappop(pq)

# 남은 것을 모두 더했을 때 강연료가 가장 큰 경우
answer = sum(pq)
print(answer)
