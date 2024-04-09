import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    real_nums = list(map(int, input().split()))
    lst = []  # 두수를 곱한 값을 넣는 리스트
    # length = len(lst)
    for i in range(N-1):  # 두수를 곱하기
        for j in range(i+1, N):
            lst.append(str(real_nums[i]*real_nums[j]))
    candidates = []  # 단조 증가하는 수들 (최대값 후보)
    for num in lst:   # 곱한 수가 들어있는 리스트에 들어있는 수: num
        if len(num) > 1: # 한 자리 수는 초반에 제외시키기( 단조 증가하는 수가 이미 아니기 때문)
            for idx in range(len(num)): # 단조 증가하는지 확인하는 반복문
                if idx + 1 < len(num):
                    if int(num[idx]) <= int(num[idx+1]):
                        continue  # 값의 모든 자릿수를 체크
                    else:
                        break  # 중간에 자릿수가 한번이라도 감소한다면 바로 반복문 탈출
                candidates.append(int(num)) # if 조건문을 자릿수 끝까지 거쳤다면 단조증가한다는 의미로 후보에 추가
    print(candidates)
    if len(candidates) > 0:
        print(f'#{tc} {max(candidates)}')
    else:  # 후보가 0개 라는 것은 단조증가하는 수가 없다는 뜻-> -1
        print(f'#{tc} -1')