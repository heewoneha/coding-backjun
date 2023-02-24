from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M and l[nx][ny] == 1:
                q.append((nx, ny))
                l[nx][ny] = 0

T = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(0, T):
    M, N, K = map(int, input().split()) # M:열, N: 행, K: 위치의 개수
    l = [[0] * M for i in range(0, N)]
    visited = [[0] * M for i in range(0, N)]

    for i in range(0, K):
        x, y = map(int, input().split())
        l[y][x] = 1


    cnt = 0
    for i in range(0, N):
        for j in range(0, M):
            if l[i][j] == 1:
                l[i][j] = 0 # visited
                bfs(i, j)
                cnt += 1

    print(cnt)
