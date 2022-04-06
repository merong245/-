n= int(input())

# dp[i][0] 왼쪽, dp[i][1] 오른쪽, dp[i][2] 안붙음
dp = [[0]*3 for _ in range(n+1)]

for i in range(1,n+1):
    if i == 1:
        for j in range(3):
            dp[1][j] = 1
        continue
    dp[i][0] = (dp[i-1][1] + dp[i-1][2])%9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2])%9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2])%9901
    
print(sum(dp[n])%9901)
