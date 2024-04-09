import sys
sys.stdin = open('input.txt')

# 게임의 룰 정리
    # 순서: 흑부터 시작해서 흑, 백 번갈아서
    # 돌 두기 룰:
        # 1) 자신이 놓을 돌과 돌 사이(가로/세로/대각선)에 상대편의 돌이 있을 경우
        # 2) 그때 사이에 있던 상대편의 돌은 자신의 돌
        # 3) 만약 돌을 놓을 곳이 없다면 상대편 플레이어 순서로
    # 종료조건: 보드에 빈 곳이 없거나/
              # 양 플레이어 모두 돌을 놓을 곳이 없으면
    # 구해야 하는 것:
        # 흑돌의 개수 백돌의 개수

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    A = N//2
    arr[A-1][A-1] = 'W'
    arr[A-1][A] = 'B'
    arr[A][A-1] = 'B'
    arr[A][A] = 'W'

    for i in range(M):
        r, c, color = list(map(int, input().split()))
        arr[r][c] = color
        # 오, 왼, 위, 아래,


