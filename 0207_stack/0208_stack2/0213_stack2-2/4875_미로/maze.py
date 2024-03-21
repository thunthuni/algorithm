# python
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    # 시작점은 2인곳
    # 방향키 설정
    # 0 인 곳으로 이동
    # 이동한 좌표를 stack에 저장
    # 이동하다가 1 로 막혀서 갈 곳이 없으면 stack 으로부터 0 이 나올 때까지 pop
    # 반복하다가 3을 찾으면 1 못찾으면 0

    stack = []
    row = N-1
    col = N-1
    dr = [0, 1, 0, -1]  # 우하좌상
    dc = [1, 0, -1, 0]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                row = i
                col = j

    # for row in range(N):
    #     for col in range(N):
    while row >= 0:
        for idx in range(4):
            next_row = row + dr[idx]
            next_col = col + dc[idx]

            if 0 <= next_row < N and 0 <= next_col < N:
                if arr[next_row][next_col] == 0:
                    arr[row][col] = 4
                    stack.append(next_row)
                    stack.append(next_col)
                    row = next_row
                    col = next_col

                elif arr[next_row][next_col] != 0:
                    count += 1

                # if arr[next_row][next_col] == 3:
                # 길이 막히면 돌아가야 되는데 어떻게... 막힌것을 알지
                # if row + dr[0:3], col + dr[0:3] 이 != 0 이라면 막힌거겠지?
