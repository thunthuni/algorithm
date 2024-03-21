import sys
sys.stdin = open('input.txt')


def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a)//2]
    smaller_arr, equal_arr, greater_arr = [], [], []
    for num in a:
        if num < pivot:
            smaller_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(smaller_arr) + equal_arr + quick_sort(greater_arr)


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    result = quick_sort(arr)
    print(f'#{tc}', *result)