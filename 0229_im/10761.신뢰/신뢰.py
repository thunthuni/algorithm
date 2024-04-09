import sys
sys.stdin = open('input.txt')

# 한 복도에 1 이상 100이하 정수로 구분되는 100개의 버튼이 존재
# 버튼 K는 복도의 시작점에서 K미터 떨어져 있다.
# 두 로봇은 버튼 1에서 시작
# 매 1초마다 로봇은 복도의 양 방향 중 하나로 1미터 걷거나,
    # 자기 위치에 있는 버튼을 누르거나,
    # 아무것도 하지 않는다
    # 두개의 루봇은 서로 다른 복도에 있다

T = int(input())
for tc in range(1, T+1):
    arr = input().split()
    arr.pop(0)
    N = len(arr)

    b_lst = []
    o_lst = []
    for i in range(0, N-1, 2):
        if arr[i] == 'B':
            b_lst.append(arr[i+1])
        else:
            o_lst.append(arr[i+1])
    print(b_lst)
    print(o_lst)
