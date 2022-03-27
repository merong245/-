import sys
input = sys.stdin.readline

n , m = map(str,input().split())

n = list(n)
m = list(m)

def cal(n,m):
    res = 0
    for i in range(len(n)):
        if n[i] == '':
            continue
        if n[i] != m[i]:
            res += 1
    return res
    
ans = sys.maxsize
    
for _ in range(len(m)-len(n)+1):
    ans = min(ans,cal(n,m))
    n = [''] + n
    
    
print(ans)

