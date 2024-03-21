import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 2차원 리스트 탐색하는 문제이다
    # 이중 반복문을 이용해서 큰 배열에서 다른 배열을 반복해서 생성해서 가장 큰 값을 구해보자


    max_v = 0
    for row in range(N):
        for col in range(N):
            sum_v = 0
            for row_2 in range(row, row+M):
                for col_2 in range(col, col+M):
                    if 0 <= row_2 < N and 0 <= col_2 < N:
                        sum_v += arr[row_2][col_2]
            if max_v < sum_v:
                max_v = sum_v
    print(max_v)