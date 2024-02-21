import sys
sys.stdin = open('input.txt')

N = 25
numbers = int(input())
bingo = (int(input()) for _ in range(N))
print(bingo)

# 1부터 25 자연수
# numbers에 있는 수를 순서대로 지워나간다
# 지워진 수가 가로줄,세로줄,대각선인 경우 줄이 그어진다
# 이렇게 지워진 줄이 3개 이상일 경우 빙고이다
# 구하려고 하는 것은 사회자가 '몇번째' 수를 부를 때 빙고를 외치게 되는 것인지

# 흠 어떻게 풀면 좋을까
# 일단 숫자를 부르면 하나씩 x 로 바꿔
# X 의 수가 12개 이상일때부터 체크 들어가
# 가로줄, 세로줄, 대각선줄 중에 x 로만 채워진 리스트가 있는지 체크해
x_list = ['x'] * 5
# 세로줄 리스트 만들기
for col in range(N):
    col_list = []
    for row in range(N):
        col_list.append(bingo[row][col])
    result1 = ''.join(col_list)

right_diagonal = []
left_diagonal = []
for i in range(25):
    right_diagonal.append(bingo[i][i])
    left_diagonal.append(bingo[i][24-i])


# 부른 숫자를 X 로 바꾸기
count_x = 0
count_b = 0
for idx in range(len(numbers)):
    for idx_v in range(25):
        if numbers[idx] == bingo[idx_v]:
            bingo[idx_v] = 'x'
            count_x += 1
if count_x >= 12:
    for row in range(25):
        if bingo[row] == x_list:
            count_b += 1
    for col in range(25):
        if result1[col] == x_list:
            count_b += 1
    if right_diagonal == x_list:
        count_b += 1
    if left_diagonal == x_list:
        count_b += 1

if count_b >= 3:
    print()