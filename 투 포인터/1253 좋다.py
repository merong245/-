import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
a.sort()
ans = 0

for i in range(n):
    l, r = 0,n-1
    while l < r:
        res =a[l]+a[r]
        if l == i:
            l+=1
            continue
        elif r == i:
            r-=1
            continue
        if res == a[i]:
            ans +=1
            break
        elif res > a[i]:
            r -= 1
        elif res < a[i]:
            l += 1

print(ans)


