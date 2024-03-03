import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrots = list(map(int, input().split()))

    counts = 1
    max_v = 0
    for idx in range(N):
        if idx + 1 < N:
            if carrots[idx] < carrots[idx+1]:
                counts += 1
            else:
                if max_v < counts:
                    max_v = counts
                counts = 1
    if max_v < counts:
        max_v = counts
    print(max_v)



