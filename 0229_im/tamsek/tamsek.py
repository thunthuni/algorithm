import sys
sys.stdin = open('input.txt')

# 파리퇴치 스멜 난다
# 하지만 다른건 시작점/ 종료조건 이 문제에서 주어진다는 것

# 조건을 정리해보자
# M*M 크기의 행렬내의 최대값을 구한다
    # 최대값을 sum_v 에 넣는다
    # 최대값의 위치를 시작점으로 다시 M*M 크기의 탐색 재시작
    # 반복하면서 sum_v 에 계속 넣어준다
    # 종료조건 시작점이 최대값과 일치할 때!

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 탐색을 시작해보자
    row = 0
    col = 0
    sum_v = 0
    while row < N and col < N:
        max_v = 0
        for row_2 in range(row, row+M):  # N*N 큰 배열안에 M*M 크기의 배열만큼 탐색하는 반복문
            for col_2 in range(col, col+M):
                if 0 <= row_2 < N and 0 <= col_2 < N:  # 박스를 나가지 않게 하는 범위이다
                    value = arr[row_2][col_2]
                    if max_v < value: # 배열 안에서 최대값 구하기
                        max_v = value

        if arr[row][col] == max_v:
            if sum_v != 0:
                # print(f'#{tc} {sum_v}')
                print(f'#{tc}', (str(sum_v)))
            if sum_v == 0:
                print(f'#{tc}', (str(max_v)))
            break
        sum_v += max_v  # 누적합
        # max_v 의 위치값 찾기
        for i in range(row, row+M):
            for j in range(col, col+M):
                if 0 <= i < N and 0 <= j < N:
                    if arr[i][j] == max_v:
                        # print(i, j)
                        row = i
                        col = j
    # 내가 지금 막힌 부분:
        # 종료지점을 어떻게 만들어야 할지 잘 모르겠다
        # start 랑 max_v 랑 일치하면 while문을 나가면서 sum_v 값을 출력해야 한다
        # 해결
    # 또 막힌 부분:
        # 마지막 tc 가 제대로 나오지 않는다
        # 디버깅을 해보니까 탐색 배열이 1*1 이라서 sum_v 이 0 이 나와버린다
        # 해결
    # 라고 할뻔
        # 마지막 출력값을 한 칸 띄워서 출력해야 한다

