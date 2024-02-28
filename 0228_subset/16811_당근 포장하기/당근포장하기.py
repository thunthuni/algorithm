import sys
sys.stdin = open('input.txt')

# 문제의 조건
# 1) N 개의 당근을 주문하면 대, 중, 소 상자로 구분해 포장해야 한다
# 2) 같은 크기의 당근은 같은 상자에 들어있어야 한다
# 3) 비어 있는 상자가 있어서는 안된다
# 4) 한 상자에 N/2 개(소수점이면 내림) 를 초과하는 당근이 있어서도 안된다
# 5) 1~3 조건을 만족하면서 각 상자에 든 당근의 개수 차가 최소가 되도록 해야한다.
# 마지막 출력값: 각 상자에 든 당근의 개수 차
    # 포장할 수 없는 경우 즉, 조건을 다 만족할 수 업는 경우 -1


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
    counts = [0] * (max(carrots) + 1)  # 제일 큰 정수 크기 + 1만큼
    len_box1 = 0
    len_box2 = 0
    len_box3 = 0
    result = 0
    for num in carrots:
        counts[num] += 1
    for a in counts:
        if a > N//2:   # 4번째 조건
            # print(f'#{tc} {-1}')
            result = -1
            break

    if result != -1:
        for b in counts:
            if b != 0:
                if len_box1 < N//2 - 1:
                    len_box1 += b
                elif len_box2 < N//2 - 1:
                    len_box2 += b
                elif len_box3 < N//2 - 1:
                    len_box3 += b
        result = max(len_box1, len_box2, len_box3) - min(len_box1, len_box2, len_box3)

    print(f'#{tc}', result)
