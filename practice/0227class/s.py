
def repeat(x):
    strr = ''
    strr += str(x)
    if x == 3:
        print(strr)
        return

    for i in range(6):
        repeat(x+1)

