from copy import deepcopy
n, k = map(int,input().split())

fishes = [list(map(int,input().split()))]

# 수 조절
def adjust(fishes):
    temp_f = deepcopy(fishes)
    dxs , dys = [0,-1],[1,0]
    for i in range(len(fishes)):
        for j in range(len(fishes[i])):
            for dx, dy in zip(dxs,dys):
                nx = i+dx
                ny = j+dy
                if 0 <= nx < len(fishes) and 0 <= ny < len(fishes[i]) and ny<len(fishes[nx]):
                    d = abs(fishes[i][j]-fishes[nx][ny])//5
                    if d > 0:
                        if fishes[i][j] > fishes[nx][ny]:
                            temp_f[i][j] -= d
                            temp_f[nx][ny] += d
                        else:
                            temp_f[i][j] += d
                            temp_f[nx][ny] -=d
    return deepcopy(temp_f)

# 가장 왼쪽에 있는 어항부터
def seq(fishes):
    temp_f = []
    for j in range(len(fishes[0])):
        for i in range(len(fishes)-1,-1,-1):
            temp_f.append(fishes[i][j])
    for i in range(len(fishes[0]),len(fishes[-1])):
        temp_f.append(fishes[-1][i])

    return [deepcopy(temp_f)]

def check(fishes,k):
    max_f = max(fishes[0])
    min_f = min(fishes[0])
    return max_f-min_f <= k
cnt = 0
while True:
    # 물고기 수 차이 확인
    if check(fishes,k):
        break
    cnt += 1
    # 어항 한번 정리
    min_f = min(fishes[0])

    for i in range(len(fishes[0])):
        if min_f == fishes[0][i]:
            fishes[0][i]+=1

    # 어항 쌓기
    # 가장 오른쪽 어항을 그 어항의 오른쪽 위에 놓기
    # 공중부양 후 90도 회전
    fishes =[[fishes[0][0]],fishes[0][1:]]

    while True:
        if len(fishes)<=len(fishes[-1])-len(fishes[0]):
            tmp1 = []
            for j in range(len(fishes[0])):
                tmp2 = []
                for i in range(len(fishes)-1,-1,-1):
                    tmp2.append(fishes[i][j])
                tmp1.append(tmp2)
            tmp1.append(fishes[-1][len(fishes[0]):])
            fishes = deepcopy(tmp1)
        else:
            break

    # 수 조절
    fishes = adjust(fishes)

    # 다시 일렬로
    fishes = seq(fishes)
    # 다시 공중 부양
    for _ in range(2):
        temp_f = []
        for i in range(len(fishes)-1,-1,-1):
            temp_1 = []
            for j in range(len(fishes[-1])//2-1,-1,-1):
                temp_1.append(fishes[i][j])
            temp_f.append(temp_1)
        for t in range(len(fishes)):
            temp_1 = []
            for p in range(len(fishes[t])//2,len(fishes[t])):
                temp_1.append(fishes[t][p])
            temp_f.append(temp_1)
        fishes=deepcopy(temp_f)

    # 수 조절
    fishes = adjust(fishes)
    # 일렬로
    fishes = seq(fishes)

print(cnt)