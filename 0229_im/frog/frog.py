import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    leaves = list(map(int, input().split()))

# 문제의 조건
# 연잎의 숫자가 양수 => 왼 -> 오
# 음수 => 오 -> 왼
# 한번 뒤로 갔다가 다시 앞으로 뛸 경우: abs(뒤로 간 칸) + 앞으로 뛸 칸 만큼 앞으로
# 연잎 범위를 벗어나는 경우 더 이상 점프하지 않음

    # 인덱스 1 부터 시작한다
    sum_v = 0
    count = 0
    idx = 0
    while count < K:   # 카운트가 점프 횟수보다 작을 때
        # 양수일때
        if leaves[idx] > 0:   # 연잎의 수가 양수일 때
            idx = idx + leaves[idx]  # 연잎의 위치 수 변경
            if 0 <= idx < N:  # 인덱스가 범위안에 잘 있는지 확인
                count += 1  # 한번 뛰었으니까 카운트 +1
                sum_v += leaves[idx] # 누적합 만들기
            else:   # 범위 밖으로 나갔다면 반복문 탈출
                break
        # 음수일때
        elif leaves[idx] < 0:  # 만약 연잎의 수가 음수일 때
            a = abs(leaves[idx])  # 음수 이후에 양수가 나올 경우를 대비해서 절대값으로 변수 저장해주기
            idx = idx + leaves[idx]  # 인덱스 이동
            if 0 <= idx < N:  # 인덱스 범위 확인
                count += 1  # 뛰었으니까 카운트 +1
                sum_v += leaves[idx]  # 누적합
                if leaves[idx] > 0:
                    idx = idx + a + leaves[idx]
                    count += 1
                    if 0 <= idx < N:
                        sum_v += leaves[idx]
                    else:
                        break
                elif leaves[idx] < 0:
                    continue
            else:
                break
        # 뒤로 갔다가 앞으로 뛰는 경우
        # if count == K:
        #     break
    print(sum_v)
