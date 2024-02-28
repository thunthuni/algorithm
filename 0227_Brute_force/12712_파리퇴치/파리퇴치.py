# right_diagonal = 0
# left_diagonal = 0
# for i in range(N):
#     right_diagonal += arr[i][i]
#     left_diagonal += arr[i][N - 1 - i]
#
# print(f'#{tc} {right_diagonal + left_diagonal - arr[2][2]}')

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 델타 탐색을 상, 하, 좌, 우 / 대각선을 해야 하는데
    # 일단 따로 하는게 좋을 듯 하다

#  가로 세로의 합
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    max_v = 0
    for row in range(N):
        for col in range(N):
            sum_v = arr[row][col]
            for k in range(4):
                for i in range(1, M):
                    nr = row + dr[k]*i
                    nc = col + dc[k]*i
                    if 0 <= nr < N and 0 <= nc < N:
                        sum_v += arr[nr][nc]
            if max_v < sum_v:
                max_v = sum_v

# 대각선
    dr_2 = [-1, 1, 1, -1]
    dc_2 = [1, 1, -1, -1]
    for row_2 in range(N):
        for col_2 in range(N):
            sum_v = arr[row_2][col_2]
            for k in range(4):
                for i in range(1, M):
                    nr_2 = row_2 + dr_2[k]*i
                    nc_2 = col_2 + dc_2[k]*i
                    if 0 <= nr_2 < N and 0 <= nc_2 < N:
                        sum_v += arr[nr_2][nc_2]
            if max_v < sum_v:
                max_v = sum_v
    print(f'#{tc} {max_v}')
