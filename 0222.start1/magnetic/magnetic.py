import sys
sys.stdin = open('input.txt')

# 푸른 자성체 : N극에 이끌리는 성질
# 붉은 자성체: S극에 이글리는 성질
# 위는 N극: 푸른색은 위쪽으로 이끌림
# 아래는 S극 : 붉은색은 아래쪽으로 이끌림

# 교착상태 조건을 어떻게 해야 될까
# 1이 붉은 자성체 / 2는 푸른 자성체
# 1 이나 2 가 가려고 하는 방향에 자신과 반대성질의 자성체가 있다면, 교착상태이다
    # 1 의 아래에 2가 있다 / 2의 위에 1이 있다

# 그렇다면 교착상태의 개수는 어떻게 셀 수 있을까?
    # 빨간색 파란색 상관없긴 하지만 걍 파란색 하나만 찾아서 같은 열에서 교착상태의 조건에 해당하는지 찾고 찾으면 count +1

T = int(input())
for tc in range(1, T+1):


# 열검사 함수
def get_sero_cnt(col):
    cnt = 0
    # red 자성체를 체크
    is_red = False

    for row in range(N):
        # 1. red 자성체 발견
        if arr[row][col] == 1:
            is_red = True
        # 2. 이전에 red 자성체를 발견했고, 현재 blue 발견 cnt+=1
        elif is_red and arr[row][col] == 2:
            cnt += 1
            is_red = False # 갱신
    return cnt

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total_cnt = 0
    for col in range(N):
        total_cnt += get_sero_cnt(col)
    print(f'{tc} {total_cnt}')
