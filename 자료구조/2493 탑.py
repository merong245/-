import sys

input = sys.stdin.readline


def solution(N, tops):
    answer = [0]*N
    stack = []
    for i in range(N):

        # 신호를 받을 타워가 있는 경우
        while stack:
            # 마지막 타워의 높이가 현재 타워보다 큰 경우
            if tops[stack[-1]] > tops[i]:
                # 현재 타워의 신호는 마지막타워가 받음
                answer[i] = stack[-1]+1
                break
            # 마지막 타워를 비움
            else:
                stack.pop()
        # 없는 경우 현재 인덱스를 추가
        stack.append(i)

    # 역순으로 출력
    for i in answer:
        print(i, end=' ')


N = int(input())
tops = list(map(int, input().split()))
solution(N, tops)
