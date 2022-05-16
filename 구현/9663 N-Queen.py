import sys

input = sys.stdin.readline

n = int(input())

# n번째 col의 선택된 행
row = [0] * n

ans = 0

def check(curr):
    for i in range(curr):
        if row[curr] == row[i] or abs(row[curr] - row[i]) == curr-i:
            return False
    return True

def choose(curr):
    global ans
    if curr == n:
        ans += 1
        return
    else:
        for i in range(n):
            row[curr] = i
            if check(curr):
                choose(curr+1)
choose(0)
print(ans)
