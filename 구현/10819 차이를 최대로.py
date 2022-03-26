from itertools import permutations as p

n = int(input())

li = list(map(int,input().split()))

li = list(p(li,n))
max_num = -1

for i in range(len(li)):
    temp = 0
    
    for j in range(n-1):
        temp += abs(li[i][j]-li[i][j+1])
    max_num = max(max_num,temp)

print(max_num)
