import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for row in range(N):
        count = 0
        for col in range(M):
            if arr[row][col] == 1:
                count += 1
                if col + 1 < M and arr[row][col+1] == 0:
                    break
        if max_v < count:
            max_v = count

    for col in range(M):
        count = 0
        for row in range(N):
            if arr[row][col] == 1:
                count += 1
                if row + 1 < N and arr[row+1][col] == 0:
                    break
        if max_v < count:
            max_v = count

    print(max_v)