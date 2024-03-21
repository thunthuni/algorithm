import sys
sys.stdin = open('input.txt')

def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a)//2]
    smaller_arr, equal_arr, bigger_arr = [], [], []
    for num in a:
        if num < pivot:
            smaller_arr.append(num)
        elif num > pivot:
            bigger_arr.append(num)
        else:
            equal_arr.append(num)
    A = list(quick_sort(smaller_arr) + equal_arr + quick_sort(bigger_arr))
    return A


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    B = quick_sort(arr)
    print(f'#{tc} {B[N//2]}')

