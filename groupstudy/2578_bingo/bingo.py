import sys
sys.stdin = open('input.txt')

arr = [list(map(int, input().split())) for _ in range(5)]
num_lst = []
for tc in range(5):
    lst = list(map(int, input().split()))
    for x in lst:
        num_lst.append(x)  # 사회자가 부르는 수의 인덱스를 쉽게 알기 위해서 1차원 리스트 사용

# 대각선 리스트 만들기
ld_lst = []
rd_lst = []
for i in range(5):
    rd_lst.append(arr[i][i])
    ld_lst.append(arr[i][5 - 1 - i])

# x_cnt = 0  # 뒤에 반복문을 덜 돌리기 위한 조건
bingo_cnt = 0  # 총 빙고를 외치는 수
row_cnt = [0] * 5  # 가로에서 지워지는 x 개수 저장소
col_cnt = [0] * 5   # 세로에서 지워지는 x 개수 저장소
left_diag = 0  # 왼쪽
right_diag = 0

# while bingo_cnt < 3:
# if bingo_cnt < 3:
for idx in range(25):  # 사회자가 부르는 수
    for row in range(5):
        for col in range(5):
            if arr[row][col] == num_lst[idx]:
                # x_cnt += 1
                row_cnt[row] += 1
                col_cnt[col] += 1
                if arr[row][col] in ld_lst:
                    left_diag += 1
                    if left_diag == 5:
                        bingo_cnt += 1
                if arr[row][col] in rd_lst:
                    right_diag += 1
                    if right_diag == 5:
                        bingo_cnt += 1
                if row_cnt[row] == 5:
                    bingo_cnt += 1
                if col_cnt[col] == 5:
                    bingo_cnt += 1

    if bingo_cnt >= 3:
        print(idx+1)
        break













