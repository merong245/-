from itertools import combinations as c
li = []

for _ in range(9):
    li.append(int(input()))

a = list(c(li,7))
for i in a:
    if sum(i) == 100:
        for i in sorted(i):
            print(i)
        break


    
