M, N = map(int, input().split()) # 1388번 <바닥 장식>

g = []

for i in range (0, M):
    g.append(list(input()))

# - : 행, | : 열

count = 0

for i in range(0, M): # 행
    tmp = ''
    for j in range(0, N):
        if g[i][j] == '-':
            if tmp != g[i][j]:
                count += 1
        tmp = g[i][j]

for j in range(0, N): # 열
    tmp = ''
    for i in range(0, M):
        if g[i][j] == '|':
            if tmp != g[i][j]:
                count += 1
        tmp = g[i][j]

print(count)