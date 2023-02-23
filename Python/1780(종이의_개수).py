def divide(x, y, n):
    global a, b, c
    start = l[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if start != l[i][j]:
                divide(x, y, n//3)
                divide(x, y+n//3, n//3)
                divide(x, y+2*n//3, n//3)

                divide(x+n//3, y, n//3)
                divide(x+n//3, y+n//3, n//3)
                divide(x+n//3, y+2*n//3, n//3)

                divide(x+2*n//3, y, n//3)
                divide(x+2*n//3, y+n//3, n//3)
                divide(x+2*n//3, y+2*n//3, n//3)

                return

    if start == -1:
        a += 1
    elif start == 0:
        b += 1
    elif start == 1:
        c += 1

N = int(input())
l = []

for i in range(0, N):
    l.append(list(map(int, input().split())))

a, b, c = 0, 0, 0
divide(0, 0, N)

print(a) # -1
print(b) # 0
print(c) # 1