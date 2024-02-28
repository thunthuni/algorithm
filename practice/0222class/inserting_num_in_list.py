N = int(input())
arr = [[0]*7 for _ in range(2)]

t1 = N
for i in range(4):
    arr[0][i] = t1
    t1 += 1

t2 = N
for j in range(6, 2, -1):
    arr[1][j] = t2
    t2 -= 1

print(arr[0])
print(arr[1])