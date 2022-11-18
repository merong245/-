def calc(a, b):
    cnt = 0
    for x,y in stars:
        if a<=x<=a+l and b<=y<=b+l:
            cnt += 1
    return cnt


n, m, l, k = map(int, input().split())

stars = [tuple(map(int, input().split())) for _ in range(k)]

answer = 0
for i,_ in stars:
    for _,j in stars:
        answer = max(calc(i, j), answer)
print(k-answer)
