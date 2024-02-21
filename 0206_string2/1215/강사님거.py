import sys
sys.stdin = open('input.txt')


def is_pelindrome(string):
    M = len(string)  # 같은 값이 나오는 함수 실행은 한 번만 하면 됨
    # return string == string[::-1]
    for idx in range(M//2 + 1):
        if string[idx] != string[M-1-idx]:
            return False   # 하나라도 다르다면 false
    return True             # return 은 함수를 종료시키기 때문에
T = 10
for tc in range(1, T+1):
    N = 8  # 문자열의 개수
    M = int(input()) # 찾아야하는 문자열 개수
    arr = [input() for _ in range(N)]

    count = 0
    # 행, 열 탐색으로 길이가 M인 무자열을 만들자
    for outer in range(N):
        for inner in range(N - M +1):
            row_str = ''
            col_str = ''
            for idx in range(M):
                row_str += arr[outer][inner+idx]  # 행탐색
                col_str += arr[inner+idx][outer]  # 열탐색

            # 회문인지 판별
            if is_pelindrome(row_str):
                count += 1
            if is_pelindrome(col_str):
                count += 1
            # count += is_pelindrome(row_str) + is_pelindrome(col_str)
                # 암시적 형변환으로 인해서 true 는 1 false는 0 으로
    print(count)
