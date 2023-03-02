from collections import deque
import copy

def bfs_one(x, y):
    visit = [[0] * M for _ in range(0, N)]
    visit[x][y] = 1

    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M:
                if l[nx][ny] == 0 and visit[nx][ny] == 0:
                    l[x][y] -= 1
                    if l[x][y] < 0: # 보기 좋게 -1이하로 넘어가는 거 방지
                        l[x][y] = 0
                elif l[nx][ny] > 0 and visit[nx][ny] == 0:
                    q.append((nx, ny))
                    visit[nx][ny] = 1

def bfs_two(x, y, v):
    v[x][y] = 0

    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M and v[nx][ny] > 0:
                q.append((nx, ny))
                v[nx][ny] = 0

    return v


N, M = map(int, input().split())
l = []
for i in range(0, N):
    l.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

year = 1
for i in range(0, N):
    for j in range(0, M):
        if l[i][j] > 0:
            bfs_one(i, j)

            cnt = 0
            tmp = copy.deepcopy(l)
            for x in range(0, N):
                for y in range(0, M):
                    if tmp[x][y] > 0:
                        tmp = bfs_two(x, y, tmp)
                        cnt += 1
            
            if cnt > 1:
                print(year)
                exit()

            year += 1

if cnt < 2:
    print(0)