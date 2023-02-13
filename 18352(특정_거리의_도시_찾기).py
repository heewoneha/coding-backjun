from collections import deque

def bfs(start):
    global count

    q = deque([start])
    visited[start] = 1

    while q:
        now = q.popleft()

        for i in m[now]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
                distance[i] = distance[now] + 1

                if distance[i] == K:
                    answer.append(i)


N, M, K, X = map(int, input().split())

visited = [0] * (N+1)
count = 0
distance = [0] * (N+1)
answer = []

m = [[] for _ in range (0, N+1)]
for _ in range(1, M+1):
    a, b = map(int, input().split())
    m[a].append(b)

bfs(X)

if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for i in range(0, len(answer)):
        print(answer[i], end = '\n')