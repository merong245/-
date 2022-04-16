import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int,input().split()))

dp = [[1]*n for _ in range(3)]

def LIS():

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j] and dp[0][i] <= dp[0][j]:
                dp[0][i] = dp[0][j]+1
def LDS():
    nums.reverse()

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j] and dp[1][i] <= dp[1][j]:
                dp[1][i] = dp[1][j]+1
LIS()
LDS()
for i in range(n):
    dp[2][i] = dp[1][n-i-1]+dp[0][i]
print(max(dp[2])-1)

