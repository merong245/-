n = int(input())

stair = []
for _ in range(n):
    stair.append(int(input()))

#  n번째 까지 최댓값
dp = [0] * (n)


for i in range(n):
    if i == 0:
        dp[i] = stair[0]
    elif i == 1:
        dp[i] = stair[0]+stair[1]
    elif i == 2:
        dp[i] = max(stair[0],stair[1])+stair[2]
    else:
        dp[i] = max(stair[i-1]+dp[i-3],dp[i-2]) + stair[i]

print(dp[n-1])
