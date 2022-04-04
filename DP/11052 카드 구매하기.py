import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
cards = [0] + list(map(int,input().split()))
dp = [0]* (n+1)

dp[1] = cards[1]
for i in range(1,n+1):
    dp[i] = max(dp[i-1]+cards[1],cards[i])
print(dp[-1])
print(dp)
