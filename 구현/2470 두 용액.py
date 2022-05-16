import sys
input = sys.stdin.readline

n = int(input())

a = list(map(int,input().split()))
a.sort()

L = 0
R =n-1
v1, v2, best_sum =0,0,int(1e10)
while L<R:
    if best_sum > abs(a[L]+a[R]):
        best_sum = abs(a[L]+a[R])
        v1 = a[L]
        v2 = a[R]

    if a[L] + a[R] > 0:
        R -= 1
    else:
        L += 1
print(v1, v2)


