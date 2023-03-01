from collections import deque

def bfs_one(x, y, value):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        l[x][y] = value

        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N and l[nx][ny] == 1:
                q.append((nx, ny))
                l[nx][ny] = value

    return

def bfs_two(z):
    global minimum

    q = deque()
    dist = [[-1] * N for _ in range(0, N)]

    for i in range(0, N):
        for j in range(0, N):
            if l[i][j] == z:
                dist[i][j] = 0
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N:
                if l[nx][ny] == 0 and dist[nx][ny] == -1: # -1은 바다
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
                elif l[nx][ny] > 0 and l[nx][ny] != z: # 다른 땅
                    minimum = min(minimum, dist[x][y])
                    return # bfs는 최단거리 구하니까

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
l = []

for i in range(0, N):
    l.append(list(map(int, input().split())))

cnt = 2 # 1로 하면 1이 원래 있던 값이라 오류
for i in range(0, N):
    for j in range(0, N):
        if l[i][j] == 1:
            bfs_one(i, j, cnt)
            cnt += 1

minimum = int(1e9)
for i in range(1, cnt):
    bfs_two(i)

if minimum != int(1e9):
    print(minimum)
else:
    print(0)