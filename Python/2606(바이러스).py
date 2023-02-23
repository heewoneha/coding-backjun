from collections import deque

def bfs(start):
    global count

    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        s = q.popleft()

        for x in m[s]:
            if visited[x] == 0:
                q.append(x)
                visited[x] = 1
                count += 1


N = int(input()) # 컴퓨터의 수
M = int(input()) # 컴퓨터의 쌍 수

m = [[] for _ in range(0, N+1)]
for _ in range(0, M):
    x, y = map(int, input().split())
    m[x].append(y)
    m[y].append(x)

visited = [0 for _ in range(0, N+1)]

count = 0
bfs(1)

print(count)