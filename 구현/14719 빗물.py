import sys

input = sys.stdin.readline


def solution(H, W, blocks):
    answer = 0

    for i in range(1,W-1):
        left = max(blocks[:i])
        right = max(blocks[i+1:])

        #  작은 것 기준의 높이 만큼 물이 채워짐
        water = min(left,right)

        # 블록의 높이보다 물의 높이가 높은 경우
        # 물이 고임
        if blocks[i] < water:
            answer += water - blocks[i]

    return answer


H, W = map(int, input().split())
blocks = list(map(int, input().split()))
print(solution(H, W, blocks))
