t = int(input())

for _ in range(t):
    n = int(input())
    jails = [0]*(n+1)
    for i in range(1,n+1):
        for j in range(0,n+1,i):
            if jails[j]:
                jails[j] = 0
            else:
                jails[j] = 1

    print(sum(jails[1:]))
    

