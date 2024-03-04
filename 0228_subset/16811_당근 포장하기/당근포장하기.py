import sys
sys.stdin = open('input.txt')

# 문제의 조건
# 1) N 개의 당근을 주문하면 대, 중, 소 상자로 구분해 포장해야 한다
# 2) 같은 크기의 당근은 같은 상자에 들어있어야 한다
# 3) 비어 있는 상자가 있어서는 안된다
# 4) 한 상자에 N/2 개(소수점이면 내림) 를 초과하는 당근이 있어서도 안된다
# 5) 1~3 조건을 만족하면서 각 상자에 든 당근의 개수 차가 최소가 되도록 해야한다.
# 마지막 출력값: 각 상자에 든 당근의 개수 차
    # 포장할 수 없는 경우 즉, 조건을 다 만족할 수 없는 경우 -1


# 예시 분석)
# 1) N = 3 / 당근의 크기 = [ 1, 2, 3]
# 2) N = 5/ 당근의 크기 = [1,1,1,2,3]
     # 4 조건을 만족하지 못함
# 3) N = 8 / 당근의 크기 = [1,2,3,4,5,6,7,8]
#     [1,2,3][4,5,6][7,8]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrots = list(map(int, input().split()))
    carrots.sort()
    # counts = [0] * (max(carrots) + 1)  # 제일 큰 정수 크기 + 1만큼   ## 0 이 아닐때를 고려해야됨
    min_value = N

    small = 0
    for s in range(N-2):
        small += 1
        if carrots[s] == carrots[s+1]:
            continue
        if small > N//2:
            break

        medium = 0
        for m in range(s+1, N-1):
            medium += 1
            if carrots[m] == carrots[m+1]:
                continue
            if medium > N//2:
                break

            # large = 0
            large = len(carrots[m+1:])
            if large > N//2:
                continue

            temp_max = max(small, medium, large)
            temp_min = min(small, medium, large)
            temp = temp_max - temp_min

            if min_value > temp:
                min_value = temp

    if min_value == N:
        min_value = -1
    print(f'#{tc} {min_value}')