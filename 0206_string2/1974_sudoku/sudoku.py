import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    sudoku = [input() for _ in range(9)]


# 각 가로줄, 세로줄, 정사각형박스 리스트를 set 으로 만들어서
# len 이 하나라도 9가 나오지 않으면 0 을 출력하게 한다

# 먼저 column 을 만들자
    for col in range(9):
        col_str = ''
        for row in range(9):
            col_str += (sudoku[row][col])

        # column = ''.join(col_list)


    # HELP: 의도치 않은 엔터줄

# 정사각형 박스를 만들자
#     box_list = []
#     for idx in range(0, 9, 3):
#         for col in range(3):
#             a = col_str[idx:idx+3]
#         print(a)
        # 값만 뽑기
# HELP: 슬라이싱이 원는대로 되지 않음









# 가로줄
#     for row in range(9):
#         if len(set(sudoku[row])) != 9:
#             print(0)
#         for col in range(9):
#             for row_1 in range(9):

