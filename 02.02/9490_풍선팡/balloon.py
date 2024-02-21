import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N행, M열
    arr = [list(map(int, input().split())) for _ in range(N)]

# 전체 배열을 탐색 하는 것
    dr = [0, 1, 0, -1, 0] #오,아,왼,위, 그대로
    dc = [1, 0, -1, 0, 0] #오,아,왼,위, 그대로

    sum_list = []
    for r in range(N):
        for c in range(M):
            sum = 0 # 한 점을 선택했을 때 상하좌우 에 있는 값들
            for k in range(5):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < M:
                    sum += arr[nr][nc]
                    # print(arr[nr][nc], end='')
            sum_list.append(sum)

    max_v = 0
    for value in sum_list:
        if max_v < value:
            max_v = value

    print(f'#{tc} {max_v}')

