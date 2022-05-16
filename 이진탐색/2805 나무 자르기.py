import sys
input =sys.stdin.readline

n, m = map(int,input().split())

trees = list(map(int,input().split()))

l ,r = 0, 2000000000
ans = 0

def can_get(h):
    res = 0
    for i in trees:
        if i > h:
            res += i-h

    return res >= m

while l <= r:
    h = (l+r)//2
    if can_get(h):
        ans = h
        l = h+1
    else:
        r = h -1

print(ans)