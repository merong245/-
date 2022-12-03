import sys
input = sys.stdin.readline

def choose(n):
    if not visited[nums[n]]:
        visited[nums[n]] = True
        up.add(n)
        down.add(nums[n])
        choose(nums[n])



T = int(input())
nums = [0]
answer = set()
for t in range(T):
    nums.append(int(input()))

for i in range(1,T+1):
    visited = [False for _ in range(T + 1)]
    up = set()
    down = set()
    choose(i)
    if up == down:
        answer = answer.union(up)



print(len(answer))
for i in sorted(list(answer)):
    print(i)

