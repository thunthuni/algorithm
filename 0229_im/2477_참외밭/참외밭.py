# 구하려고 하는 것: 참외의 총 개수 => 참외밭의 넓이
# 주어진 조건:
# 참외밭의 모양은 ㄱ을 90도, 180도, 270 도 회전한 육각형
# 동쪽: 1, 서쪽: 2, 남쪽: 3, 북쪽: 4

import sys
sys.stdin = open('input.txt')

one = int(input())
garo_lst = []
sero_lst = []

# index_lst = []
for tc in range(6):
    direction, length = list(map(int, input().split()))
    # index_lst.append(length)
    if direction == 1 or direction == 2:
        garo_lst.append(length)
    elif direction == 3 or direction == 4:
        sero_lst.append(length)

garo_lst.sort()
sero_lst.sort()
result = (garo_lst[2] * sero_lst[2] -
          (garo_lst[2]-garo_lst[1])*(sero_lst[2]-sero_lst[1]))

print(result * one)