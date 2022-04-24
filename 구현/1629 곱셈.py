import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())

def power(a,b,c):
    if b==1:
        return a%c
    elif b==2:
        return a*a%c

    else:
        if b%2:
            return ((power(a,b//2,c)**2)*a)%c
        else:
            return ((power(a,b//2,c)**2))%c
print(power(a,b,c))

