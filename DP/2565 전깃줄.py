import sys
input = sys.stdin.readline

n = int(input())
lines = []
for _ in range(n):
    a ,b = map(int,input().split())
    lines.append((a,b))
lines.sort()

dp = [1] * n
def LIS():

    for i in range(1,n):
        for j in range(i):
            if lines[i][1] > lines[j][1] and dp[i] <= dp[j]:
                dp[i] = dp[j] + 1

    
LIS()
print(n-max(dp))
        
    
