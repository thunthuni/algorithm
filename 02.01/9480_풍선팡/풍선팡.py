import sys
sys.stdin = open('input1.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [0, 1, 0, -1]  # 우 하 좌 상
    dc = [1, 0, -1, 0]

    max_v = 0
    for row in range(N):
        for col in range(M):
            value = arr[row][col]
            sum_v = arr[row][col]
            for k in range(4):
                for i in range(1, value + 1):
                    nr = row + (dr[k]*i)
                    nc = col + (dc[k]*i)
                    if 0 <= nr < N and 0 <= nc < M:
                        sum_v += arr[nr][nc]
            if max_v < sum_v:
                max_v = sum_v
    print(f'#{tc} {max_v}')