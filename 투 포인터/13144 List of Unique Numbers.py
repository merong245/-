import sys
input = sys.stdin.readline

n = int(input())

a = list(map(int,input().split()))


cnt = [0 for _ in range(max(a)+1)]

ans = 0
r = -1
for l in range(n):
    while r+1 < n and cnt[a[r+1]] == 0:
        r += 1
        cnt[a[r]] += 1
    ans += r-l + 1
    cnt[a[l]] -= 1
print(ans)




