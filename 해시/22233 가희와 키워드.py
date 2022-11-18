import sys

input = sys.stdin.readline
n, m = map(int, input().split())
keywords = {input().rstrip(): 1 for _ in range(n)}
for _ in range(m):
    memo = input().rstrip().split(',')
    for m in memo:
        if m in keywords:
            del keywords[m]
    print(len(keywords))
