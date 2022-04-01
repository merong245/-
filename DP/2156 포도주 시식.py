n= int(input())

wines = [int(input()) for _ in range(n)]

# n번째 까지 최대로 마실 수 있는 포도주의 양 
dp = [0] *n

for i in range(n):
    if i == 0:
        dp[0] = wines[0]
    elif i == 1:
        dp[1] = wines[1] + wines[0]
    elif i == 2:
        dp[2] = max(wines[1]+ wines[2], wines[0]+ wines[2],dp[1]) 
    else:
        dp[i] = max(dp[i-2]+wines[i], wines[i-1]+dp[i-3]+wines[i], dp[i-1])

print(max(dp))

