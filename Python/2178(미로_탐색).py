from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()
        #m[x][y] = 0
        #distance[x][y] = 1

        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < N) and (0 <= ny < M) and (m[nx][ny] == 1):
                q.append((nx, ny))
                m[nx][ny] = m[x][y] + 1
                #distance[nx][ny] = distance[x][y] + 1


N, M = map(int, input().split())
m = []
#distance = [[0 for j in range(0, M)] for i in range(0, N)]

for i in range(0, N):
    m.append(list(map(int, input())))

dx = [-1, 0, 1, 0]
dy = [0, 1 ,0, -1]

bfs(0, 0)

print(m[N-1][M-1])