from collections import deque

def bfs(i, j):
    cnt = 1 # 넓이
    q = deque()
    q.append((i, j))
    m[i][j] = 1

    while q:
        x, y = q.popleft()
        
        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and m[nx][ny] == 0:
                q.append((nx, ny))
                m[nx][ny] = 1
                cnt += 1
    answer.append(cnt)
    return True


M, N, K = map(int, input().split())

sq = []
for i in range(0, K):
    sq.append(list(map(int, input().split())))

m = [[0 for j in range(0, N)] for i in range(0, M)]

for i in range(0, K):
    for y in range(sq[i][1], sq[i][3]):
        for x in range(sq[i][0], sq[i][2]): # 그림이 뒤집어져도 ㄱㅊ
            m[y][x] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 0
answer = []

for i in range(0, M):
    for j in range(0, N):
        if m[i][j] == 0:
            if bfs(i, j) == True:
                count += 1

print(count)
answer.sort()
for i in range(0, len(answer)):
    print(answer[i], end=' ')