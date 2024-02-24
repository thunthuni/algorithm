import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    # [0][0] 부터 우, 하, 좌, 상 반복이다
    # 먼저 델타 탐색을 위해서 방향키를 설정한다
    # 오른쪽 방향부터 갈 수 있도록 설정한 다음 방향을 변경하는 조건을 설정한다
        # 배열의 벽에 닿으면 이라는 조건

    dr = [0, 1, 0, -1]  # 우, 하, 좌, 상 행
    dc = [1, 0, -1, 0]  # '' 열
    row = 0
    col = 0
    num = 1
    i = 0 # 방향키의 인덱스
    arr[row][col] = num
    while num < N*N:
        nr = row + dr[i]    # 다음 행선지 탐색
        nc = col + dc[i]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            row = nr
            col = nc
            num += 1
            arr[row][col] = num
        else:
            i = (i + 1) % 4

    print(f'#{tc}')
    for row in range(N):
        print(*arr[row])

        # if nr >= N or nr < 0 or nc >= N or nc < 0:




