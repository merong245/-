import heapq
import sys
input = sys.stdin.readline

N = int(input())
pq = []
for i in range(N):
    for j in list(map(int,input().split())):

        heapq.heappush(pq,j)
        if len(pq) > N:
            heapq.heappop(pq)

answer = heapq.heappop(pq)

print(answer)