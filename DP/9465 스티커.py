import sys
input = sys.stdin.readline

t = int(input())


for i in range(t):
    n = int(input())
    dp = [[0] * (n+1) for _ in range(2)]
    stickers = [list(map(int,input().split())) for _ in range(2)]
    for j in range(1,n+1):
        for k in range(2):
            if j == 1:
                dp[k][j] = stickers[k][j-1]
            else:
                dp[k][j] = max(dp[(k+1)%2][j-1],dp[k][j-2],dp[(k+1)%2][j-2])+stickers[k][j-1]


    print(dp[0][n] if dp[0][n] > dp[1][n] else dp[1][n])
