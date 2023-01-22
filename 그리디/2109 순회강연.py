import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
answer = 0
lectures = []
for _ in range(n):
    p, d = map(int, input().split())
    lectures.append((p, d))

lectures.sort(key=lambda x: -x[0])
visited = [False] * 10001

for i in range(n):
    for j in range(lectures[i][1], 0, -1):
        if not visited[j]:
            answer += lectures[i][0]
            visited[j] = True
            break
print(answer)
