import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
cards = [0] + list(map(int,input().split()))
dp = [0]* (n+1)

dp[1] = cards[1]
for i in range(2,n+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i-j]+cards[j],dp[i])
print(dp[-1])
