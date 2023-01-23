import copy
import sys

sys.stdin = open("../input.txt", "r")
input = sys.stdin.readline

T = int(input())
now = list(input().rstrip())
target = list(input().rstrip())

temp = copy.deepcopy(now)
temp[0] = '1' if temp[0] == '0' else '0'
temp[1] = '1' if temp[1] == '0' else '0'

cnt1 = 0

# 0번째 스위치 동작 x
for i in range(1, T):
    if now[i - 1] != target[i - 1]:
        cnt1 += 1
        now[i - 1] = '1' if now[i - 1] == '0' else '0'
        now[i] = '1' if now[i] == '0' else '0'
        if i + 1 < T:
            now[i + 1] = '1' if now[i + 1] == '0' else '0'

cnt2 = 1
# 0번째 스위치 동작 o
for i in range(1, T):
    if temp[i - 1] != target[i - 1]:
        cnt2 += 1
        temp[i - 1] = '1' if temp[i - 1] == '0' else '0'
        temp[i] = '1' if temp[i] == '0' else '0'
        if i + 1 < T:
            temp[i + 1] = '1' if temp[i + 1] == '0' else '0'

answer = int(1e9)
if now == target:
    answer = cnt1
elif temp == target:
    answer = min(answer, cnt2)
else:
    answer = -1
print(answer)
