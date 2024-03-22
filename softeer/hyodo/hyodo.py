# 주어진 밭: 3*3
# 각 땅의 높이 => 1~3
# 가로 / 세로로 최소 한줄의 높이가 같아야 농사를 지을 수 있음
# 빼거나 더해서 높이를 같게 만들어야 됨
# 구하고자 하는 것: 농사를 지을 수 있는 영역을 최소 1곳 이상 만들게 하는 최소비용

import sys
sys.stdin = open('input.txt')

arr = [list(map(int, input().split())) for _ in range(3)]

# 흠 일단 행, 열 탐색해서 값이 다 같은 줄이 있다면 바로 0 이 나와야되고
# 아니라면 출력값은 1 아니면 2 임
# 제일 큰값에서 작은값 빼서 2이면 2 1이면 1

result = 1
# 행 탐색
# 같은 줄이 이미 있다면 끝내버리기
for c in range(3):
    if arr[c] == [1]*3 or arr[c] == [2]*3 or arr[c] == [3]*3:
        result = 0
        break

# 열 탐색
col_lst = []
if result != 0:
    for c in range(3):
        col = []
        for r in range(3):
            col.append(arr[r][c])
        col_lst.append(col)
    for i in range(3):
        if col_lst[i] == [1] * 3 or col_lst[i] == [2] * 3 or col_lst[i] == [3] * 3:
            result = 0
        break

if result != 0:
    for i in range(3):
        if max(arr[i]) - min(arr[i]) == 1 or max(col_lst[i]) - min(col_lst[i]) == 1:
            result = 1
    else:
        result = 2
print(result)