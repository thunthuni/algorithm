#  N*N 배열
# 안에 숫자/ 지뢰/ 0
# 숫자 => 그 칸과 인접해 있는 칸중에서 지뢰가 있는 칸이 몇개
# 한칸에 여러개의 지뢰가 있을 수 도 있음

import sys
sys.stdin = open('input.txt')

# 그 전에  . 을 0 으로 바꿔줌
N = int(input())
arr = [list(input()) for _ in range(N)]

start_points = []  # 시작점 저장하기 (r, c, value)
for r in range(N):
    for c in range(N):
        if arr[r][c] == '.':
            arr[r][c] = 0
        else:
            start_points.append([r, c, int(arr[r][c])])
            arr[r][c] = '*'

# 방향키 생성 8방향
dr = [0, 1, 0, -1, -1, 1, 1, -1]  # 우, 하, 좌, 상 , 오위대, 오아대, 왼아대, 왼위대
dc = [1, 0, -1, 0, 1, 1, -1, -1]

length = len(start_points)
for i in range(length):
    row = start_points[i][0]
    col = start_points[i][1]
    num = start_points[i][2]
    for k in range(8):
        nr = row + dr[k]
        nc = col + dc[k]
        if 0 <= nr < N and 0 <= nc < N and not arr[nr][nc] in ['*','M']:
            arr[nr][nc] += num
            if arr[nr][nc] >= 10:
                arr[nr][nc] = 'M'

# 마무리 출력
for r in range(N):
    for c in range(N):
        arr[r][c] = str(arr[r][c])
for i in range(N):
    print(''.join(arr[i]))

