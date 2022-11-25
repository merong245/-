import sys

input = sys.stdin.readline


def solution(T):
    n = len(T)

    # 전체 a의 개수만큼 연결 되어있으면 됨
    # aabab a는 세개가 연결되어 있으면 된다
    # aab aba bab aba 최소 하나만 a랑 바꾸면 된다
    left = 0
    right = T.count('a')
    T = T * 2
    a_cnt = 0
    b_cnt = 0
    for i in range(right):
        if T[i] == 'a':
            a_cnt += 1
        else:
            b_cnt += 1
    answer = b_cnt

    for _ in range(n):

        if T[left] == 'a':
            a_cnt -= 1
        else:
            b_cnt -= 1

        if T[right] == 'a':
            a_cnt += 1
        else:
            b_cnt += 1

        left += 1
        right += 1
        answer = min(answer, b_cnt)

    return answer


T = input().rstrip()
print(solution(T))
