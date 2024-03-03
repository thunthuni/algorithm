max_v = 0
        for b_idx in range(M):
            if b_idx + N > M:
                break
            sum_v = 0
            i = 0
            for a_idx in range(N):
                # if b_idx + i < M:
                sum_v += B[b_idx + i] * A[a_idx]
                i += 1
            if max_v < sum_v:
                max_v = sum_v
        print(max_v)