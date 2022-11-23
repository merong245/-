import sys

input = sys.stdin.readline
from collections import deque

# 회전 초밥 벨트에 놓인 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
N, d, k, c = map(int, input().split())
q = deque()
now = deque()
for _ in range(N):
    q.append(int(input()))

# 원형이니 q 2개로 연결 초기 세팅
q.extend(q)

# k개 만큼 채워넣기
for i in range(k):
    now.append(q[i])

answer = 0
left = 0
right = k
# left가 마지막 인덱스까지
while left < N:
    # 서로 다른 초밥 종류
    temp = set(now)

    # 수열에 서비스 초밥 없는 경우
    if c not in temp:
        answer = max(answer, len(temp) + 1)
    # 수열에 서비스 초밥이 있는 경우
    else:
        answer = max(answer, len(temp))
    now.append(q[right])
    now.popleft()
    left += 1
    right += 1
print(answer)