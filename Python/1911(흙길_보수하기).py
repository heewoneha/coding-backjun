N, L = map(int, input().split())
tmp = []

for _ in range(0, N):
    tmp.append(list(map(int, input().split())))

tmp.sort(key=lambda x: x[0])


count = 0
cur = 0
for x, y in tmp:
    if cur > x:
        x = cur
    while x < y:
        x += L
        count += 1
    cur = x

print(count)