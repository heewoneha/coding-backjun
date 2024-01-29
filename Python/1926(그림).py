from collections import deque

def bfs(i, j):
    sum_all = 1
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and z[nx][ny]==1:
                q.append((nx, ny))
                z[nx][ny] = 0
                sum_all += 1

    return sum_all


dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
z = []

n, m = map(int, input().split())
for i in range(0, n):
    z.append(list(map(int, input().split())))

cnt = 0
max_area = 0
for i in range(0, n):
    for j in range(0, m):
        if z[i][j] == 1:
            z[i][j] = 0
            tmp = bfs(i, j)
            cnt += 1
            
            if tmp > max_area:
                max_area = tmp

print(cnt)
print(max_area)
