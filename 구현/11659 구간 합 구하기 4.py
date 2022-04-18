import sys
input = sys.stdin.readline

n, m = map(int,input().split())

nums = list(map(int,input().split()))

prefix = [0]

for i in range(n):
    prefix.append(prefix[-1] + nums[i])

for _ in range(m):
    i, j = map(int,input().split())
    print(prefix[j] - prefix[i-1])
    
