from collections import deque
import copy

def bfs(x, y, m):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N and m[nx][ny] == 0:
                q.append((nx, ny))
                m[nx][ny] = 1

    return

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
l = []

for i in range(0, N):
    l.append(list(map(int, input().split())))

maximum = l[0][0]
minimum = l[0][0]
for i in range(0, N):
    for j in range(0, N):
        maximum = max(maximum, l[i][j])
        minimum = min(minimum, l[i][j])

answer = []
for h in range(minimum, maximum + 1):
    m = copy.deepcopy(l)
    for i in range(0, N):
        for j in range(0, N):
            if m[i][j] <= h:
                m[i][j] = 1
            else:
                m[i][j] = 0

    cnt = 0
    for i in range(0, N):
        for j in range(0, N):
            if m[i][j] == 0:
                m[i][j] = 1
                bfs(i, j, m)
                cnt += 1

    answer.append(cnt)


if max(answer) == 0:
    print(1)
else:
    print(max(answer))