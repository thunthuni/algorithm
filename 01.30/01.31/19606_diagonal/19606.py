import sys
sys.stdin = open('input .txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    right_diagonal = 0
    left_diagonal = 0
    for i in range(N):
        right_diagonal += arr[i][i]
        left_diagonal += arr[i][N-1-i]


    print(f'#{tc} {right_diagonal + left_diagonal - arr[2][2]}')