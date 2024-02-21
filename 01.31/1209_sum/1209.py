import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input)
    arr = [list(map(int, input().split())) for _ in range(N)]

# 필요한 것 :
# 각 row 의 합
# 각 column의 합
# 두개의 대각선의 합
    # 이것들을 다 하나의 리스트에 넣어서 맥스값을 구해보자


    # row의 합 구하기
        # row 는 그대로 column 은 1씩 증가함
    rows_sum = []
    for row in range(100):
        for column in range(100):
            # column 이 하나씩 증가하는 것을 어떻게 표현하면 될까?
            rows_sum.append(arr[row][column])
            column += 1

    # column의 합 구하기
    columns_sum = []
    for column in range(100):
        for row in range(100):
            columns_sum.append(arr[column][row])
            row += 1

    # 대각선의 합
    diagonal_sum = []
    right_diagonal = 0
    left_diagonal = 0
    for i in range(N):
        right_diagonal += arr[i][i]
        left_diagonal += arr[i][N - 1 - i]
