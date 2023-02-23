from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i, j))
    m[i][j] = 0

    count = 1

    while q:
        x, y = q.popleft()

        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if m[nx][ny] == 1:
                    m[nx][ny] = 0 # 이거 중요
                    q.append((nx, ny))
                    count += 1

    answer.append(count)
    return

N = int(input())
m = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = []

for _ in range(0, N):
    m.append(list(map(int,input())))

for i in range(0, N):
    for j in range(0, N):
        if m[i][j] == 1: # 이거 중요
            bfs(i, j)

answer.sort()
print(len(answer))

for x in answer:
    print(x)