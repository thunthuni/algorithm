def f(i, k, t): # k개의 원소를 가진 배열A, 부분집합 합이 t인 경우
    if i == k:   # 모든 원소에 대해 결정하면
        sum_v = 0
        for j in range(k):
            if bit[j] == 1:  # A[i]가 포함된 경우
                sum_v += A[j]
        if sum_v == t:
            for j in range(k):
                if bit[j]:
                    print(A[j], end = '')
            print() # 부분집합 출력
    else:
        for j in range(1, -1, -1):
            bit[i] = j
            f(i+1, k, t)
        # bit[i] = 1
        # f(i+1, k)
        # bit[i] = 0
        # f(i+1, k)
N = 10
A = [1,2,3,4,5,6,7,8,9,10]
bit = [0] * N    # bit[i] 는 A[i]가 부분집합에 포함되는지 표시
f(0, N, 10)