from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(0, 8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<h and 0<=ny<w and m[nx][ny] == 1:
                q.append((nx, ny))
                m[nx][ny] = 0


dx = [-1, 0, 1, 0, 1, -1, -1, 1] # 대각선
dy = [0, 1, 0, -1, -1, 1, -1, 1]

w, h = map(int, input().split())

while True:
    cnt = 0
    if w == 0 and h == 0:
        break

    m = []
    for i in range(0, h):
        m.append(list(map(int, input().split())))

    for i in range(0, h):
        for j in range(0, w):
            if m[i][j] == 1:
                m[i][j] = 0
                bfs(i, j)
                cnt += 1

    print(cnt)
    w, h = map(int, input().split())
