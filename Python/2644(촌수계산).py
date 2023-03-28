from collections import deque

def bfs(x, y):
    q = deque()
    q.append(x)

    while q:
        x = q.popleft()

        for i in l[x]:
            if tmp[i] == 0:
                tmp[i] = tmp[x] + 1
                q.append(i)

    if tmp[y] > 0:
        return tmp[y]
    else:
        return -1

n = int(input())
a, b = map(int, input().split())
m = int(input())

l = [[] for _ in range(0, n+1)]
for _ in range(0, m):
    x, y = map(int, input().split())
    l[x].append(y)
    l[y].append(x) # 양방향

tmp = [0] * (n+1)

print(bfs(a, b))