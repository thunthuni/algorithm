import sys
sys.stdin = open('input.txt')

d_num = []
t_num = []
def merge_sort(a):
    if len(a) < 2:
        return

    mid = len(a) // 2
    down_arr = merge_sort(a[:mid])

    top_arr = merge_sort(a[mid:])
    # t_num.append(top_arr[-1])
    # 병합 바로 직전

    merged_arr = []
    l = h = 0
    while l < len(down_arr) and h < len(top_arr):
        if down_arr[l] < top_arr[h]:
            merged_arr.append(down_arr[l])
            l += 1
        else:
            merged_arr.append(top_arr[h])
            h += 1
    merged_arr += down_arr[l:]
    merged_arr += top_arr[h:]
    return merged_arr, d_num, t_num

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    print(merge_sort(arr))