N = int(input())

def dfs(cnt):
    if cnt == len(l):
        print(''.join(answer))

    for x in visited.keys():
        if visited[x] != 0:
            visited[x] -= 1
            answer.append(x)
            dfs(cnt + 1)
            answer.pop()
            visited[x] += 1
    

for _ in range(0, N):
    l = sorted(list(input()))

    visited = {}
    answer = []

    for x in l:
        if x not in visited.keys():
            visited[x] = 1
        else:
            visited[x] += 1


    dfs(0)