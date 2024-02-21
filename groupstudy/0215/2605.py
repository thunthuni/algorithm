N = int(input())
card = list(map(int, input().split()))

student = list(range(1, N+1))
lst = [1]

for i in range(N):
    if i > 0:
        if card[i] != 0:
            lst.insert(len(lst)-card[i], student[i])
        else:
            lst.insert(student[i]-1, student[i])
print(*lst)