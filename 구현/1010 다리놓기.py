import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int,input().split())
    a=1
    b=1
    for i in range(2,n+1):
        a *= i
    for j in range(m,m-n,-1):
        b *= j

    print(b//a)
        
    
