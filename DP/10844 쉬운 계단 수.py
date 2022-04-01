n= int(input())

dp = [[0] *10 for _ in range(n)]

for i in range(1,10):
    dp[0][i] = 1

for i in range(1,n):
    for j in range(10):
        if j == 0:
            dp[i][j] =dp[i-1][j+1]
        elif 1<=j<=8:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
print(sum(dp[n-1])%1000000000)
    

'''
자리수      0 1 2 3 4 5 6 7 8 9


1자리수     0 1 1 1 1 1 1 1 1 1

2자리수     1 1 2 2 2 2 2 2 2 1

3자리수     1 3 3 4 4 4 4 4 3 2
'''
