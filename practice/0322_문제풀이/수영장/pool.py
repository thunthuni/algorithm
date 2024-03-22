import sys
sys.stdin = open('input.txt')

def dfs(month, sum_cost):
    global ans
    # 기저조건
    # 1. 12월까지 다 봤네? 종료
    if month > 12:
        # 최소비용
        ans = min(ans, sum_cost)
        return
    # 이미 최소값을 넘어가면 종료
    if sum_cost > ans:
        return

    # 모두 1일권으로 구매
    dfs(month+1, sum_cost + (days[month] * cost[0]))
    # 1달권 구매
    dfs(month + 1, sum_cost + cost[1])
    # 3달권 구매
    dfs(month + 3, sum_cost + cost[2])
    # 1년권 구매
    dfs(month+12, sum_cost + cost[3])


T = int(input())
for tc in range(1, T+1):
    cost = list(map(int, input().split()))
    days = [0] + list(map(int, input().split()))
    ans = int(1e9)
    dfs(1,0)
    print(f'#{tc} {ans}')


######### dp 로 풀기 ##################
T = int(input())
for tc in range(1, T+1):
    cost = list(map(int, input().split()))
    days = [0] + list(map(int, input().split()))

    plans = [0]*13

    # 1~12 까지 반복
    for i in range(1, 13):
        # 현재 달의 최소 비용 계산
        # 이전 달 + 1일권 구입 / 이전 달 + 1달권 구입 / 3달 전 + 3달권 구입 그 중에서 최소
        plans[i] = min(plans[i-1] + (days[i]*cost[0]), plans[i-1] + cost[1])

        if i >= 3:
            plans[i] = min(plans[i], plans[i-3] + cost[2])

        # 12월까지의 계산 결과 or 1년권
        min_cost = min(plans[12], cost[3])