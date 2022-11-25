import sys
from collections import Counter
input = sys.stdin.readline


def solution(w, k):
    answer1 = int(1e9)
    answer2 = -int(1e9)
    idx = dict()
    # 개수가 k개 이상이어야 함
    alpha = Counter(w)
    alpha = [key for key, value in alpha.items() if value >= k]

    if len(alpha) == 0:
        print(-1)
        return

    # k개 이상인 알파벳의 인덱스를 저장함
    for i in range(len(w)):
        if w[i] in alpha:
            if w[i] not in idx:
                idx[w[i]] = [i]
            else:
                idx[w[i]].append(i)

    # 알파벳들의 각 인덱스의 차이로 정답을 구함
    for value in idx.values():
        left = 0
        right = k - 1

        # k 간격으로 한 칸씩 이동하며 인덱스 차의 최소, 최대를 구함
        for i in range(len(value) - k + 1):
            answer1 = min(value[right + i] - value[left + i] + 1, answer1)
            answer2 = max(value[right + i] - value[left + i] + 1, answer2)

    print(answer1, answer2)
    return


T = int(input())
for t in range(T):
    w = input().rstrip()
    k = int(input())
    solution(w, k)
