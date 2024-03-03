C, R = list(map(int, input().split()))
K = int(input())

arr = [[0]*C for _ in range(R)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
row = R - 1
col = 0
num = 1
i = 0  # 방향키의 인덱스
arr[row][col] = num
while num < C * R:
    if K < 0 or K > C * R:
        print(0)
        break
    nr = row + dr[i]  # 다음 행선지 탐색
    nc = col + dc[i]
    if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] == 0:
        row = nr
        col = nc
        num += 1
        arr[row][col] = num
    else:
        i = (i + 1) % 4

arr.reverse()
for row in range(R):
    for col in range(C):
        if arr[row][col] == K:
            print(col+1, row+1)

