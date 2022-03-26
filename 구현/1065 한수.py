n = int(input())

cnt = 0
for i in range(1,n+1):
    if len(str(i)) < 2:
        cnt += 1
        continue
    temp = str(i)
    gap = int(temp[0]) - int(temp[1])
    flag = False
    for k in range(1,len(temp)):
        if gap == int(temp[k-1]) - int(temp[k]):
            flag = True
        else:
            flag= False
            break
    if flag:
        cnt += 1
print(cnt)

