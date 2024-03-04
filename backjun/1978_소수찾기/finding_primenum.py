N = int(input())
numbers = list(map(int, input().split()))
if 1 in numbers:
    numbers.remove(1)
result = 0
for num in numbers:
    # if num != 1:
    count = 0
    for dividor in range(2, num):
        if num % dividor == 0:
            count += 1
            break
    if count == 0:
        result += 1
print(result)