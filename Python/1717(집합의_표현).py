import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000) # 재귀 깊이 줄였더니 맞음...ㅋ

def union(a, b):
    x = find(a)
    y = find(b)

    if x < y:
        l[y] = x
    else:
        l[x] = y

def find(x):
    if l[x] == x:
        return x

    parent = find(l[x])
    l[x] = parent
    return l[x]

N, M = map(int, input().split())
l = [i for i in range(0, N+1)]

for i in range(0, M):
    X, A, B = map(int, input().split())

    if X == 0: # union
        union(A, B)

    elif X == 1: # find -> 출력
        if find(A) == find(B):
            print('YES')
        else:
            print('NO')