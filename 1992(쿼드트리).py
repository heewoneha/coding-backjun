def quarter(x, y, n):
    start = l[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if start != l[i][j]:
                print('(', end='')
                quarter(x, y, n//2)
                quarter(x, y+n//2, n//2)
                quarter(x+n//2, y, n//2)
                quarter(x+n//2, y+n//2, n//2)
                print(')', end='')
                return

    if start == '0':
        print(0, end='')
        return

    elif start == '1':
        print(1, end='')
        return

N = int(input())
l = []

for i in range(0, N):
    l.append(list(input()))

quarter(0, 0, N)