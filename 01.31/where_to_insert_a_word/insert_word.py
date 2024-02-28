import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 어떻게 풀어보면 좋을까?
        # 행 탐색, 열 탐색 각각 진행해서 1이 연속적으로 K만큼 나오면 count+=1
    for