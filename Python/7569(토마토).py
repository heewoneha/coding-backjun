from collections import deque

def bfs():
    while q:
        x, y, z = q.popleft()

        for i in range(0, 6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0<=nx<H and 0<=ny<N and 0<=nz<M and l[nx][ny][nz] == 0:
                q.append((nx, ny, nz))
                l[nx][ny][nz] = l[x][y][z] + 1

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0 ,-1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

M, N, H = map(int, input().split()) # M: 열, N: 행, H: 높이
l = []
for i in range(0, H):
    tmp = []
    for j in range(0, N):
        tmp.append(list(map(int, input().split())))
    l.append(tmp)

q = deque()

for i in range(0, H):
    for j in range(0, N):
        for k in range(0, M):
            if l[i][j][k] == 1:
                q.append((i, j, k))

bfs()

maximum = 0
for i in range(0, H):
    for j in range(0, N):
        for k in range(0, M):
            if l[i][j][k] == 0:
                print(-1)
                exit()
            else:
                maximum = max(maximum, l[i][j][k])

print(maximum - 1)