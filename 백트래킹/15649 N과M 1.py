
n, m = map(int,input().split())
seq = []
def Choose():

    if len(seq) == m:
        print(' '.join(map(str,seq)))
        return

    for i in range(1, n+1):
        if i not in seq:
            seq.append(i)
            Choose()
            seq.pop()

Choose()
    
