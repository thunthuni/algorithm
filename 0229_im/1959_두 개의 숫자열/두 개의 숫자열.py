import sys
sys.stdin = open('input.txt')


def sum(short_r, long_r, short_l, long_l):  # 매개변수는 범위
    max_v = 0
    for l_idx in range(long_r):   # 더 긴 배열
        if l_idx + short_r > long_r: # 만약 짧은 배열 범위 더했을 때 긴 배열의 범위를 벗어난다면
            break   # 멈추고 그때까지 max 값 출력
        sum_v = 0  # 누적합 구할 거
        i = 0  # 짧은 배열 인덱스와 함께 맞춰갈 때 쓸 인덱스
        for s_idx in range(short_r):  # 더 짧은 배열
            if l_idx + i < long_r:  # 인덱스 범위 안 벗어나게
                sum_v += long_l[l_idx + i] * short_l[s_idx]
                i += 1
    #     print(sum_v)
    # print()
        if max_v < sum_v:
            max_v = sum_v
    print(f'#{tc} {max_v}')

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N < M:
        sum(N, M, A, B)
    elif N > M:
        sum(M, N, B, A)
    elif N == M:
        sum(N, M, A, B)
