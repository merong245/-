import sys
input = sys.stdin.readline

n= int(input())

res = []
li = [list(map(int,input().split()))
      for _ in range(n)]

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            li[i][j] = li[i][j] + li[i-1][j]
        elif i == j:
            li[i][j] = li[i][j] + li[i-1][j-1]
        else:
            li[i][j] = max(li[i-1][j], li[i-1][j-1])+li[i][j]

print(max(li[n-1]))
            
