import sys
from collections import deque
input = sys.stdin.readline

def solution(N):
    answer = 0
    q = deque([i+1 for i in range(N)])
    while len(q) > 1:
        q.popleft()
        q.append(q.popleft())
    answer = q[0]
    return answer

N = int(input())
print(solution(N))