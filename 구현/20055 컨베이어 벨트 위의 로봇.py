import sys
input =sys.stdin.readline
from collections import deque
# 2<= n <= 100
# 1<= k <= 2n
# 1 <= A <= 1000
# Ai 은 내구도

# 1 번 올리는 위치
# n번 내리는 위치 -> 도달 즉시 로봇은 내림

# 로봇이 올라가거나 로봇이 이동시 칸의 내구도는 1감소

# 1 로봇과 함께 벨트가 한칸 회전
# 2 먼저 올라간 로봇 부터 벨트 회전 방향으로 한칸 이동-> 불가시 정지
# 2-1 이동하려는 칸에 로봇이 없으며, 칸의 내구도가 1이상이여야함
# 3 올리는 위치에 칸의 내구도가 0이 아니면 로봇 올림
# 4 내구도 0 인 칸의 개수가 k개 이상이면 과정 종료 -> 아니면 1단계로 돌아감

# 종료시 단계 출력

n, k = map(int,input().split())
belt = deque(map(int,input().split()))
robot = deque([0 for _ in range(2*n)])
ans = 0

while True:
    # 1
    belt.rotate(1)
    robot.rotate(1)
    robot[n-1] = 0

    # 2
    for i in range(n-2,-1,-1):
        # 2-1
        if robot[i] and not robot[i+1] and belt[i+1]:
            robot[i+1] = 1
            robot[i] = 0
            belt[i+1] -= 1
    robot[n-1] = 0

    # 3
    if not robot[0] and belt[0]:
        robot[0] = 1
        belt[0] -= 1
    ans += 1
    if belt.count(0) >= k:
        break
print(ans)


