import sys
sys.stdin = open('input.txt')

# 구하려는 것: 조망권이 확보된 세대의 수
    # 조망권이 확보됐다 -> 양 옆 두칸이 비어있다
# 필요한 것 : 각 건물의 i-2, i-1, i+1, i+2 의 높이
    # 옆 건물들중에 가장 높은 건물을 찾아야한다 (최댓값 찾기)
    # i - 최대값 = 각 건물에서 조망권이 확보된 세대의 수이다
    # 이걸 반복해서 sum 을 하면 된다

def solve(data):
    sum_v = 0
    for i in range(2, N-2):
        max = data[i-2]
        for b in [data[i-1], data[i+1], data[i+2]]:
            if b > max:
                max = b

    # 근데 그냥 무작정 최대값을 빼면 -가 생길 수도 있을텐데
    # 그럼 data[i] 가 구한 최대값보다 크다는 가정이 필요하겠다
            # 문제점을찾았어! 아래의 반복구문의 위치가 지금 문제야 어디로 가야할까

        if data[i] > max:
            sum_v += (data[i] - max)
    # 해치웠나...?
        # 호출해보자
        # 호출이 왜 안돼돼
    return sum_v
# T = int(input())
T = 10 # test case 가 주어졌을때 Vs. 입력으로 주어졌을 때
for tc in range(1, T+1):
    N = int(input()) # 총 건물의 개수 숫자로 바꿔주기(안 바꾸면 문자열임)
    # M = map(int, input().split())
    data = list(map(int, input().split()))
    result = solve(data)
    print(f'#{tc} {result}')
