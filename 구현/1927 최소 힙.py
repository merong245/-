import heapq as h
import sys
input = sys.stdin.readline
n= int(input())

pq = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if len(pq):
            print(h.heappop(pq))
        else:
            print(0)
    else:
        h.heappush(pq,x)
        
                   



