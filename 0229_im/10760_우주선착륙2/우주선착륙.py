# 후보지를 기준으로 8방향을 갔을 때 후보지보다 낮은 지역이 4개 이상
# 델타 탐색해서 낮은 지역 카운트 하고 카운트가 4 이상이면 상위에서 카운트 1

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 탐색 방향키
    dr = [0, 1, 1, 1, 0, -1, -1, -1]
    dc = [1, 1, 0, -1, -1, -1, 0, 1]

    cnt2 = 0
    for row in range(N):
        for col in range(M):
            cnt1 = 0
            for k in range(8):
                nr = row + dr[k]
                nc = col + dc[k]
                if 0 <= nr < N and 0 <= nc < M:
                    if arr[row][col] > arr[nr][nc]:
                        cnt1 += 1
                        if cnt1 > 4:
                            break
            if cnt1 >= 4:
                cnt2 += 1
    print(f'#{tc} {cnt2}')