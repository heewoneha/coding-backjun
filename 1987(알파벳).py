def dfs(x, y):
    global maximum

    maximum = max(maximum, len(answer))    

    for i in range(0, 4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<R and 0<=ny<C:
            if m[nx][ny] not in answer:
                answer.add(m[nx][ny])
                dfs(nx, ny)
                answer.remove(m[nx][ny])


R, C = map(int, input().split())

m = []
for _ in range(0, R):
    m.append(list(input()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]

answer = set()
maximum = -1

answer.add(m[0][0])
dfs(0, 0)

print(maximum)