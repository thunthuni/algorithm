import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    # 가로 탐색
    result = 1
    for i in range(9):
        row_set = set(arr[i])
        if len(row_set) != 9:
            result = 0
            break

    # 세로 탐색
    if result != 0:
        for col in range(9):
            col_lst = []
            for row in range(9):
                col_lst.append(arr[row][col])
            if len(set(col_lst)) != 9:
                result = 0
                break

    # 박스 탐색
    if result != 0:
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                box_lst = []
                for roww in range(row, row + 3):
                    for coll in range(col, col + 3):
                        box_lst.append(arr[roww][coll])
                if len(set(box_lst)) != 9:
                    result = 0
                    break
    print(f'#{tc} {result}')
