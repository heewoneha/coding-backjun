import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    if x<0 or y<0 or x>=N or y>=M:
        return False

    if m[x][y] == 1:
        m[x][y] = 0
        for i in range(0, 4):
            dfs(x + dx[i], y + dy[i])
        return True

# -----

T = int(input()) # the number of test cases

for _ in range (0, T):
    answer = 0
    M, N, K = map(int, input().split())

    m = [[0]*M for _ in range(0, N)]

    for _ in range(0, K):
        a, b = map(int, input().split())
        m[b][a] = 1

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    for i in range(0, N):
        for j in range(0, M):
            if dfs(i, j) == True:
                answer += 1

    print(answer)