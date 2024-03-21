def binary_search(target, start, end, direction):
    # 종료 조건
    if start > end:
        return -1

    mid = (start + end) // 2
    middle = A[mid]
    # 가운데 있는 값이 찾으려는 값이면 종료
    if target == middle:
        return mid
    # 크면 오른쪽
    elif target > middle:
        res = binary_search(target, mid+1, end)
    # 작으면 왼쪽
    else:
        res = binary_search(target, start, mid-1)
    return res


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 이진 탐색을 위해 A를 정렬해야 함
    A.sort()
    # B에 있는 값을 하나:씩 A에 있는지 찾아야 함
    for t in B:
        print(t, end='>')
        result = binary_search(t, 0, N-1)
        print(result)