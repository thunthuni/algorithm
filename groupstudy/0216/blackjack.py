import itertools

N, M = list(map(int,input().split()))
cards = list(map(int, input().split()))

def subsets(s, n):
    a = list(itertools.combinations(s, n))
    lst = []
    for i in a:
        lst.append(sum(i))
    for j in range(M, -1, -1):
        for i in lst:
            if i == j:
                print(j)
            else:
                continue

            # else:
            #     continue
subsets(cards, 3)





