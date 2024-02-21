import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # K: 최대 이동횟수, N: 종점, M: 충전소 갯수
    K, N, M = map(int, input().split())
    # M개의 충전소
    station = list(map(int, input().split()))

    # 충전횟수를 저장할 변수
    charge = 0

    # 버스의 이동 변수
    move = K # 버스는 처음에 충전되어 있기 때문에

    # 마지막 충전소의 위치를 저장하는 변수
    last = 0
    while move < N:   # 버스가 종점에 도달하거나 넘어갈 때 까지
        for _ in range(K): # K만큼 갔기 때문에 K 번 되돌아 오면 된다.
            if move in station: # 이동한 거리에 충전소가 있다면
                charge += 1
                break           # 뒤로 되돌아갈 필요가 없기에 break
            move -= 1

        if last == move:  # 되돌아 갔을 때, 마지막 충전소 위치까지 왔다면
            charge = 0    # 더 이상 이동할 수 없음을 의미
            break

        last = move    # 새롭게 찾은 충전소 위치를 갱신
        move += K       # 다음 충전소를 찾기 위해 최대 이동

