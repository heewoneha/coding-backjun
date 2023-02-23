from collections import deque

def bfs():
    while q:
        x, y = q.popleft()

        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M and l[nx][ny] == 0:
                q.append((nx, ny))
                l[nx][ny] = l[x][y] + 1 # 익음

M, N = map(int, input().split()) # 행이 N, 열이 M
l = []
for i in range(0, N):
    l.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque()

for i in range(0, N):
    for j in range(0, M):
        if l[i][j] == 1:
            q.append((i, j))

bfs()

maximum = 0
for i in range(0, N):
    for j in range(0, M):
        if l[i][j] == 0:
            print(-1)
            exit()
        maximum = max(maximum, l[i][j])

print(maximum-1)